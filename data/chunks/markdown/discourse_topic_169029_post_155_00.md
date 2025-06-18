---
chunk_id: discourse_topic_169029_post_155_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/155
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 296
username: Algsoch
post_number: 155
topic_id: 169029
---

## Post #155 by Algsoch

**Direct Link**: [Post #155](https://discourse.onlinedegree.iitm.ac.in/t/169029/155)

Hello Sir,

I want to express my gratitude for the opportunity to work on this project. I have developed a mini chatbot backend using `vicky_server.py`, which handles question matching and execution internally, producing appropriate responses. `My mini chatbot is capable of creating its own API using REST and can manage tasks such as image compression, repository management, workflows, and web scraping related to graded assignments. It can even calculate total marks for subjects like physics and convert PDFs into markdown content. Additionally, it is capable of downloading the Llama model and creating a tunnel using ngrok. Essentially, it can address the first four assignment questions.`

However, there are some limitations to this project. Currently, it processes my local files instead of the uploaded PDFs. I am working on resolving this issue, but I have some confusion regarding the internal handling of uploaded files. When I pass a PDF or file through an upload method, how should the system proceed? I want to ensure that the file is treated as a PDF for the user rather than just being referenced as “question.pdf.” How can I effectively manage this problem?

Furthermore, there is an issue with question matching. At times, the system incorrectly identifies questions containing the word “code” and executes `first.py` for GA1.
