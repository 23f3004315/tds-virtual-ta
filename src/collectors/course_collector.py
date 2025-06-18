import requests
import json
import time
from pathlib import Path
from typing import Dict, List, Optional
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))
from config.settings import config

class TDSCourseCollector:
    def __init__(self):
        self.github_api = "https://api.github.com/repos"
        self.raw_base = "https://raw.githubusercontent.com"
        self.owner = "sanand0"
        self.repo = "tools-in-data-science-public"
        self.branch = "tds-2025-01"
        self.tds_base_url = "https://tds.s-anand.net/#/"
        self.output_dir = Path("data/raw/course")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.collected_files = []
    
    def collect_all_course_content(self) -> List[Dict]:
        print(f"Collecting TDS course content from {self.owner}/{self.repo}#{self.branch}")
        try:
            markdown_files = self._get_repository_markdown_files()
            if not markdown_files:
                print("No markdown files found")
                return []
            print(f"Found {len(markdown_files)} markdown files")
            for file_info in markdown_files:
                file_data = self._download_file_with_metadata(file_info)
                if file_data:
                    self.collected_files.append(file_data)
                time.sleep(0.1)
            self._save_collection_metadata()
            print(f"Course collection complete: {len(self.collected_files)} files")
            return self.collected_files
        except Exception as e:
            print(f"Course collection failed: {e}")
            return []
    
    def _get_repository_markdown_files(self) -> List[Dict]:
        tree_url = f"{self.github_api}/{self.owner}/{self.repo}/git/trees/{self.branch}?recursive=1"
        try:
            response = requests.get(tree_url, timeout=30)
            response.raise_for_status()
            tree_data = response.json()
            return [
                item for item in tree_data["tree"]
                if (item["type"] == "blob" and
                    item["path"].endswith(".md") and
                    not item["path"].startswith("."))
            ]
        except requests.RequestException as e:
            print(f"Failed to get repository tree: {e}")
            return []
    
    def _download_file_with_metadata(self, file_info: Dict) -> Optional[Dict]:
        file_path = file_info["path"]
        try:
            file_url = f"{self.raw_base}/{self.owner}/{self.repo}/{self.branch}/{file_path}"
            response = requests.get(file_url, timeout=30)
            response.raise_for_status()
            local_path = self.output_dir / file_path
            local_path.parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            return {
                "github_path": file_path,
                "local_path": str(local_path),
                "tds_link": self._generate_tds_link(file_path),
                "github_url": file_url,
                "content_size": len(response.text),
                "title": self._generate_title(file_path),
                "section": self._extract_section(file_path)
            }
        except Exception as e:
            print(f"Failed to download {file_path}: {e}")
            return None
    
    def _generate_tds_link(self, github_path: str) -> str:
        clean_path = github_path.replace('.md', '')
        return f"{self.tds_base_url}{clean_path}"
    
    def _generate_title(self, file_path: str) -> str:
        filename = Path(file_path).stem
        return filename.replace('-', ' ').replace('_', ' ').title()
    
    def _extract_section(self, file_path: str) -> str:
        parent = Path(file_path).parent
        if parent.name == ".":
            return "Core Content"
        return parent.name.replace('-', ' ').replace('_', ' ').title()
    
    def _save_collection_metadata(self):
        metadata = {
            "collection_info": {
                "repository": f"{self.owner}/{self.repo}",
                "branch": self.branch,
                "tds_base_url": self.tds_base_url,
                "collected_at": time.strftime('%Y-%m-%d %H:%M:%S'),
                "total_files": len(self.collected_files)
            },
            "files": self.collected_files
        }
        metadata_file = self.output_dir / "course_collection_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
