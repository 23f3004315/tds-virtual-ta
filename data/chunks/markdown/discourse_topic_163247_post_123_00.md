---
chunk_id: discourse_topic_163247_post_123_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/123
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 243
username: Sudhishnarayan
post_number: 123
topic_id: 163247
---

## Post #123 by Sudhishnarayan

**Direct Link**: [Post #123](https://discourse.onlinedegree.iitm.ac.in/t/163247/123)

This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You

`from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], # Allows all origins
 allow_credentials=True,
 allow_methods=["OPTIONS", "POST"], # Allows all methods (GET, POST, OPTIONS, etc.)
 allow_headers=["*"], # Allows all headers
)
