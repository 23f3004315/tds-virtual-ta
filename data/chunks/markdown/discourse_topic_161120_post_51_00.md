---
chunk_id: discourse_topic_161120_post_51_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/51
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 213
username: 23F300327
post_number: 51
topic_id: 161120
---

## Post #51 by 23F300327

**Direct Link**: [Post #51](https://discourse.onlinedegree.iitm.ac.in/t/161120/51)

`from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the CSV file into a DataFrame
data = pd.read_csv('marks.csv')

@app.route('/api', methods=['GET'])
def get_marks():
 # Get the list of names from query parameters
 names = request.args.getlist('name')
 
 # Ensure the order of the names in the response matches the query
 marks = [
 int(data[data['name'] == name]['marks'].values[0]) if not data[data['name'] == name].empty else None 
 for name in names
 ]
 
 return jsonify({"marks": marks})

if __name__ == '__main__':
 app.run(debug=True)
`
this is the 2nd code I am trying but same error TypeError: Failed to fetch
