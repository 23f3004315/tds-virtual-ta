---
chunk_id: discourse_topic_166357_post_1_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166357/1
source_title: Doubts in Q7, Q8
content_type: discourse
tokens: 312
username: Sakshi6479
post_number: 1
topic_id: 166357
---

 {"matches": top_matches}

`
for Q8

`from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

---

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

def calculate_performance_bonus(employee_id: int, current_year: int) -&gt; Dict[str, Any]:
 # Mock response for illustration purposes
 return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}
