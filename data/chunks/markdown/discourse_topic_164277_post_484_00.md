---
chunk_id: discourse_topic_164277_post_484_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/484
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 158
username: abhigyandsa
post_number: 484
topic_id: 164277
---

## Post #484 by abhigyandsa

**Direct Link**: [Post #484](https://discourse.onlinedegree.iitm.ac.in/t/164277/484)

On my system evaulate.py is throwing an error on A2 trying to execute npx on format.md before the llm is even invoked. However running the command directly on the command line works.

evaluate.py:

A2 failed: Command ‘[‘npx’, ‘prettier@3.4.2’, ‘–stdin-filepath’, ‘data/format.md’]’ returned non-zero exit status 2.

A2 FAILED

bash:

npx prettier@3.4.2 --stdin-filepath data/format.md

bash works as expected. Can someone help?
