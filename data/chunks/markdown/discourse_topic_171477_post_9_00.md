---
chunk_id: discourse_topic_171477_post_9_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171477/9
source_title: Project 1 Evaluation second mail is not correct and reports files missing while they are present
content_type: discourse
tokens: 233
username: carlton
post_number: 9
topic_id: 171477
---

## Post #9 by carlton

**Direct Link**: [Post #9](https://discourse.onlinedegree.iitm.ac.in/t/171477/9)

Your Dockerfile was misconfigured. When we try to build the docker image from your github repo, we get this error:

`tried copying parent folder(COPY failed: forbidden path outside the build context: .. ())`

You have to replicate the test environment. If it works when you follow this test setup then you should get in touch with us.

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
import argparse
import os
import zipfile

parser = argparse.…
