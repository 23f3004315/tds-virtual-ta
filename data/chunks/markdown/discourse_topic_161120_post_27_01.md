---
chunk_id: discourse_topic_161120_post_27_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/27
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 217
username: 23F300327
post_number: 27
topic_id: 161120
---

 "class": row["class"]
 })

@app.get("/api")
async def get_students(class: Optional[List[str]] = Query(None)): 
 """
 Retrieves a list of students, optionally filtered by class.

Args:
 class: A list of class names to filter by. If None, returns all students.

---

Returns:
 A dictionary containing a list of students.
 """
 print(f"Requested classes: {class}") # Debugging line
 if class:
 filtered_students = [student for student in students if student["class"] in class]
 else:
 filtered_students = students
 print(f"Filtered students: {filtered_students}") # Debugging line
 return {"students": filtered_students}

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="127.0.0.1", port=8000)

`
@Jivraj this is the code I’m executing which is not getting accepted in the answer box the last time I modified the code it got accepted and I also saved the answer but when I reopened the page till now it is not getting accepted
