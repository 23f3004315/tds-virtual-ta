---
chunk_id: discourse_topic_171141_post_366_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/366
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 86
username: Jivraj
post_number: 366
topic_id: 171141
---

## Post #366 by Jivraj

**Direct Link**: [Post #366](https://discourse.onlinedegree.iitm.ac.in/t/171141/366)

This is error that you got while building docker image using docker file in your github repo tried copying requirements.txt which doesn’t exists

In your Dockerfile you are trying to copy requirements.txt but it doesn’t exists in the directory where Dockerfile is located
