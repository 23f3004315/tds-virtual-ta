---
chunk_id: discourse_topic_164277_post_398_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/398
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 201
username: Nelson
post_number: 398
topic_id: 164277
---

## Post #398 by Nelson

**Direct Link**: [Post #398](https://discourse.onlinedegree.iitm.ac.in/t/164277/398)

Task A9 fails.

[Quote]: 
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings “HTTP/1.1 401 Unauthorized”

A9 failed: ‘data’

A9 FAILED

If I run

`curl -X POST http://aiproxy.sanand.workers.dev/openai/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AIPROXY_TOKEN" -d '{"model": "text-embedding-3-small", "input": ["king", "queen"]}'
`
I get

`{
 "message": "Missing Authorization: Bearer header. See https://github.com/sanand0/aiproxy"
}
`
@carlton @Jivraj @s.anand
