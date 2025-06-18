---
chunk_id: discourse_topic_169029_post_65_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/65
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 327
username: 23f2004837
post_number: 65
topic_id: 169029
---

Direct Link**: [Post #65](https://discourse.onlinedegree.iitm.ac.in/t/169029/65)

my small piece of code to evaluate the GA number parsing, it may be useful for some

`
import httpx, os
import json
import logging
import random

---

async def run(task: str):
 async with httpx.AsyncClient(timeout=30) as client:
 logging.warning(f"🟡 Running task: {task.strip()}")
 data = {
 "question": task
 }
 files = {}
 response = await client.post("http://localhost:8000/api/parse", data=data, files=files)
 try:
 response_text = response.json()
 except json.JSONDecodeError:
 response_text = response.text
 if response.status_code &lt; 400:
 logging.info(f"🟢 HTTP {response.status_code} {response_text}")
 else:
 logging.error(f"🔴 HTTP {response.status_code} {response_text}")
 return response.status_code, response_text
 
async def evaluate(use_case: str):
 # file exists under test_data directory
 file_path = f"test_data/{use_case}.txt"
 if os.path.exists(file_path):
 with open(file_path, "r") as file:
 task = file.read()
 status_code, response_text = await run(task)
 if status_code != 200:
 return False
 
 # check the returned json matches the use case
 if "GA_No" in response_text and response_text["GA_No"] == use_case:
 return True
 else:
 return False
 else:
 #print("File does not exist.")
 return False
