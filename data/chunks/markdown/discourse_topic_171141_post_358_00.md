---
chunk_id: discourse_topic_171141_post_358_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/358
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 258
username: carlton
post_number: 358
topic_id: 171141
---

## Post #358 by carlton

**Direct Link**: [Post #358](https://discourse.onlinedegree.iitm.ac.in/t/171141/358)

Hi Hari,

Your docker failed to build.

Did you try to replicate the test environment as mentioned in

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

If you tried you would find that it will not build. Thats why you have no logs.

90 such cases are there where the image could not be built from your repo.

The specific error in your case is:

tried copying requirements.txt which doesn’t exists

Thats why there are no logs.

Kind regards
