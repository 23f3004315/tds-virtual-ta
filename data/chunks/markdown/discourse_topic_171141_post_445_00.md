---
chunk_id: discourse_topic_171141_post_445_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/445
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 102
username: Jivraj
post_number: 445
topic_id: 171141
---

## Post #445 by Jivraj

**Direct Link**: [Post #445](https://discourse.onlinedegree.iitm.ac.in/t/171141/445)

23F300327:
[Quote]: 
To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

That destroys the purpose of containerization, your container should run anywhere anytime, all the dependencies must be preinstalled.
