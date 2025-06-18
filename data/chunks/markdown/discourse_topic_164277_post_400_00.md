---
chunk_id: discourse_topic_164277_post_400_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/400
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 130
username: 22f3002248
post_number: 400
topic_id: 164277
---

## Post #400 by 22f3002248

**Direct Link**: [Post #400](https://discourse.onlinedegree.iitm.ac.in/t/164277/400)

you have to give the `AIPROXY_TOKEN` to the evaluate.py by either

bash - `export AIPROXY_TOKEN="your token"`

or

powershell - `$env:AIPROXY_TOKEN="your token"`

the evaluate.py file takes the token to send request to embedding end point for processing.

so you have to set `AIPROXY_TOKEN` in both terminals

i.e. app.py and evaluate.py teminals
