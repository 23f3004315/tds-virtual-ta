---
chunk_id: discourse_topic_164277_post_15_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/15
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 134
username: 23f2005325
post_number: 15
topic_id: 164277
---

 card number. Extract the credit card number from the image"
 },
 {
 "type": "image_url",
 "image_url": {
 "url": f"data:image/png;base64,{base64_image}"
 }
 }
 ]
 }
 ],
 }

response = requests.post(BASE_URL, headers=headers, json=payload)

---

if response.status_code == 200:
 result = response.json()
 print("RESULT:", result)
 cno = result["choices"][0]["message"]["content"]
 print("CREDIT CARD NUMBER:", cno)
 else:
 print(f"Error: {response.status_code}")
 print(response.text)
`
please guide @Jivraj @Saransh_Saini
