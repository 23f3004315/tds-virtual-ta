---
chunk_id: discourse_topic_164277_post_514_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/514
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 185
username: 23f2001286
post_number: 514
topic_id: 164277
---

## Post #514 by 23f2001286

**Direct Link**: [Post #514](https://discourse.onlinedegree.iitm.ac.in/t/164277/514)

More Particularily the failure occurs in the response portion…

`def get_completions(prompt: str):
 print("Inside get_completions")#Debug
 with httpx.Client(timeout=20) as client:
 response = client.post(
 f"{openai_api_chat}",
 headers=headers,
 json=
 {
 "model": "gpt-4o-mini",
 "messages": [
 {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
 {"role": "user", "content": prompt}
 ],
 "tools": [
 {
 "type": "function",
 "function": function
 } for function in function_definitions_llm
 ],
 "tool_choice": "auto"
 },
 )
