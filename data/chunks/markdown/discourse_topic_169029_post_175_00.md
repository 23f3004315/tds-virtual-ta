---
chunk_id: discourse_topic_169029_post_175_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/175
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 91
username: 23ds3000149
post_number: 175
topic_id: 169029
---

## Post #175 by 23ds3000149

**Direct Link**: [Post #175](https://discourse.onlinedegree.iitm.ac.in/t/169029/175)

Hello @22f3001307, there is an error in the code that needs to be fixed as part of the question:

image = Image.open(list(files.upload().keys)[0]

with

image = Image.open(list(files.upload().keys())[0])
