---
chunk_id: discourse_topic_161120_post_14_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/14
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 96
username: Jivraj
post_number: 14
topic_id: 161120
---

## Post #14 by Jivraj

**Direct Link**: [Post #14](https://discourse.onlinedegree.iitm.ac.in/t/161120/14)

Hi Mishkat,

This error is because you are filtering on `class_` instead of `class`

So if you send a request on `http://127.0.0.1/api?class_=1S` you will see response for that `1S` class only.

kind regards
