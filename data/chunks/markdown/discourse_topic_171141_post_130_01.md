---
chunk_id: discourse_topic_171141_post_130_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/130
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 232
username: 23ds2000092
post_number: 130
topic_id: 171141
---

: 172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

`
Similarly for task B2.

---

`INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO: 172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK
`
For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.

For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?

Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8
