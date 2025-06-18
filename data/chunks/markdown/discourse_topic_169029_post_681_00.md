---
chunk_id: discourse_topic_169029_post_681_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/681
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 207
username: 23ds3000090
post_number: 681
topic_id: 169029
---

## Post #681 by 23ds3000090

**Direct Link**: [Post #681](https://discourse.onlinedegree.iitm.ac.in/t/169029/681)

@carlton @Jivraj I appreciate the team incorporating my updated response at the endpoint with the “/api” path and re-evaluating accordingly, as well as sharing the results via email.

To my surprise, when I invoke the same endpoint that was evaluated — using the correct multipart/form-data payload with both question and file fields — I consistently receive a 200 OK response with the expected output.

Moreover, if I omit either field from the form-data, the server returns the exact validation error mentioned in the re-evaluation report, which makes sense. Based on this behavior and the details in the shared report, I’d like to confirm: during the re-evaluation, was the request payload indeed sent with both question and file fields included in the form-data?

For reference, I’ve attached a screenshot demonstrating the response.
