---
chunk_id: discourse_topic_171141_post_454_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/454
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 276
username: carlton
post_number: 454
topic_id: 171141
---

## Post #454 by carlton

**Direct Link**: [Post #454](https://discourse.onlinedegree.iitm.ac.in/t/171141/454)

Hi Hilal,

You have to recreate the test environment as shown in this post

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

That way you will be able to identify why the error was occuring.

The specific error itself means:

Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.

If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.

Kind regards
