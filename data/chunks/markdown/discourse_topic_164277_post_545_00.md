---
chunk_id: discourse_topic_164277_post_545_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/545
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 247
username: 23f1002382
post_number: 545
topic_id: 164277
---

## Post #545 by 23f1002382

**Direct Link**: [Post #545](https://discourse.onlinedegree.iitm.ac.in/t/164277/545)

Nice bro, if its getting 8 you are sorted, probably get more later. But Prompting seems a little less info

BUT

Structured Outputs
JSON Mode

Outputs valid JSON
Yes
Yes

Adheres to schema
Yes (see supported schemas)
No

Compatible models
gpt-4o-mini, gpt-4o-2024-08-06, and later
gpt-3.5-turbo, gpt-4-* and gpt-4o-* models

Enabling
response_format: { type: json_schema, json_schema: {strict: true, schema: …} }
response_format: { type: json_object }

` try:
 response = client.chat.completions.create(
 model="gpt-4o-mini",
 messages=[{"role": "user", "content": prompt}],
 temperature=0,
 response_format={"type": "json_object"}
 )
`

github.com/23f2005593/tds

app.py

`main`
