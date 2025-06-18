---
chunk_id: discourse_topic_169029_post_123_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/123
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 186
username: carlton
post_number: 123
topic_id: 169029
---

-base62-sha1="oH1VnNagrJMWv1kL9vEZ36eOUoU" width="323" height="120">Screenshot 2025-03-27 at 1.09.56 pm323×120 3.61 KB

---

Its a proper multiline correctly formatted text! The encodings are invisible just like in the original as well as in your clipboard when you copy paste into the GA.

Here is a json example:

`json_answer = {
 "mary": "poppins",
 "age": 42
}

stringed_json = json.dumps (json_answer)
response_to_send_to_tds_evaluator = {
"answer": stringed_json
}

response = requests.post (url, json=response_to_send_to_tds_evaluator)

print (json.loads (response.text)['json']['answer'])
`
Look at the response. A perfect json.
