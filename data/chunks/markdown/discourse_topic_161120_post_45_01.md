---
chunk_id: discourse_topic_161120_post_45_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/45
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 174
username: 23f2003751
post_number: 45
topic_id: 161120
---

 in the vercel doc but still i am getting that error.

what to do?

i have added the cors in the app.py file as well

`from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

---

# Load the data
with open("q-vercel-python.json", "r") as f:
 data = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
 names = request.args.getlist("name")
 marks = [student["marks"] for student in data if student["name"] in names]
 return jsonify({"marks": marks})

if __name__ == "__main__":
 app.run()

`
https://student-marks-4vsd75x3f-tushars-projects-f2a54030.vercel.app/api
