---
chunk_id: discourse_topic_161120_post_46_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/46
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 184
username: carlton
post_number: 46
topic_id: 161120
---

## Post #46 by carlton

**Direct Link**: [Post #46](https://discourse.onlinedegree.iitm.ac.in/t/161120/46)

@23f2003751

While I understand why you might choose to use `flask` due to your familiarity with it,

the `http.server` library is just very simple to use.

The **only extra line of code** you would need inside your `get` request if you used the `http.server` library would be:

`self.send_header("Access-Control-Allow-Origin", "*")`

Try to rewrite your code using `http.server` library so that your debugging for simple tasks like this is easy.

The boilerplate code for a `get` request using the `http.server` library was already given in Q6. So you have to do very minimal modifications to it and it works like a charm.

Kind regards
