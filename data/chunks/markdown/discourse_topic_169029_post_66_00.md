---
chunk_id: discourse_topic_169029_post_66_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/66
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 182
username: 23f2000573
post_number: 66
topic_id: 169029
---

## Post #66 by 23f2000573

**Direct Link**: [Post #66](https://discourse.onlinedegree.iitm.ac.in/t/169029/66)

Hi TAs,

I attended the meet which happened today. But I don’t clearly get one thing.

Most of the questions have a **question text** and a **file: csv,zip,json,etc**

My doubt is, will the request to the end point be :

`curl -X POST "https://your-app.vercel.app/api/" \
 -H "Content-Type: multipart/form-data" \
 -F "question=question text" \
 -F "file=https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;template=results;type=batting"
`
[Quote]: 
my doubt :

Is this the only format or can there be other too ?
