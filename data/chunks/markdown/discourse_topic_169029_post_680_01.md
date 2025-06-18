---
chunk_id: discourse_topic_169029_post_680_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/680
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 444
username: Anshul-IITM-DSA
post_number: 680
topic_id: 169029
---

 that may have led to this result.

I have deployed the project on vercel as instructed.

I have uploaded all the links in google form and submitted it.

To support this, I am attaching a screenshot of the PowerShell window that shows an example of my application running successfully for one of the questions.

---

**[Discussion Image by Anshul-IITM-DSA]** This image depicts a student's attempt to solve a TDS problem using the provided API endpoint via a PowerShell command. The student executes a POST request with the Google Sheets formula `=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 15, 7), 1, 10))` as the "question" parameter, noting it's intended for Google Sheets, not Excel. The PowerShell command used is `http -f POST "https://tds-solver-lyart.vercel.app/api/" question="=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 15, 7), 1, 10))"`. The API responds with a 200 OK status, returning a JSON payload `{"answer": 465, "status": "success"}`, indicating the problem was successfully solved with the answer 465. The student has successfully interfaced with the API to solve the given problem.yart.vercel.app/api/` with a question involving a Google Sheets formula `SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 15, 7), 1, 10))`. The instruction specifies this formula should be tried in Google Sheets, noting that it won't work in Excel. The API responds with a JSON object containing the `"answer": 465` and `"status": "success"`, indicating the TDS solver correctly evaluated the expression. The exchange aims to confirm if the student can construct formulas compatible with Google Sheets within the TDS solver context." alt="ss" data-base62-sha1="ljdUx5EEPRL2xkSX73F8uDHJWAp" width="690" height="242" data-dominant-color="131414">ss1525×535 24.1 KB
