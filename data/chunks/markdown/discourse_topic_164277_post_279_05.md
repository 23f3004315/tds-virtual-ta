---
chunk_id: discourse_topic_164277_post_279_05
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/279
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 349
username: 23f1002382
post_number: 279
topic_id: 164277
---

 files in `/data/docs/`.

For each file, extract the first occurrance of each H1 (i.e. a line starting with `# `).

Create an index file `/data/docs/index.json` that maps each filename (without the `/data/docs/` prefix) to its title

---

(e.g. `{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}`)

HTTP Request: POST http://localhost:8000/run?task=Find+all+Markdown+(`.md`)+files+in+`%2Fdata%2Fdocs%2F`.
For+each+file%2C+extract+the+first+occurrance+of+each+H1+(i.e.+a+line+starting+with+`%23+`).
Create+an+index+file+`%2Fdata%2Fdocs%2Findex.json`+that+maps+each+filename+(without+the+`%2Fdata%2Fdocs%2F`+prefix)+to+its+title
(e.g.+`{“README.md”%3A+“Home”%2C+“path%2Fto%2Flarge-language-models.md”%3A+“Large+Language+Models”%2C+...}`) “HTTP/1.1 200 OK”

HTTP 200 {

“status”: “success”,

“message”: “Task executed successfully”

}

HTTP Request: GET http://localhost:8000/read?path=/data/docs/index.json “HTTP/1.1 200 OK”

A6 PASSED
