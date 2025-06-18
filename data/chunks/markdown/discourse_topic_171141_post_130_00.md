---
chunk_id: discourse_topic_171141_post_130_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/130
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 263
username: 23ds2000092
post_number: 130
topic_id: 171141
---

## Post #130 by 23ds2000092

**Direct Link**: [Post #130](https://discourse.onlinedegree.iitm.ac.in/t/171141/130)

Hi,

For Tasks A8, A9 &amp; A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.

For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK

`ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO: 172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

`
Similarly for task B2.
