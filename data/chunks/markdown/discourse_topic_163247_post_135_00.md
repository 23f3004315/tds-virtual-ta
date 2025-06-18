---
chunk_id: discourse_topic_163247_post_135_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/135
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 226
username: Sakshi6479
post_number: 135
topic_id: 163247
---

## Post #135 by Sakshi6479

**Direct Link**: [Post #135](https://discourse.onlinedegree.iitm.ac.in/t/163247/135)

Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

Q7 &amp; Q8 in these questions the problem is the same my app couldn’t fetch the details from the file.

``from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Add CORSMiddleware with more restrictive settings
app.add_middleware(
 CORSMiddleware,
 allow_origins=["http://localhost:3000"], # Allow only this specific origin
 allow_credentials=True,
 allow_methods=["POST", "OPTIONS"], # Allow only POST and OPTIONS methods
 allow_headers=["Content-Type", "Authorization"], # Allow only specific headers
)
