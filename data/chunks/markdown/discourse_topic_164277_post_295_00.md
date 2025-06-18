---
chunk_id: discourse_topic_164277_post_295_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/295
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 111
username: 23f2005419
post_number: 295
topic_id: 164277
---

## Post #295 by 23f2005419

**Direct Link**: [Post #295](https://discourse.onlinedegree.iitm.ac.in/t/164277/295)

`def format_with_prettier(file_path:str, prettier_version:str):
 if file_path and os.path.exists(file_path):
 print('Path exisit - will perform prettier')
 subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])
 else:
 raise FileNotFoundError()
`
This is my code
