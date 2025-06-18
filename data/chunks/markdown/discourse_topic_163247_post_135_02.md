---
chunk_id: discourse_topic_163247_post_135_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/135
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 346
username: Sakshi6479
post_number: 135
topic_id: 163247
---

 similarity
 similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
 ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]
 
 return JSONResponse(content={"matches": ranked_docs[:3]})

---

# Optionally, handle requests to the root (GET /)
@app.get("/")
async def root():
 return {"message": "Welcome to the similarity API!"}
`
`
and for Q8

`from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], # Allows all origins
 allow_credentials=True,
 allow_methods=["*"], # Allows all methods (GET, POST, etc.)
 allow_headers=["*"], # Allows all headers
)
def get_ticket_status(ticket_id: int) -&gt; Dict[str, Any]:
 # Mock response for illustration purposes
 return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -&gt; Dict[str, Any]:
 # Mock response for illustration purposes
 return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -&gt; Dict[str, Any]:
 # Mock response for illustration purposes
 return {"employee_id": employee_id, "balance": 1000.0}
