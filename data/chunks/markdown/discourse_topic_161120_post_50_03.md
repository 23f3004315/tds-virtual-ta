---
chunk_id: discourse_topic_161120_post_50_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/50
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 115
username: 23F300327
post_number: 50
topic_id: 161120
---

 None 
 for name in names
 ]

response = json.dumps({"marks": marks})
 self.send_response(200)
 self.send_header("Content-type", "application/json")
 self.send_header("Access-Control-Allow-Origin", "*") # Enable CORS
 self.end_headers()
 self.wfile.write(response.encode())

---

if __name__ == "__main__":
 server_address = ('', 8000) # Run on port 8000
 httpd = HTTPServer(server_address, MarksHandler)
 print("Server running on port 8000...")
 httpd.serve_forever()
`
