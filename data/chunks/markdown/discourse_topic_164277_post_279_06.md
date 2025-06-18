---
chunk_id: discourse_topic_164277_post_279_06
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/279
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 307
username: 23f1002382
post_number: 279
topic_id: 164277
---

/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/docs/index.json “HTTP/1.1 200 OK”

A6 PASSED

---

Running task: `/data/email.txt` contains an email message. Pass the content to an LLM with instructions to extract the sender’s email address, and write just the email address to `/data/email-sender.txt`

HTTP Request: POST http://localhost:8000/run?task=`%2Fdata%2Femail.txt`+contains+an+email+message.+Pass+the+content+to+an+LLM+with+instructions+to+extract+the+sender’s+email+address%2C+and+write+just+the+email+address+to+`%2Fdata%2Femail-sender.txt` “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/email-sender.txt “HTTP/1.1 200 OK”

A7 PASSED

Running task: `/data/credit_card.png` contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to `/data/credit-card.txt`
