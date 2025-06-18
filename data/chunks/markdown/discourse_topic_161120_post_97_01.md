---
chunk_id: discourse_topic_161120_post_97_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/97
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 362
username: 24f2006531
post_number: 97
topic_id: 161120
---

**[Discussion Image by 24f2006531]** This image depicts Python code within the context of a TDS student discussion about deployment tools, likely as a code snippet shared for debugging or demonstration purposes. The code defines a custom HTTP request handler class, inheriting from `BaseHTTPRequestHandler`, designed to handle `GET` and `OPTIONS` requests. The `do_GET` method sets CORS headers, loads JSON data from a file (located at `"../q-vercel-python.json"` relative to the script's directory), parses query parameters to extract names, and then searches for marks associated with those names in the loaded JSON data. If no names are provided in the query string, it returns a JSON error indicating the missing parameter; if marks are found, it returns them in the response, otherwise, it returns a "Name not found" error. The `do_OPTIONS` method handles CORS preflight requests by setting appropriate headers.ased on the 'name' parameter. It sets CORS headers for cross-origin requests using the `do_GET` and `do_OPTIONS` methods. The code checks if the `name` parameter is provided and returns an error message if it's missing. The code iterates through the JSON data, appending 'marks' values to a list if the 'name' matches, and returns these marks or an error if the name is not found. This looks like a student's implementation that could be part of a deployment tools assignment, showcasing backend logic for handling API requests." alt="image" data-base62-sha1="7RxQiQx0hI5v7xb7lKJg2yG5HSH" width="483" height="500" data-dominant-color="232323">image871×900 40.7 KB
