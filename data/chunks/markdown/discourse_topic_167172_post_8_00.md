---
chunk_id: discourse_topic_167172_post_8_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/8
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 260
username: Sakshi6479
post_number: 8
topic_id: 167172
---

## Post #8 by Sakshi6479

**Direct Link**: [Post #8](https://discourse.onlinedegree.iitm.ac.in/t/167172/8)

sir i have tried that by putting by doing this

`import os
from dotenv import load_dotenv
import json
import requests
from dateutil import parser as date_parser
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3
import base64
import mimetypes
import numpy as np

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["GET", "POST"],
 allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
def cakebake(no_people: int, flavor: str):
 return {"message": f"Making a {flavor} cake for {no_people} people"}
