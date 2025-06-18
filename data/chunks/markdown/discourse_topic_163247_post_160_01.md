---
chunk_id: discourse_topic_163247_post_160_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/160
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 281
username: Abhishek11_11
post_number: 160
topic_id: 163247
---

 valid json format or Error: Model must be gpt-4o-mini, not undefined.

I have tried multiple approaches but the same issue even after using help from Chat GPT. Could any one tell what is the correct answer?? Thanks!

Here is my response for not valid json format error:

---

`{
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "system",
 "content": "Respond in JSON"
 },
 {
 "role": "user",
 "content": "Generate 10 random addresses in the US"
 }
 ],
 "response_format": "json",
 "tool_choice": "auto",
 "tools": [
 {
 "type": "function",
 "function": {
 "name": "generate_addresses",
 "parameters": {
 "$schema": "http://json-schema.org/draft-07/schema#",
 "type": "object",
 "properties": {
 "addresses": {
 "type": "array",
 "items": {
 "type": "object",
 "properties": {
 "apartment": { "type": "string" },
 "city": { "type": "string" },
 "street": { "type": "string" }
 },
 "required": ["apartment", "city", "street"],
 "additionalProperties": false
 }
 }
 },
 "required": ["addresses"],
 "additionalProperties": false
 }
 }
 }
 ]
}
`
