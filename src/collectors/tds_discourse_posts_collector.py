import requests
import json
import time
import urllib.parse
from pathlib import Path
from typing import Dict, List, Optional, Set
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))

class TDSPostsCollector:
    def __init__(self):
        self.base_url = "https://discourse.onlinedegree.iitm.ac.in"
        self.rate_limit = 1.0
        self.output_dir = Path("data/raw/discourse")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.collected_topics = {}
        self.session = requests.Session()
        self._setup_authentication()
        self.stats = {
            'search_pages_processed': 0,
            'unique_topics_found': 0,
            'topics_successfully_collected': 0,
            'total_posts_collected': 0,
            'topics_with_pagination': 0,
            'topics_with_incomplete_posts': 0,
            'search_url_used': '',
            'collection_method': 'complete_search_api'
        }
    
    def _setup_authentication(self):
        import os
        session_token = os.getenv('DISCOURSE_SESSION_TOKEN')
        forum_session = os.getenv('DISCOURSE_FORUM_SESSION')
        
        if session_token:
            self.session.cookies.set('_t', session_token, domain='discourse.onlinedegree.iitm.ac.in')
        if forum_session:
            self.session.cookies.set('_forum_session', forum_session, domain='discourse.onlinedegree.iitm.ac.in')
        
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; TDS-Collection-Bot)',
            'Accept': 'application/json',
        })
    
    def collect_complete_tds_data(self, start_date: str, end_date: str) -> Dict:
        print(f"Complete TDS Data Collection: {start_date} to {end_date}")
        
        search_query = f"#courses:tds-kb after:{start_date} before:{end_date}"
        encoded_query = urllib.parse.quote(search_query)
        search_url = f"{self.base_url}/search.json?q={encoded_query}"
        
        self.stats['search_url_used'] = search_url
        print(f"Search URL: {search_url}")
        
        all_topic_ids = self._get_all_topics_from_search(search_url)
        if not all_topic_ids:
            print("No topics found in search results")
            return self.stats
        
        self.stats['unique_topics_found'] = len(all_topic_ids)
        print(f"Found {len(all_topic_ids)} unique topics")
        
        self._collect_all_posts_from_topics(all_topic_ids)
        self._save_complete_collection_metadata(start_date, end_date)
        self._generate_collection_report()
        
        return self.stats
    
    def _get_all_topics_from_search(self, search_url: str) -> List[int]:
        print("Collecting all topics from search results...")
        all_topic_ids: Set[int] = set()
        page = 0
        consecutive_empty_pages = 0
        max_consecutive_empty = 3
        
        while consecutive_empty_pages < max_consecutive_empty and page < 100:
            page += 1
            self.stats['search_pages_processed'] = page
            
            paginated_url = search_url if page == 1 else f"{search_url}&page={page}"
            
            try:
                response = self.session.get(paginated_url, timeout=15)
                
                if response.status_code == 403:
                    print("Authentication required - set DISCOURSE_SESSION_TOKEN and DISCOURSE_FORUM_SESSION")
                    break
                elif response.status_code != 200:
                    consecutive_empty_pages += 1
                    continue
                
                data = response.json()
                page_topics = set()
                
                for topic in data.get('topics', []):
                    if topic.get('id'):
                        page_topics.add(topic['id'])
                
                for post in data.get('posts', []):
                    if post.get('topic_id'):
                        page_topics.add(post['topic_id'])
                
                if page_topics:
                    new_topics = page_topics - all_topic_ids
                    all_topic_ids.update(page_topics)
                    consecutive_empty_pages = 0
                    print(f"Page {page}: {len(page_topics)} topics ({len(new_topics)} new)")
                else:
                    consecutive_empty_pages += 1
                
                time.sleep(self.rate_limit)
                
            except Exception as e:
                print(f"Error processing page {page}: {e}")
                consecutive_empty_pages += 1
                continue
        
        return list(all_topic_ids)
    
    def _collect_all_posts_from_topics(self, topic_ids: List[int]):
        print(f"Collecting ALL posts from {len(topic_ids)} topics...")
        
        for i, topic_id in enumerate(topic_ids):
            if i % 10 == 0:
                print(f"Topic {i+1}/{len(topic_ids)}: ID {topic_id}")
            
            try:
                topic_data = self._get_topic_with_complete_posts(topic_id)
                if topic_data:
                    self._save_topic_with_verification(topic_id, topic_data)
                    self.stats['topics_successfully_collected'] += 1
                    self.stats['total_posts_collected'] += len(topic_data.get('posts', []))
                    
                    if not topic_data.get('collection_status', {}).get('complete_collection', False):
                        self.stats['topics_with_incomplete_posts'] += 1
                
                time.sleep(self.rate_limit)
                
            except Exception as e:
                print(f"Error collecting topic {topic_id}: {e}")
                continue
    
    def _get_topic_with_complete_posts(self, topic_id: int) -> Optional[Dict]:
        try:
            response = self.session.get(f"{self.base_url}/t/{topic_id}.json", timeout=15)
            if response.status_code != 200:
                return None
            
            data = response.json()
            topic_info = {
                "topic_id": topic_id,
                "title": data.get("title", ""),
                "slug": data.get("slug", ""),
                "category_id": data.get("category_id"),
                "posts_count": data.get("posts_count", 0),
                "created_at": data.get("created_at"),
                "views": data.get("views", 0),
                "topic_url": f"{self.base_url}/t/{data.get('slug', topic_id)}/{topic_id}",
                "posts": []
            }
            
            post_stream = data.get("post_stream", {})
            initial_posts = post_stream.get("posts", [])
            declared_posts_count = data.get("posts_count", 0)
            
            for post in initial_posts:
                topic_info["posts"].append(self._extract_post_info(post, topic_info))
            
            posts_collected = len(initial_posts)
            if posts_collected < declared_posts_count:
                self.stats['topics_with_pagination'] += 1
                additional_posts = self._get_remaining_posts(topic_id, data)
                topic_info["posts"].extend(additional_posts)
                posts_collected += len(additional_posts)
            
            topic_info["collection_status"] = {
                "posts_declared": declared_posts_count,
                "posts_collected": posts_collected,
                "complete_collection": posts_collected == declared_posts_count,
                "collection_method": "complete_pagination" if posts_collected < declared_posts_count else "single_request"
            }
            
            return topic_info
            
        except Exception as e:
            return None
    
    def _get_remaining_posts(self, topic_id: int, initial_data: Dict) -> List[Dict]:
        additional_posts = []
        try:
            post_stream = initial_data.get("post_stream", {})
            stream = post_stream.get("stream", [])
            initial_post_ids = [post["id"] for post in post_stream.get("posts", [])]
            missing_post_ids = [pid for pid in stream if pid not in initial_post_ids]
            
            if missing_post_ids:
                chunk_size = 20
                for i in range(0, len(missing_post_ids), chunk_size):
                    chunk = missing_post_ids[i:i + chunk_size]
                    post_ids_str = "&".join([f"post_ids[]={pid}" for pid in chunk])
                    posts_url = f"{self.base_url}/t/{topic_id}/posts.json?{post_ids_str}"
                    response = self.session.get(posts_url, timeout=15)
                    
                    if response.status_code == 200:
                        posts_data = response.json()
                        for post in posts_data.get("post_stream", {}).get("posts", []):
                            additional_posts.append(self._extract_post_info(post, {"topic_id": topic_id}))
                    
                    time.sleep(self.rate_limit)
        except Exception:
            pass
        
        return additional_posts
    
    def _extract_post_info(self, post: Dict, topic_info: Dict) -> Dict:
        return {
            "post_id": post.get("id"),
            "post_number": post.get("post_number"),
            "username": post.get("username"),
            "name": post.get("name", ""),
            "created_at": post.get("created_at"),
            "updated_at": post.get("updated_at"),
            "cooked": post.get("cooked", ""),
            "raw": post.get("raw", ""),
            "reply_count": post.get("reply_count", 0),
            "like_count": post.get("like_count", 0),
            "post_url": f"{self.base_url}/t/{topic_info.get('topic_id', 'unknown')}/{post.get('post_number')}",
            "extracted_at": time.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def _save_topic_with_verification(self, topic_id: int, topic_data: Dict):
        safe_title = "".join(c for c in topic_data["title"] if c.isalnum() or c in (' ', '-', '_')).strip()[:50]
        filename = f"topic_{topic_id}_{safe_title}.json"
        filepath = self.output_dir / filename
        
        topic_data["collected_at"] = time.strftime('%Y-%m-%d %H:%M:%S')
        topic_data["filename"] = filename
        topic_data["collection_method"] = "complete_search_api"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(topic_data, f, indent=2, ensure_ascii=False)
        
        self.collected_topics[topic_id] = {
            "title": topic_data["title"],
            "posts_declared": topic_data["posts_count"],
            "posts_collected": len(topic_data.get("posts", [])),
            "complete": topic_data["collection_status"]["complete_collection"],
            "topic_url": topic_data["topic_url"],
            "filename": filename,
            "created_at": topic_data["created_at"]
        }
    
    def _save_complete_collection_metadata(self, start_date: str, end_date: str):
        metadata = {
            "collection_info": {
                "method": "complete_search_api",
                "search_url": self.stats['search_url_used'],
                "date_range": {"start_date": start_date, "end_date": end_date},
                "collected_at": time.strftime('%Y-%m-%d %H:%M:%S'),
                "statistics": self.stats
            },
            "completeness_verification": {
                "topics_with_complete_posts": len([t for t in self.collected_topics.values() if t["complete"]]),
                "topics_with_missing_posts": len([t for t in self.collected_topics.values() if not t["complete"]]),
                "total_posts_collected": sum(t["posts_collected"] for t in self.collected_topics.values()),
                "average_posts_per_topic": sum(t["posts_collected"] for t in self.collected_topics.values()) / len(self.collected_topics) if self.collected_topics else 0
            },
            "topics": self.collected_topics
        }
        
        metadata_file = self.output_dir / "complete_tds_collection_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    def _generate_collection_report(self):
        print(f"\nCOMPLETE TDS COLLECTION REPORT")
        print("=" * 60)
        print(f"Search URL: {self.stats['search_url_used']}")
        print(f"Search pages: {self.stats['search_pages_processed']}")
        print(f"Topics found: {self.stats['unique_topics_found']}")
        print(f"Topics collected: {self.stats['topics_successfully_collected']}")
        print(f"Posts collected: {self.stats['total_posts_collected']}")
        print(f"Topics with pagination: {self.stats['topics_with_pagination']}")
        print(f"Incomplete collections: {self.stats['topics_with_incomplete_posts']}")
