---
chunk_id: discourse_topic_161120_post_13_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/13
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 94
username: 23F300327
post_number: 13
topic_id: 161120
---

: {class_}") # Debugging line
 if class_:
 filtered_students = [student for student in students if student["class"] in class_]
 print(f"Filtered students: {filtered_students}") # Debugging line
 return {"students": filtered_students}
 return {"students": students}

---

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="127.0.0.1", port=8000)
`
