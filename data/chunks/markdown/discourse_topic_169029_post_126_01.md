---
chunk_id: discourse_topic_169029_post_126_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/126
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 273
username: lakshaygarg654
post_number: 126
topic_id: 169029
---

 actually live—resulting in a broken or non-functional link on the assignment portal. On the other hand, including the delay function causes Azure to throw a **502 Bad Gateway** error, likely due to Azure’s request timeout limitations. The additional wait time slightly exceeds the platform’s allowed response duration.

---

**GA4 - Question 9: Process PDF Files**

A similar issue occurs in GA4 Question 9, where the task involves processing PDF files. While this works perfectly in the local environment, it leads to a **502 Bad Gateway** error on Azure. This is due to the relatively long time required to parse and analyze the PDFs, which again exceeds Azure’s execution time limit.

Moreover, pre-processing the PDF files is not an option because the input varies for each user. Therefore, the PDFs must be processed dynamically, which adds to the delay and contributes to the timeout problem.

Currently, I am using Azure for deployment, and for the majority of tasks, it works reliably. Although these specific tasks face timeout issues, shifting to another deployment platform is not feasible at this point. I am not certain if alternative platforms will work consistently across all questions, and making such a change could introduce failures in other parts of the assignment where Azure performs well.

Below Image is showing response of local machine api request for GA2 Q3 which works fine.
