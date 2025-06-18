---
chunk_id: discourse_topic_164277_post_279_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/279
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 353
username: 23f1002382
post_number: 279
topic_id: 164277
---

last_name`%2C+then+`first_name`%2C+and+write+the+result+to+`%2Fdata%2Fcontacts-sorted.json` “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

---

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/contacts-sorted.json “HTTP/1.1 200 OK”

A4 PASSED

Running task: Write the first line of the 10 most recent `.log` file in `/data/logs/` to `/data/logs-recent.txt`, most recent first

HTTP Request: POST http://localhost:8000/run?task=Write+the+first+line+of+the+10+most+recent+`.log`+file+in+`%2Fdata%2Flogs%2F`+to+`%2Fdata%2Flogs-recent.txt`%2C+most+recent+first “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/logs-recent.txt “HTTP/1.1 200 OK”

A5 PASSED

Running task: Find all Markdown (`.md`) files in `/data/docs/`.

For each file, extract the first occurrance of each H1 (i.e. a line starting with `# `).

Create an index file `/data/docs/index.json` that maps each filename (without the `/data/docs/` prefix) to its title
