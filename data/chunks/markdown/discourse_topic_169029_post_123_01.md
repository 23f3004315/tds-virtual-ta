---
chunk_id: discourse_topic_169029_post_123_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/123
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 174
username: carlton
post_number: 123
topic_id: 169029
---

.g., newline = 10, tab = 9

This is a great way to check what we are receiving when you send us some response,

`import requests
import json

# This is just an example server to see what we see.

url = "https://httpbin.org/post"

---

my_multiline_string_answer = """This is a multiline
string that spans
multiple lines with spaces 
and some newlines
and a tab	as well."""

response_to_send_to_tds_evaluator = {
"answer": my_multiline_string_answer
}

# Send the JSON data
response = requests.post (url, json=response_to_send_to_tds_evaluator)

# Check the response
print (response.status_code)
print (response.json ())
print (response.text)

# Do other checks as necessary... 
`
See what happens when I print the result
