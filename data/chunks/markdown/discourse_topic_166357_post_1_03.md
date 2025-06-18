---
chunk_id: discourse_topic_166357_post_1_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166357/1
source_title: Doubts in Q7, Q8
content_type: discourse
tokens: 346
username: Sakshi6479
post_number: 1
topic_id: 166357
---

 {
 "model": "text-embedding-3-small", # Use the correct model
 "input": docs
 }

response = requests.post(API_URL, json=data, headers=headers)

if response.status_code != 200:
 raise HTTPException(status_code=response.status_code, detail="API request failed")

---

response_data = response.json()
 if 'data' not in response_data:
 raise KeyError("Missing 'data' field in API response")

return [embedding['embedding'] for embedding in response_data['data']]

@app.post("/similarity")
async def similarity(request: SimilarityRequest):
 # Get embeddings for docs and query
 docs = request.docs
 query = request.query

# Get embeddings for the documents and query
 all_docs = docs + [query] # Combine documents and query into one list
 embeddings = get_embeddings(all_docs) # Get embeddings from OpenAI API

doc_embeddings = embeddings[:-1] # All embeddings except for the query
 query_embedding = embeddings[-1] # The last embedding is for the query

# Calculate cosine similarities
 similarities = util.cos_sim(query_embedding, doc_embeddings)[0].cpu().numpy()

# Sort documents by similarity (highest first)
 sorted_docs = sorted(zip(docs, similarities), key=lambda x: x[1], reverse=True)

# Return the top 3 most similar documents
 top_matches = [doc for doc, _ in sorted_docs[:3]]
 
 return {"matches": top_matches}

`
for Q8

`from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()
