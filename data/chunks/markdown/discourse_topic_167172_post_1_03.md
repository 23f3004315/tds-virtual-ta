---
chunk_id: discourse_topic_167172_post_1_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/1
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 412
username: Sakshi6479
post_number: 1
topic_id: 167172
---

.get("/")
def home():
 return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
 try:
 with open(path, "r") as f:
 return f.read()
 except Exception as e:
 raise HTTPException(status_code=404, detail="File does not exist")

---

@app.post("/run")
async def run(task: str):
 query = query_gpt(task)
 print(query) # Print the full response to inspect it.
 
 if 'choices' not in query:
 raise HTTPException(status_code=500, detail="Invalid response format from GPT API")
 
 try:
 tool_calls = query['choices'][0]['message'].get('tool_calls', [])
 if tool_calls:
 func_name = tool_calls[0]['function']['name']
 args = json.loads(tool_calls[0]['function']['arguments'])
 
 # Map function names to their respective functions
 function_map = {
 "cakebake": cakebake,
 "install_uv_and_run_datagen": install_uv_and_run_datagen,
 "format_markdown_file": format_markdown_file,
 "count_wednesdays": count_wednesdays,
 "sort_contacts": sort_contacts,
 "extract_recent_logs": extract_recent_logs,
 "create_markdown_index": create_markdown_index,
 "extract_sender_email": extract_sender_email,
 "extract_credit_card_number": extract_credit_card_number,
 "find_similar_comments": find_similar_comments,
 "calculate_gold_ticket_sales": calculate_gold_ticket_sales,
 }
 
 if func_name in function_map:
 output = function_map[func_name](**args)
 else:
 raise HTTPException(status_code=500, detail="Unknown function called")
 else:
 raise HTTPException(status_code=500, detail="No function call found in response")
 except KeyError as e:
 raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
 except Exception as e:
 raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
 
 return output
