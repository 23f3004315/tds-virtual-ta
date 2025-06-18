---
chunk_id: discourse_topic_167172_post_1_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/1
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 947
username: Sakshi6479
post_number: 1
topic_id: 167172
---

 response")
 except KeyError as e:
 raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
 except Exception as e:
 raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
 
 return output

---

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)
`
**[Discussion Image by Sakshi6479]** This image captures a student's question related to a project assignment, showing troubleshooting within Postman. The student is attempting to send a POST request to `http://127.0.0.1:8000/run?task=Sort the array of contacts in/...` with the `task` parameter set to "Sort the array of contacts...". The server is responding with a 200 OK status, but the JSON response body contains an error message: `"error": "Failed to sort contacts: File /data/contacts.json does not exist"`. This indicates that the student's code is attempting to read a `contacts.json` file from the `/data/` directory, but the file is not found, representing the student's core issue. The UI shows common Postman elements: the request URL, request method (POST), parameters, headers, body as JSON, and the response display.ly sent the request correctly through Postman, but the backend code is failing to locate the data source." alt="Screenshot 2025-02-14 171217" data-base62-sha1="5kpj9Kh1zIaAJZmIig1SCQTXOtL" width="690" height="446" srcset="**[Discussion Image by Sakshi6479]** This image captures a student encountering an error while testing their project using Postman, indicating a peer discussion where the student is likely seeking help. The request is a POST to `http://127.0.0.1:8000/run?task=Sort the array of contacts in ...`, with "task" as a parameter. The response body in JSON format shows the error: `"error": "Failed to sort contacts: File /data/contacts.json does not exist"`. This suggests the application is attempting to read a `contacts.json` file from the `/data/` directory, but the file is not found, which the student needs to resolve by ensuring the file exists at the specified path., **[Discussion Image by Sakshi6479]** This image depicts a student's troubleshooting process for Project 1, specifically addressing an issue where the application fails to locate the `contacts.json` file after a POST request. The student is using Postman to send a POST request to `http://127.0.0.1:8000/run?task=Sort the array of contacts in ...` with a parameter `task` set to "Sort the array of contacts i...". The response body in JSON format shows a "200 OK" status, but contains an error message: `"error": "Failed to sort contacts: File /data/contacts.json does not exist"`. This indicates that the server-side code, when attempting to sort contacts, cannot find the specified data file, suggesting a file path or directory issue within the project structure. The UI elements indicate this is a client-side HTTP request debugging scenario within Postman, with the student likely seeking guidance on resolving the file path error. 1.5x, **[Discussion Image by Sakshi6479]** This image depicts a student's issue with a project, specifically project 1, where a file is not being detected after sending a POST request. The student is using Postman to make a POST request to `http://127.0.0.1:8000/run?task=Sort the array of contacts in ...` with a "task" parameter. The response body returns a JSON object containing an error message: `"error": "Failed to sort contacts: File /data/contacts.json does not exist"`. The error message indicates that the application is unable to locate the `/data/contacts.json` file, suggesting either a file path issue, the file does not exist in the expected location, or there are permission problems preventing access to the file. The student likely needs to verify the file path and ensure the `contacts.json` file is present in the `/data/` directory relative to the application's execution path. 2x" data-dominant-color="272728">Screenshot 2025-02-14 1712172075×1343 176 KB
