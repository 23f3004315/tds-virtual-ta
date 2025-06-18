---
chunk_id: discourse_topic_161120_post_27_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/27
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 241
username: 23F300327
post_number: 27
topic_id: 161120
---

## Post #27 by 23F300327

**Direct Link**: [Post #27](https://discourse.onlinedegree.iitm.ac.in/t/161120/27)

`from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], # Allow all origins
 allow_credentials=True,
 allow_methods=["*"], # Allow all methods
 allow_headers=["*"], # Allow all headers
)

# Load student data from the specified CSV file
students = []
with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
 reader = csv.DictReader(file)
 for row in reader:
 students.append({
 "studentId": int(row["studentId"]),
 "class": row["class"]
 })

@app.get("/api")
async def get_students(class: Optional[List[str]] = Query(None)): 
 """
 Retrieves a list of students, optionally filtered by class.

Args:
 class: A list of class names to filter by. If None, returns all students.
