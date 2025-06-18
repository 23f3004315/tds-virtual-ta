---
chunk_id: discourse_topic_164277_post_15_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/15
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 321
username: 23f2005325
post_number: 15
topic_id: 164277
---

0000000003, 'monthlyRequests': 31, 'costError': 'crypto.createHash is not a function'}
`
my code is as below :

`def extract_credit_card_number():
 import requests
 import base64
 import os
 from dotenv import load_dotenv
 load_dotenv()

---

BASE_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
 headers = {
 "Content-Type": "application/json",
 "Authorization": f"Bearer {os.environ["AIPROXY_TOKEN"]}"
 }

image_path = "../data/credit_card.png"

with open(image_path, "rb") as image_file:
 base64_image = base64.b64encode(image_file.read()).decode("utf-8")

payload = {
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "system", 
 "content": "You are a helpful assistant that provides detailed and accurate descriptions of images. Focus on describing the objects, colors, textures, the overall scene, and most importantly, the text and numbers in the image. Be concise but thorough."
 },
 {
 "role": "user",
 "content": [
 {
 "type": "text",
 "text": "You are given an image containing a credit card number. Extract the credit card number from the image"
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
