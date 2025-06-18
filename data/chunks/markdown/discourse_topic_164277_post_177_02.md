---
chunk_id: discourse_topic_164277_post_177_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/177
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 314
username: 23f1002382
post_number: 177
topic_id: 164277
---

’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_bd83329f63’, ‘monthlyCost’: 0.048128640000000014, ‘cost’: 0.0026880000000000003, ‘monthlyRequests’: 51}

---

`def query_gpt_image(image_path: str, task: str):
 print("🔍 Image Path:", image_path)
 image_format = image_path.split(".")[-1]
 with open(image_path, "rb") as file:
 image_data = base64.b64encode(file.read()).decode("utf-8")
 response = requests.post(
 "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
 headers={"Authorization": f"Bearer {"APIKEY"}",
 "Content-Type": "application/json"},
 json={
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "user",
 "content": [
 {"type": "text", "text": task},
 {
 "type": "image_url",
 "image_url": { "url": f"data:image/{image_format};base64,{image_data}" }
 }
 ]
 }
 ]
 }
 )
 response.raise_for_status()
 print(response)
 print(response.json())
 result = response.json() 
response = query_gpt_image("data/credit_card.png","Extract the credit card number from image")
`
Why is this not working?

EDIT: Requires prompt engineering as “credit card” is sensitive information

&lt;Response [200]&gt;
