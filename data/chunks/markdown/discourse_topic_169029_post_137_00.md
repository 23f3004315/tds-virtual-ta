---
chunk_id: discourse_topic_169029_post_137_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/137
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 275
username: lakshaygarg654
post_number: 137
topic_id: 169029
---

## Post #137 by lakshaygarg654

**Direct Link**: [Post #137](https://discourse.onlinedegree.iitm.ac.in/t/169029/137)

lakshaygarg654:
[Quote]:

**GA4 - Question 9: Process PDF Files**

A similar issue occurs in GA4 Question 9, where the task involves processing PDF files. While this works perfectly in the local environment, it leads to a **502 Bad Gateway** error on Azure. This is due to the relatively long time required to parse and analyze the PDFs, which again exceeds Azure’s execution time limit.
Moreover, pre-processing the PDF files is not an option because the input varies for each user. Therefore, the PDFs must be processed dynamically, which adds to the delay and contributes to the timeout problem.

@carlton

I watched the last session. In that session, regarding the specific PDF question, you mentioned that the PDF is the same for everyone, so it can be preprocessed beforehand. However, I checked and found that the PDF is actually different for each user. So, we need to fetch it from the API endpoint.

How should we handle the timeout issue on the deployment platform? I even tried upgrading the plan, but it didn’t help.

@s.anand

@carlton @Jivraj
