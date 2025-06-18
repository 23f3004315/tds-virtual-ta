---
chunk_id: discourse_topic_164277_post_36_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/36
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 256
username: 23f1002382
post_number: 36
topic_id: 164277
---

## Post #36 by 23f1002382

**Direct Link**: [Post #36](https://discourse.onlinedegree.iitm.ac.in/t/164277/36)

evaluate.py

TDS course repo

github.com

tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·...

Contribute to sanand0/tools-in-data-science-public development by creating an account on GitHub.

line 20

`from datagen import (
 get_markdown,
 get_dates,
 get_contacts,
 get_logs,
 get_docs,
 get_email,
 get_credit_card,
 get_comments,
 get_tickets,
)
`
but we get datagen.py only in a1 task

line 69

`async def a1(email: str, **kwargs):
 await run(
 f"""
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`
with `{email}` as the only argument
"""
 )
 return email in await read("/data/format.md")
`
The issue is **importing `datagen` before ensuring it exists**

just checking

@carlton @Jivraj
