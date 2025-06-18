---
chunk_id: discourse_topic_171141_post_94_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/94
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 89
username: Jivraj
post_number: 94
topic_id: 171141
---

## Post #94 by Jivraj

**Direct Link**: [Post #94](https://discourse.onlinedegree.iitm.ac.in/t/171141/94)

That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.

Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.
