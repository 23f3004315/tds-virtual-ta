---
chunk_id: discourse_topic_171141_post_434_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/434
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 192
username: carlton
post_number: 434
topic_id: 171141
---

## Post #434 by carlton

**Direct Link**: [Post #434](https://discourse.onlinedegree.iitm.ac.in/t/171141/434)

Your docker failed to build from your Dockerfile

` =&gt; ERROR [4/7] RUN uv --version 0.1s
------
 &gt; [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
 23 | 
 24 | # Verify uv installation
 25 | &gt;&gt;&gt; RUN uv --version
 26 | 
 27 | # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127
`
Since we cannot build your docker from your Docker manifest file we cannot evaluate it.
