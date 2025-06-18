---
chunk_id: discourse_topic_171141_post_395_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/395
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 213
username: carlton
post_number: 395
topic_id: 171141
---

## Post #395 by carlton

**Direct Link**: [Post #395](https://discourse.onlinedegree.iitm.ac.in/t/171141/395)

Did you follow these instructions when building the test environment? Our logs indicated that this was the problem:

tried copying multiple files for that you need to give directory name and it should end with a /

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
