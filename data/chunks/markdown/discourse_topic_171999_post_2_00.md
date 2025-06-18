---
chunk_id: discourse_topic_171999_post_2_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171999/2
source_title: Project 1 solution repository link
content_type: discourse
tokens: 202
username: carlton
post_number: 2
topic_id: 171999
---

## Post #2 by carlton

**Direct Link**: [Post #2](https://discourse.onlinedegree.iitm.ac.in/t/171999/2)

The repo has not been made public. But until that happens, we are allowed to share the solution.

Just name the script app.py, build the docker image according to test environment. This also happened to be the highest scoring script getting 19 tasks correct.

`# /// script
# requires-python = "&gt;=3.11"
# dependencies = [
# "fastapi",
# "httpx",
# "uvicorn",
# ]
# ///

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import httpx
import re
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

token = os.environ["LLMFOUNDRY_TOKEN"]
