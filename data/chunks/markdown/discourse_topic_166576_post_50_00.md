---
chunk_id: discourse_topic_166576_post_50_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/50
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 109
username: carlton
post_number: 50
topic_id: 166576
---

## Post #50 by carlton

**Direct Link**: [Post #50](https://discourse.onlinedegree.iitm.ac.in/t/166576/50)

@daksh76 thats because your innermost logic layer must not return a long list of results.

If you think about it logically each row cannot have a column field where one of the columns is a whole row of results right?

Thats why you are getting the error.

Check your innermost layer is returning a single value or a row of results.

Kind regards
