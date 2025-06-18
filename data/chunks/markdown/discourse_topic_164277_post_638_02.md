---
chunk_id: discourse_topic_164277_post_638_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/638
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 999
username: Sakshi6479
post_number: 638
topic_id: 164277
---

 "role": "user", 
 "content": task
 },
 {
 "role": "system",
 "content": f"""{primary_prompt}"""
 }
 ],
 "response_format": response_format
 }

response = requests.post(url=url, headers=headers, json=data)
 r = response.json()

return r

---

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)
`
**[Discussion Image by Sakshi6479]** This image depicts a student's troubleshooting process using Postman while working on the LLM-based Automation Agent project. The student is making a POST request to `http://localhost:8000/run?task=The file /data/dates.txt con...` with a parameter "task" set to "The file /data/dates.txt con...". The response body indicates an error: `"message": "Invalid value: 'json'. Supported values are: 'json_object', 'json_schema', and 'text'."`, suggesting that the server expects the response format type to be one of the specified options rather than the default JSON. The student needs to adjust the request parameters, specifically the `response_format.type`, to resolve this error and successfully interact with the LLM agent, which is likely a point of confusion in understanding how to correctly format the request. The image shows the response also contains "monthlyCost", "cost", and "monthlyRequ" outside of the error, suggesting the request reached the LLM and produced some output before the error occurred.cific string format rather than JSON format." alt="Screenshot 2025-02-14 185820" data-base62-sha1="nGMHoGQOqao8rFmV5aSYe2okJXK" width="655" height="500" srcset="**[Discussion Image by Sakshi6479]** This image depicts a student encountering an error while attempting to use a POST request to a local endpoint `http://localhost:8000/run` within a tool like Postman or Insomnia. The student is passing a `task` parameter with the value "The file /data/dates.txt con..." in the request parameters section. The server returns a 200 OK status, but the response body contains a JSON error message indicating an "invalid_value" for the "response_format.type", suggesting that the server expects a JSON object, JSON schema, or text, but receives something else, possibly due to how the task parameter is being interpreted. The response also includes 'monthlyCost', 'cost' and 'monthlyReq' values, likely related to the server's processing but are overshadowed by the primary error. The student is likely trying to send a file path as a parameter, which is not the intended format, causing the backend to fail to parse the request correctly., **[Discussion Image by Sakshi6479]** This image depicts a student facing an error while working on the TDS Project 1 using an LLM-based automation agent, and it appears to be a student question related to the error. The student is using a POST request to `http://localhost:8000/run?task=The file /data/dates.txt con...` and the response contains a JSON body with an "error" field. The error message "Invalid value: 'json'. Supported values are: 'json_object', 'json_schema', and 'text'." suggests an issue with the expected response format type. It also highlights that the request expects a specific response_format.type, likely one of 'json_object', 'json_schema', or 'text', and the current request is sending 'json', causing an "invalid_request_error". 1.5x, **[Discussion Image by Sakshi6479]** This image depicts a student debugging an HTTP POST request to `http://localhost:8000/run?task=The file /data/dates.txt co...` using a tool like Postman or Insomnia. The "Params" section shows a 'task' parameter being passed with the value "The file /data/dates.txt co...". The response body, formatted as JSON, returns a `200 OK` status but includes an "error" object indicating `"message": "Invalid value: 'json'. Supported values are: 'json_object', 'json_schema', and 'text'."`. This indicates the server expected a different 'response_format.type' than the default 'json' being used, requiring the student to adjust the request or server configuration to align the expected and provided data types. Additionally, the response includes "monthlyCost" and "cost" values, suggesting the request aims to calculate or return cost-related information, although the error prevents proper execution. 2x" data-dominant-color="272828">Screenshot 2025-02-14 1858201945×1484 229 KB
