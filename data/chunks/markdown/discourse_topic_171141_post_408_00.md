---
chunk_id: discourse_topic_171141_post_408_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/408
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 198
username: Jivraj
post_number: 408
topic_id: 171141
---

## Post #408 by Jivraj

**Direct Link**: [Post #408](https://discourse.onlinedegree.iitm.ac.in/t/171141/408)

Hi @22f3002723

/bin/sh: 1: uv: not found 
This is error that we got on your evaluation while building docker image through github repo.

Tds-official-Project1-discrepencies Tools in Data Science
 
 [Quote]: 
 To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can run this code using uv. 
# /// script
# dependencies = [
# "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo

owner = "your_username" # Replace with your actual GitHub …
