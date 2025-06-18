---
chunk_id: discourse_topic_169029_post_189_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/189
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 130
username: Saransh_Saini
post_number: 189
topic_id: 169029
---

## Post #189 by Saransh_Saini

**Direct Link**: [Post #189](https://discourse.onlinedegree.iitm.ac.in/t/169029/189)

Its unusual to have a docker container worth 7 GBs of space. Here is what you can do

Remove unused libraries from your `requirements.txt`. Sometimes having resource demanding libraries like `SentenceTransformers` can install large sub-dependency packages.
Exclude your virtual environment folder from the container creation
Create a `.containerignore` file to have an exception for those folders you want to skip.
Clear your package cache and any vscode cache you might have.
