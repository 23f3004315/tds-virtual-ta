---
chunk_id: discourse_topic_171141_post_110_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/110
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 423
username: 23f2004644
post_number: 110
topic_id: 171141
---

 data-base62-sha1="gwD7SZY75yucA5CeD6a6hXj3CuA" width="690" height="362" data-dominant-color="F5F5F5">image1456×765 41.6 KB

---

**[Discussion Image by 23f2004644]** This image shows a student encountering errors while running the TDS project, specifically in accessing a CSV file. The error message "unable to open database file" is followed by a "HTTP/1.1 404 NOT FOUND" error when trying to GET the file at the specified path `http://localhost:8000/read?path=/data/b10.csv`. This indicates that the server cannot find the requested file, and is further confirmed by the message "B10 failed: Cannot read /data/b10.csv". The student is getting a score of 12/20 on the project, and the student will likely need to review the file path and confirm that the `b10.csv` file is present in the `/data/` directory and correctly accessible to the server. There is also a successful POST request to an OpenAI embeddings endpoint, but this seems unrelated to the file access problem.message `"error": "unable to open database file"`. The HTTP request `GET http://localhost:8000/read?path=/data/b10.csv` results in a "404 NOT FOUND" error, meaning the file `b10.csv` could not be found at the specified path `/data/b10.csv`, which caused test case B10 to fail. Despite this error, a subsequent request to the OpenAI embeddings endpoint was successful. The student ultimately achieved a score of 12/20, reflecting the impact of the missing file." alt="image" data-base62-sha1="l8bjD57G9c5qcDceIuFC3WTZPyi" width="690" height="161" data-dominant-color="080A0F">image1094×256 9.59 KB
