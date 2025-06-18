---
chunk_id: discourse_topic_167172_post_1_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/1
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 265
username: Sakshi6479
post_number: 1
topic_id: 167172
---

## Post #1 by Sakshi6479

**Direct Link**: [Post #1](https://discourse.onlinedegree.iitm.ac.in/t/167172/1)

sir i am getting an error in this function calling which you have demonstrate yesterday , i am attaching my code also the error with it. Please take a look and provide the solution as the deadline is close please help me as soon as possible.

is there anything to do with dockerfile or anything else please explain it how to do it step by step.

`import os
from dotenv import load_dotenv
import json
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["GET", "POST"],
 allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
load_dotenv()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "enter your token here")
