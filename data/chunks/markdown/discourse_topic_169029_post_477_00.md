---
chunk_id: discourse_topic_169029_post_477_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/477
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 173
username: 22f3000819
post_number: 477
topic_id: 169029
---

## Post #477 by 22f3000819

**Direct Link**: [Post #477](https://discourse.onlinedegree.iitm.ac.in/t/169029/477)

@carlton @Jivraj @Saransh_Saini

I just got the mail stating that my evaluation is complete and I can turn off my server.

However the Cloud Run logs show that all POST requests were made to the wrong end point.

The exact url I gave ends with “/api/” but every POST request was either made to “/api” which resulted in a 307 response or with “http” instead of “https” which resulted in a 302 response. Only the get requests were made to the correct endpoint but since the app was supposed to allow POST requests only, making GET requests just resulted in 405.
