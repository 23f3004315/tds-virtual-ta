---
chunk_id: discourse_topic_171141_post_350_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/350
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 310
username: Santoshsharma
post_number: 350
topic_id: 171141
---

.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.

---

However, during your evaluation, this incompatibility caused the container to fail.

I acknowledge this issue, have fixed it in my updated submission, and previously conveyed this in my earlier message.

Action Taken

To address this issue, I made a small adjustment to my requirements.txt file to explicitly fix these versions for compatibility across all environments. This was the only change made to my submission. After rebuilding the container with this updated file, I tested it again thoroughly in your replicated test environment, and it worked as expected:

The application initializes correctly on port 8000 within 5 minutes.

It responds to requests within the required timeframe.

I have pushed this updated image to Docker Hub under the same repository:

Docker Hub URL: santoshsharma003/tds-project-one-1:latest

Request for Re-Evaluation

I kindly request that you pull the latest version of my Docker image from Docker Hub and re-run the evaluation process. I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.

Previous Message for Reference

For your convenience, here is my earlier message explaining this issue in detail:

"Greetings, Sir,
