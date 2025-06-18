---
chunk_id: discourse_topic_161120_post_29_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/29
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 111
username: carlton
post_number: 29
topic_id: 161120
---

## Post #29 by carlton

**Direct Link**: [Post #29](https://discourse.onlinedegree.iitm.ac.in/t/161120/29)

Hi Mishkat,

In your code, the word `class` is a reserved keyword in python. So simply changing `class_` to `class` is not going to work. The *only* thing you need to change is the keyword accepted by the api *not* the variable name used inside your function. Hope that helps you narrow down the problem.

Kind regards
