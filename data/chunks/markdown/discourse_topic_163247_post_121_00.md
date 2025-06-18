---
chunk_id: discourse_topic_163247_post_121_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/121
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 192
username: Aditya_Sahu
post_number: 121
topic_id: 163247
---

## Post #121 by Aditya_Sahu

**Direct Link**: [Post #121](https://discourse.onlinedegree.iitm.ac.in/t/163247/121)

The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to http://aiproxy.sanand.workers.dev/openai/v1/embeddings with required headers. And, then calculate `similarity_scores` simply using

\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}

which in python syntax is-

`np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
`
