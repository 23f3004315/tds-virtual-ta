---
chunk_id: discourse_topic_171141_post_353_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/353
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 282
username: carlton
post_number: 353
topic_id: 171141
---

## Post #353 by carlton

**Direct Link**: [Post #353](https://discourse.onlinedegree.iitm.ac.in/t/171141/353)

There are no evaluation logs for you, I am not sure which evaluation log you are referring to. Your docker image fails to run the required task because your Dockerfile is misconfigured. Did you follow the test environment setup mentioned in this post before posting your query?

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

Because if you did, you will realise why your evaluation failed.

You must replicate the test environment and then if you submission works, you have a legitimate appeal. Otherwise we will not consider it. Please replicate the issue using the test environment as detailed in the post link.

Kind regards
