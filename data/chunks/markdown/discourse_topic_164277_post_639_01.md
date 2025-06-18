---
chunk_id: discourse_topic_164277_post_639_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/639
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 143
username: carlton
post_number: 639
topic_id: 164277
---

‘json_object’, ‘json_schema’, and ‘text’

Since you are defining a schema the correct value should be ‘json_schema’

So therefore you should change

`"type": "json"
`
to

`"type": "json_schema"
`
If you have trouble constructing Json schemas,

---

either feed it to gpt and have it correct it (along with your error) or please go over Module 3, in particular

https://tds.s-anand.net/#/llm-text-extraction

There is a clear example you can use as a template. We use the same one as a template when we do it in the sessions. That way you will make less errors.

Kind regards
