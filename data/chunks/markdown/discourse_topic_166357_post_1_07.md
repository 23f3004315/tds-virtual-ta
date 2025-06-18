---
chunk_id: discourse_topic_166357_post_1_07
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166357/1
source_title: Doubts in Q7, Q8
content_type: discourse
tokens: 266
username: Sakshi6479
post_number: 1
topic_id: 166357
---

 }
 elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
 return {
 "name": "report_office_issue",
 "arguments": {
 "issue_code": int(match.group(1)),
 "department": match.group(2)
 }
 }
 return {}

---

@app.get("/execute")
async def execute_query(q: str):
 # Extract the function name and arguments from the query
 result = extract_parameters(q)
 
 if not result:
 return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)
 
 # Call the respective function
 func_name = result["name"]
 arguments = result["arguments"]
 
 # Call the function dynamically based on func_name
 if func_name == "get_ticket_status":
 response = get_ticket_status(**arguments)
 elif func_name == "schedule_meeting":
 response = schedule_meeting(**arguments)
 elif func_name == "get_expense_balance":
 response = get_expense_balance(**arguments)
 elif func_name == "calculate_performance_bonus":
 response = calculate_performance_bonus(**arguments)
 elif func_name == "report_office_issue":
 response = report_office_issue(**arguments)
 
 # Return the response in the requested format
 return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)

`
