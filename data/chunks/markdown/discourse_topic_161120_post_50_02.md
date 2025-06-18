---
chunk_id: discourse_topic_161120_post_50_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/50
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 328
username: 23F300327
post_number: 50
topic_id: 161120
---

 output provide valuable context for understanding the student's progress and potential challenges in the deployment process. 2x" data-dominant-color="0D0B0B">Screenshot 2025-01-21 at 1.37.06 PM1440×900 28.1 KB

---

when I paste the url it is showing TypeError: Failed to fetch

my code:

`import json
import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Load the CSV file into a DataFrame
try:
 data = pd.read_csv('marks.csv')
except FileNotFoundError:
 data = None

class MarksHandler(BaseHTTPRequestHandler):
 def do_GET(self):
 if data is None:
 self.send_response(500)
 self.send_header("Content-type", "application/json")
 self.send_header("Access-Control-Allow-Origin", "*")
 self.end_headers()
 self.wfile.write(json.dumps({"error": "marks.csv not found"}).encode())
 return

parsed_path = urlparse(self.path)
 query_params = parse_qs(parsed_path.query)
 names = query_params.get('name', []) # Get list of names from query parameters

marks = [
 int(data[data['name'] == name]['marks'].values[0]) if not data[data['name'] == name].empty else None 
 for name in names
 ]

response = json.dumps({"marks": marks})
 self.send_response(200)
 self.send_header("Content-type", "application/json")
 self.send_header("Access-Control-Allow-Origin", "*") # Enable CORS
 self.end_headers()
 self.wfile.write(response.encode())
