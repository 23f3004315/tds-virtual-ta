---
chunk_id: discourse_topic_164277_post_279_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/279
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 363
username: 23f1002382
post_number: 279
topic_id: 164277
---

1.1 200 OK”

A2 PASSED

Running task: The file `/data/dates.txt` contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to `/data/dates-wednesdays.txt`

---

HTTP Request: POST http://localhost:8000/run?task=The+file+`%2Fdata%2Fdates.txt`+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+`%2Fdata%2Fdates-wednesdays.txt` “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/dates-wednesdays.txt “HTTP/1.1 200 OK”

A3 PASSED

Running task: Sort the array of contacts in `/data/contacts.json` by `last_name`, then `first_name`, and write the result to `/data/contacts-sorted.json`

HTTP Request: POST http://localhost:8000/run?task=Sort+the+array+of+contacts+in+`%2Fdata%2Fcontacts.json`+by+`last_name`%2C+then+`first_name`%2C+and+write+the+result+to+`%2Fdata%2Fcontacts-sorted.json` “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,
