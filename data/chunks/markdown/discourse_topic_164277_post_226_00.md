---
chunk_id: discourse_topic_164277_post_226_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/226
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 293
username: Adithya
post_number: 226
topic_id: 164277
---

## Post #226 by Adithya

**Direct Link**: [Post #226](https://discourse.onlinedegree.iitm.ac.in/t/164277/226)

I am also facing the same issue.

Evaluation Output:

`HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

❌ A9 FAILED
`
I sense ‘Authentication Problem’ happens only with the evaluation script, as the curl requests seems to work fine.

`INFO:httpx:HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
INFO: 127.0.0.1:60849 - "POST /run?task=%60%2Fdata%2Fcomments.txt%20contains%20a%20list%20of%20comments,%20one%20per%20line.%20Using%20embeddings,%20find%20the%20most%20similar%20pair%20of%20comments%20and%20write%20them%20to%20%2Fdata%2Fcomments-similar.txt,%20one%20per%20line HTTP/1.1" 200 OK
`
Any views? @carlton @Jivraj
