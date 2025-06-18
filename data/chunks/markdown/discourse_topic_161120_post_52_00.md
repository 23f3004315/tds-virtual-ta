---
chunk_id: discourse_topic_161120_post_52_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/52
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 285
username: carlton
post_number: 52
topic_id: 161120
---

## Post #52 by carlton

**Direct Link**: [Post #52](https://discourse.onlinedegree.iitm.ac.in/t/161120/52)

@23F300327

Typically for a vercel application, and in particular for GA2-Q6, the applications are basically function calls. You are not expected to setup and run a local http server as you are doing in your code.

When a call is made to the endpoint which in this scenario is /api

with parameters, only one function is required, i.e the function that handles the get request.

The rest is also automagically handled by vercel. There might be a conflict between vercel’s webserver deployment and the one you explicitly have encoded in your program.

That’s why if you see in the course content about vercel, the simplest API service that you can launch with vercel looks something like this

`# api/index.py
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
 def do_GET(self):
 self.send_response(200)
 self.send_header('Content-type','application/json')
 self.send_header("Access-Control-Allow-Origin", "*")
 self.end_headers()
 self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
 return
`
Notice there is no `if __name__ == "__main__":` code block.
