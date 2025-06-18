---
chunk_id: discourse_topic_164277_post_545_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/545
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 304
username: 23f1002382
post_number: 545
topic_id: 164277
---

.completions.create(
 model="gpt-4o-mini",
 messages=[{"role": "user", "content": prompt}],
 temperature=0,
 response_format={"type": "json_object"}
 )
`

github.com/23f2005593/tds

app.py

`main`

---

`
 
 prompt = (
 f"The Python code generated for the task '{task}' produced the following error when executed:\n"
 f"{error_message}\n\n"
 f"Here is the original code:\n{original_code_data['code']}\n\n"
 "Please provide a corrected version of the code that fixes the error. Return only a JSON object with:\n"
 "- code: the corrected Python code as a string\n"
 "- function_name: name of the main function\n"
 "- required_libraries: list of required pip packages\n\n"
 "Make sure the code is simple, direct, and error-free this time. And try not to mess it up like before."
 )
 try:
 response = client.chat.completions.create(
 model="gpt-4o-mini",
 messages=[{"role": "user", "content": prompt}],
 temperature=0,
 response_format={"type": "json_object"}
 )
 except Exception as exc:
 logger.error("Error connecting to OpenAI API for auto-fix: %s", exc)
 raise HTTPException(status_code=500, detail="Connection error during auto-fix. Maybe it's time to admit defeat?")

`

you are taking a chance on that format
