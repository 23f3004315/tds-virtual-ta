---
chunk_id: discourse_topic_171141_post_350_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/350
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 303
username: Santoshsharma
post_number: 350
topic_id: 171141
---

 I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.

Previous Message for Reference

For your convenience, here is my earlier message explaining this issue in detail:

"Greetings, Sir,

---

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between pandas and numpy caused the container to fail. To my surprise, the same versions (pandas==2.0.3 and numpy==1.24.3) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (santoshsharma003/tds-project-one-1:latest). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!"
