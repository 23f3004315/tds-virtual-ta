---
chunk_id: discourse_topic_169029_post_171_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/171
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 290
username: 21f2000709
post_number: 171
topic_id: 169029
---

## Post #171 by 21f2000709

**Direct Link**: [Post #171](https://discourse.onlinedegree.iitm.ac.in/t/169029/171)

Saransh_Saini:
[Quote]: 
This is a basic prototype function we would be using to send requests to your URL.

`def run(question, file_path):
 url = "http://127.0.0.1:8080/api"
 questions = {'question': question}
 files = [
 ('file', open("abcd.zip", 'rb')),
 ('file', open("dcba.img", 'rb'))
 ]
 response = requests.post(url, data=questions, files=files)
 return response
`

I couldn’t find this function on the Project Doc and I made the project based on the curl function calling.

Saransh_Saini:
[Quote]: 
`curl -X POST "http://127.0.0.1:8080/api" \
 -H "Content-Type: multipart/form-data" \
 -F "question=question" \
 -F "file=@abcd.zip" \
 -F "file=@dcba.img"
`

At this moment it can’t be changed as I am occupied with other things. Please keep the question parameter as “question” and file parameter as “file” in the evaluation which is on the Project 2 page and the content type as multipart/form-data.
