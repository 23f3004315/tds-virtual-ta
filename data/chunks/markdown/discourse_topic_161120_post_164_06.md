---
chunk_id: discourse_topic_161120_post_164_06
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/164
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 279
username: 22f3000657
post_number: 164
topic_id: 161120
---

 format with other data formats they might encounter during the deployment process. The image thus represents a step in a debugging or data verification process, where the student is checking the response from the API. 2x" data-dominant-color="181818">image1919×1079 185 KB

---

The main code is below

`import sys

sys.path.append("C:\\Users\\Deveshu Pathak\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\Scripts")
# tds_q9.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], 
 allow_credentials=True,
 allow_methods=["*"], 
 allow_headers=["*"], 
)

# Load CSV file
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
 if class_:
 filtered_df = df[df["class"].isin(class_)]
 else:
 filtered_df = df

# Convert to dictionary list
 students = filtered_df.to_dict(orient="records")
 return {"students": students}
`
