---
chunk_id: discourse_topic_161120_post_45_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/45
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 302
username: 23f2003751
post_number: 45
topic_id: 161120
---

## Post #45 by 23f2003751

**Direct Link**: [Post #45](https://discourse.onlinedegree.iitm.ac.in/t/161120/45)

`{
 "version": 2,
 "builds": [
 {
 "src": "app.py",
 "use": "@vercel/python"
 }
 ],
 "routes": [
 {
 "src": "/api",
 "dest": "app.py"
 }
 ],
 "headers": [
 {
 "source": "/api/(.*)",
 "headers": [
 { "key": "Access-Control-Allow-Credentials", "value": "true" },
 { "key": "Access-Control-Allow-Origin", "value": "*" },
 {
 "key": "Access-Control-Allow-Methods",
 "value": "GET,OPTIONS,PATCH,DELETE,POST,PUT"
 },
 {
 "key": "Access-Control-Allow-Headers",
 "value": "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
 }
 ]
 }
 ]
}
`
@Jivraj @carlton

i have added the header key in order to use the cors as said in the vercel doc but still i am getting that error.

what to do?

i have added the cors in the app.py file as well

`from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
