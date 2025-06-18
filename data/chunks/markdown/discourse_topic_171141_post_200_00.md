---
chunk_id: discourse_topic_171141_post_200_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/200
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 173
username: Jivraj
post_number: 200
topic_id: 171141
---

## Post #200 by Jivraj

**Direct Link**: [Post #200](https://discourse.onlinedegree.iitm.ac.in/t/171141/200)

Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.

`tags = httpx.get(
 f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
 ).json()
 tag, size = next(
 (
 (tag["name"], tag["full_size"])
 for tag in tags.get("results", [])
 if pd.Timestamp(tag["last_updated"]) &lt;= DEADLINE
 ),
 (None, 0),
 )

`
This is part of our script that does the validation check for docker repo.
