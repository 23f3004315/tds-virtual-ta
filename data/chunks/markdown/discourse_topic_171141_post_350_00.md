---
chunk_id: discourse_topic_171141_post_350_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/350
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 291
username: Santoshsharma
post_number: 350
topic_id: 171141
---

## Post #350 by Santoshsharma

**Direct Link**: [Post #350](https://discourse.onlinedegree.iitm.ac.in/t/171141/350)

Respected Sir,

Thank you for your response and for providing the steps to replicate the test environment.

Steps Taken to Replicate the Test Environment

I cloned my repository using:

`bash
git clone &lt;my_repo_url&gt;
cd &lt;my_repo_directory&gt;
I built the Docker image using:

bash
docker build -t.
I ran the Docker container with:

bash
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000

I ensured that datagen.py and evaluate.py were placed in the same folder as instructed.

Finally, I ran the evaluation script using:

bash
uvicorn evaluate.py --email=&lt;any_email&gt; --token_counter 1 --external_port 8000
`
Issue with Original Submission

After reviewing the evaluation logs, I identified that the issue with my original submission was caused by binary incompatibility between pandas (version 2.0.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.
