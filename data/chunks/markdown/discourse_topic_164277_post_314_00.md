---
chunk_id: discourse_topic_164277_post_314_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/314
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 297
username: 22f3002723
post_number: 314
topic_id: 164277
---

## Post #314 by 22f3002723

**Direct Link**: [Post #314](https://discourse.onlinedegree.iitm.ac.in/t/164277/314)

when trying to use function call way of open api

`tools = [
 {
 "type": "function",
 "function": {
 "name": "extract_email_sender",
 "description": "Extract sender email from a specific file in directory",
 "parameters": {},
 "strict": True
 }
 },
 {
 "type": "function",
 "function": {
 "name": "count_day_of_week",
 "description": "To count the occurances of a specific day of a week in a file with various dates",
 "parameters": {
 "type": "object",
 "properties": {
 "day_of_week": {
 "type": "string",
 "description": "day of week"
 }
 },
 "required": ["day_of_week"],
 "additionalProperties": False
 },
 "strict": True
 }
 }
]
`
` payload = {
 "model": "gpt-4o-mini",
 "messages": [
 {"role": "user", "content": user_input},
 
 ], 
	"tools": tools,
 "tool_choice": "auto",
 "max_tokens": 500,
 "temperature": 0.7
 }
`
facing the below issue

ror’: {‘message’: “Invalid type for ‘tools[0]’: expected an object, but got an array instead.”
