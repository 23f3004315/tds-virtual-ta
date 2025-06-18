---
chunk_id: discourse_topic_171141_post_71_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/71
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 114
username: Jivraj
post_number: 71
topic_id: 171141
---

## Post #71 by Jivraj

**Direct Link**: [Post #71](https://discourse.onlinedegree.iitm.ac.in/t/171141/71)

We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.

Line number 81 of your app.py

`subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)`

which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.
