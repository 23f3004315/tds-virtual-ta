---
chunk_id: discourse_topic_163247_post_47_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/47
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 210
username: 23f2003853
post_number: 47
topic_id: 163247
---

0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

---

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
 "model": "gpt-4o-mini", 
 "messages": [{"role": "user", "content": user_message}],

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
 input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
 print(f"Input tokens used: {input_tokens}")
else:
 print(f"Request failed with status code {response.status_code}: {response_json}")````
