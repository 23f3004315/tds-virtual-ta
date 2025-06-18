---
chunk_id: discourse_topic_171141_post_384_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/384
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 210
username: Jivraj
post_number: 384
topic_id: 171141
---

## Post #384 by Jivraj

**Direct Link**: [Post #384](https://discourse.onlinedegree.iitm.ac.in/t/171141/384)

Your docker image and github repo are not consistent.

While running docker image we got following error: `flask module missing`

For regenerating this error follow steps mentioned in below post.

Tds-official-Project1-discrepencies Tools in Data Science
 
 [Quote]: 
 To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
 response = requests.get(url,headers=github_headers, timeout=60)
 fetch_commit = None
 if response.status_code == 200:
 commits = response.json()
 for commit in commits:
 sha = commit["sha"]
 …
