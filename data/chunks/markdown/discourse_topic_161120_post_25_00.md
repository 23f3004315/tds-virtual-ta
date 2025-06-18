---
chunk_id: discourse_topic_161120_post_25_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/25
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 105
username: carlton
post_number: 25
topic_id: 161120
---

## Post #25 by carlton

**Direct Link**: [Post #25](https://discourse.onlinedegree.iitm.ac.in/t/161120/25)

Hi Mishkat,

The GA url encoded parameter is `class`

In your screenshot, you are using `class_`

Your code that we examined earlier also accepts `class_` as the parameter instead of `class` as required by the GA

The GA will test your deployment by sending it a request with the url encoded parameter `class`
