---
chunk_id: discourse_topic_169029_post_123_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/123
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 278
username: carlton
post_number: 123
topic_id: 169029
---

## Post #123 by carlton

**Direct Link**: [Post #123](https://discourse.onlinedegree.iitm.ac.in/t/169029/123)

Your markdown must have newline characters or spaces wherever necessary. Otherwise we will not be able to check if your answer is correct. Our parser will only work if encodings for the formatting are present in the response. If there are no encodings (invisible or visible) then we will not have the correctly formatted file.

Please review module 1 for a better understanding about how text is encoded. Especially invisible characters.

The browser is designed for user friendliness. Thats why the characters are invisible when you copy paste string with newlines. But it exists.

The programmatic strings show invisible encodings as escaped characters. (Usually)

To check if a string has invisible characters,

`# Multi-line string
my_string = """Hello
World with spaces 
and some newlines
and a tab	"""

# Print ASCII values of each character
print([ord(c) for c in my_string])
`
e.g., newline = 10, tab = 9

This is a great way to check what we are receiving when you send us some response,

`import requests
import json

# This is just an example server to see what we see.

url = "https://httpbin.org/post"
