---
chunk_id: discourse_topic_164277_post_196_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/196
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 122
username: Jivraj
post_number: 196
topic_id: 164277
---

## Post #196 by Jivraj

**Direct Link**: [Post #196](https://discourse.onlinedegree.iitm.ac.in/t/164277/196)

After submitting docker image through, it will be pulled and our token will be used.

Things to be checked at your end.

1.` podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME` works fine

2. Above command will start 8000 server so use evaluate.py to test if things are working as expected.

Kind regards.

Jivraj
