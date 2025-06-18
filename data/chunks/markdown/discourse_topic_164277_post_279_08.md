---
chunk_id: discourse_topic_164277_post_279_08
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/279
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 293
username: 23f1002382
post_number: 279
topic_id: 164277
---

ers.dev/openai/v1/embeddings “HTTP/1.1 200 OK”

Running task: `/data/comments.txt` contains a list of comments, one per line. Using embeddings, find the most similar pair of comments and write them to `/data/comments-similar.txt`, one per line

---

HTTP Request: POST http://localhost:8000/run?task=`%2Fdata%2Fcomments.txt`+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair+of+comments+and+write+them+to+`%2Fdata%2Fcomments-similar.txt`%2C+one+per+line “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/comments-similar.txt “HTTP/1.1 200 OK”

A9 PASSED

Running task: The SQLite database file `/data/ticket-sales.db` has a `tickets` with columns `type`, `units`, and `price`. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the “Gold” ticket type? Write the number in `/data/ticket-sales-gold.txt`
