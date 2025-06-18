---
chunk_id: discourse_topic_171141_post_316_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/316
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 277
username: carlton
post_number: 316
topic_id: 171141
---

## Post #316 by carlton

**Direct Link**: [Post #316](https://discourse.onlinedegree.iitm.ac.in/t/171141/316)

To replicate the test environment:

Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can run this code using uv.

`# /// script
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

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
 "--owner",
 type=str,
 required=True,
 help="GitHub username."
)
parser.add_argument (
 "--repo",
 type=str,
 required=True,
 help="GitHub repository name."
)
parser.add_argument (
 "--save",
 type=str,
 default="../github/",
 help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
 "--extract",
 type=str,
 default="../github/",
 help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract
