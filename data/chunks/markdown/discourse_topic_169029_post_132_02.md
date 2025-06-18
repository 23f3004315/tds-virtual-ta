---
chunk_id: discourse_topic_169029_post_132_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/132
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 352
username: adi3
post_number: 132
topic_id: 169029
---

 serves as a clear problem statement and data schema for the student project. 2x" data-dominant-color="2B2E33">WhatsApp Image 2025-03-27 at 13.41.43_5bd0a1821600×1069 246 KB

---

Dear Sirs,

I have a question regarding Q3 and Q4 of GA5. When calling the API, should we pass the `.gz` file directly, or will the API accept a Google Drive link from which it can download the `.gz` file?

Specifically, will the API call be structured as follows?

Essentialy, will the API call look like so?

[Quote]: 
curl -X POST “http://127.0.0.1:5000”

-H “Content-Type: multipart/form-data”

-F "question=Bandwidth Analysis for Regional Contents - anand.net is a personal website that had region-specific music content. One of the site’s key sections is tamilmp3, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement. By analyzing the server’s Apache log file, the author can identify heavy users and take measures to manage bandwidth, improve site performance, or even investigate potential abuse. Your Task: This GZipped Apache log file has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024. Each row has these fields:

IP: The IP address of the visitor.

Remote logname: The remote logname of the visitor. Typically ‘-’.
