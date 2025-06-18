---
chunk_id: discourse_topic_164277_post_223_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/223
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 277
username: 22f3002771
post_number: 223
topic_id: 164277
---

## Post #223 by 22f3002771

**Direct Link**: [Post #223](https://discourse.onlinedegree.iitm.ac.in/t/164277/223)

i am getting unauthorized error in A9 again and again, i have pasted my code if someone can help please look into this.

`# /// script
# requires-python = "&gt;=3.11"
# dependencies = [
# "numpy",
# "httpx",
# "fastapi",
# ]
# ///

import httpx
import numpy as np
import datetime
import os

from fastapi import HTTPException

now = datetime.datetime.now()

OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"

# async def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -&gt; float:
def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -&gt; float:
 # """Calculate cosine similarity between two texts."""
 # emb1 = await embed(text1)
 # emb2 = await embed(text2)
 return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))
