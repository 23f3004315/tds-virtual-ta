---
chunk_id: discourse_topic_161120_post_134_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/134
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 301
username: 23f3004114
post_number: 134
topic_id: 161120
---

=1A`), should return only students from the specified class(es) in the order they appear in the CSV file. The student is using the provided API endpoint `http://127.0.0.1:8000/api` and has likely submitted their solution to the autograder.

---

The autograder feedback displays an error: "Response undefined does not match expected," followed by a JSON array of student objects (studentId and class). This indicates a mismatch between the student's API response and the expected output for a particular query. The student's browser's Network tab is open, showing two GET requests to `/api?class=1N&class=8N&class=8X&class=4Z`. The "Preview" tab reveals the JSON response from the API, containing a list of student objects. The problem appears to be that the API response isn't matching the expected output for the classes in the query string, resulting in the test failure. The instructions also emphasize enabling CORS to allow GET requests from any origin, implying this could be a potential area for troubleshooting, although the response data suggests CORS isn't the primary issue here since data is being returned. The student needs to debug their API logic to ensure that the filtering and ordering of results for multiple class parameters are correct. 2x" data-dominant-color="919393">Screenshot 2025-02-01 at 6.13.02 PM1920×1200 178 KB
