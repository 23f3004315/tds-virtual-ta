---
chunk_id: discourse_topic_163247_post_135_05
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/135
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 315
username: Sakshi6479
post_number: 135
topic_id: 163247
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
Please kindly guide me with these problems as I am trying to do it since last 3 days. I am exhaust now, Please help me with this. @Jivraj , @carlton , @Saransh_Saini
