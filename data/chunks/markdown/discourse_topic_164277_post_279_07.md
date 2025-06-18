---
chunk_id: discourse_topic_164277_post_279_07
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/279
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 312
username: 23f1002382
post_number: 279
topic_id: 164277
---

.txt “HTTP/1.1 200 OK”

A7 PASSED

Running task: `/data/credit_card.png` contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to `/data/credit-card.txt`

---

HTTP Request: POST **[Discussion Image by 23f1002382]** External image (processing failed) - likely course-related content`+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+`%2Fdata%2Fcredit-card.txt` “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/credit-card.txt “HTTP/1.1 200 OK”

/data/credit-card.txt

EXPECTED:

30091429521159

RESULT:

3009142952159

A8 FAILED

HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings “HTTP/1.1 200 OK”

Running task: `/data/comments.txt` contains a list of comments, one per line. Using embeddings, find the most similar pair of comments and write them to `/data/comments-similar.txt`, one per line
