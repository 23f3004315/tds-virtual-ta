---
chunk_id: discourse_topic_166357_post_1_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166357/1
source_title: Doubts in Q7, Q8
content_type: discourse
tokens: 357
username: Sakshi6479
post_number: 1
topic_id: 166357
---

 the request. This means the student needs to include the ticket number itself in the query to get the status. 2x" data-dominant-color="1C1E1B">Screenshot 2025-02-05 1827501917×1018 38.3 KB

---

`import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import util
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], # Allow all origins
 allow_credentials=True,
 allow_methods=["OPTIONS", "POST"], # Allow OPTIONS and POST
 allow_headers=["*"], # Allow all headers
)

# Pydantic model to parse incoming data
class SimilarityRequest(BaseModel):
 docs: List[str]
 query: str

# OpenAI API key and URL
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
API_KEY = "enter your key" # Replace with your actual API key

def get_embeddings(docs: List[str]) -&gt; List[List[float]]:
 """Retrieve embeddings for a list of documents from OpenAI's API."""
 headers = {
 "Content-Type": "application/json",
 "Authorization": f"Bearer {API_KEY}",
 }
 
 data = {
 "model": "text-embedding-3-small", # Use the correct model
 "input": docs
 }

response = requests.post(API_URL, json=data, headers=headers)

if response.status_code != 200:
 raise HTTPException(status_code=response.status_code, detail="API request failed")
