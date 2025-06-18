---
chunk_id: discourse_topic_164277_post_351_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/351
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 79
username: 23f2002205
post_number: 351
topic_id: 164277
---

## Post #351 by 23f2002205

**Direct Link**: [Post #351](https://discourse.onlinedegree.iitm.ac.in/t/164277/351)

i too got the same error you can change the the tools part in your payload to

`"tools": [{"type": "function", "function": schema} for schema in function_schema]
`
