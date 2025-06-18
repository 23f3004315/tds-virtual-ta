---
chunk_id: discourse_topic_163247_post_48_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/48
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 354
username: 24f2006531
post_number: 48
topic_id: 163247
---

 context and thread name, it is unlikely this relates to code snippets or error messages." alt="image" data-base62-sha1="dOWXuMn1NzBuHNYXw6RnYs0LbPT" width="332" height="84">

---

The below is my code for the question.

`import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
 "Authorization": "Bearer api_key",
 "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4 AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
 "model": "gpt-4o-mini",
 "messages": [
 {"role": "system", "content": system_message}, # System message
 {"role": "user", "content": user_message} # One user message
 ],
 "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
 print("AI Response:", choice["message"]["content"])
`
I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative

`user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"`

The error message i keep receiving is as below.
