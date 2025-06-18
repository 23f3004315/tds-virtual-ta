---
chunk_id: discourse_topic_169029_post_445_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/445
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 355
username: 23f3001764
post_number: 445
topic_id: 169029
---

**[Discussion Image by 23f3001764]** This image depicts a student's interaction with the TDS solver API, likely as part of Project 2. The student uses a `curl` command to send a POST request to the API endpoint `/api/`, including the question "Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel) =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 5, 2), 1, 10)) What is the result?". The request specifies a `Content-Type` of `multipart/form-data`. The API responds with `{"answer":"140"}`, indicating that the TDS solver correctly calculated the result of the Google Sheets formula. This demonstrates the student successfully using the API to solve a Google Sheets formula question. specified `/api/` endpoint, including a question about a Google Sheets formula. The formula provided is `=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 5, 2), 1, 10))`, which generates a sequence of numbers and then constrains it to a single row of 10 columns before summing the values. The API responds with a JSON object: `{"answer": "140"}`, indicating that the TDS solver correctly evaluated the Google Sheets formula. This suggests that the student successfully implemented and tested their solution against a specific test case." alt="image" data-base62-sha1="4vgA4z7D6KJ6V22YRpjlpclLZO0" width="517" height="93" data-dominant-color="151611">image965×175 6.84 KB
