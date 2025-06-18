---
chunk_id: discourse_topic_161120_post_131_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/131
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 246
username: carlton
post_number: 131
topic_id: 161120
---

## Post #131 by carlton

**Direct Link**: [Post #131](https://discourse.onlinedegree.iitm.ac.in/t/161120/131)

Hi Srividya,

Thats right the idea behind vercel is you do not need to create a server. Its serverless! Instead you create functions that respond to endpoints.

When the endpoint is triggered, the appropriate function runs.

This renders `name == main` part of the code unnecessary at best, since python interpreters only run this line if that file was the starting point of the application (but its not, because a vercel wrapper application(s) or processes have started before it).

In other words you do not create a flask server, or a http server or indeed any server at all. Just functions tied to specific endpoints. So you have to rethink how your application is designed. You *do not* create serverless applications in the same traditional way you have been taught in MAD-1 or MAD-2.

This is a common mistake many students have been making with their approach to vercel. Watching the videos and using the provided code template will greatly help in deploying successful serverless applications.

Thanks for your input.

Kind regards
