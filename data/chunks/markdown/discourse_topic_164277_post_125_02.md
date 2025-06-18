---
chunk_id: discourse_topic_164277_post_125_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/125
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 152
username: 23f1002382
post_number: 125
topic_id: 164277
---

F1hzxksDi54nBGls5d6m6F2hyu" width="643" height="499" data-dominant-color="F3F3F3">Screenshot 2025-02-11 232608919×714 22.4 KB

---

correct code in step 2 collection query step

`response = ollama.embed(
 model="nomic-embed-text:latest",
 input=task
)
results = collection.query(
 query_embeddings=response["embeddings"], #here embeddings and also not list of list as response embeddings already gives correct format
 n_results=1
)
data = results['documents'][0][0]
`
@s.anand @Jivraj @carlton
