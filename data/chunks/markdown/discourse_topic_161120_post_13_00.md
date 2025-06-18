---
chunk_id: discourse_topic_161120_post_13_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/13
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 273
username: 23F300327
post_number: 13
topic_id: 161120
---

## Post #13 by 23F300327

**Direct Link**: [Post #13](https://discourse.onlinedegree.iitm.ac.in/t/161120/13)

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
async def get_students(class_: Optional[List[str]] = Query(None)):
 print(f"Requested classes: {class_}") # Debugging line
 if class_:
 filtered_students = [student for student in students if student["class"] in class_]
 print(f"Filtered students: {filtered_students}") # Debugging line
 return {"students": filtered_students}
 return {"students": students}
