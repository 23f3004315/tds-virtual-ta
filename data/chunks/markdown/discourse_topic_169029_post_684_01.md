---
chunk_id: discourse_topic_169029_post_684_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/684
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 294
username: Priya5379
post_number: 684
topic_id: 169029
---

**[Discussion Image by Priya5379]** This image depicts a student question regarding an error encountered in the TDS Solver project, specifically showing a JSON response object indicating a SQL syntax error. The "status" field is "ERROR" and the "error" field contains the specific syntax error message along with the problematic SQL query. The query aims to calculate the sum of (price * units) as total_sales from the 'tickets' table where the lowercase of the 'type' column equals 'gold'. The error message hints at a syntax issue near the end of the provided SQL query, before the closing backticks. The student likely needs to carefully review the SQL syntax within the WHERE clause, paying close attention to the use of single quotes and parentheses.L query `SELECT SUM(price * units) AS total_sales FROM tickets WHERE LOWER(type) = 'gold'` is embedded within a string, indicating the query itself has a syntax problem. The error message suggests the syntax error is located near the end of the query, likely related to how the 'gold' string is handled or a missing semicolon within the query itself when running against the test suite." alt="image" data-base62-sha1="8tEKQXoSjHVSmyV2LB11QNVr64q" width="690" height="68" data-dominant-color="F8F8F8">image1430×142 5.42 KB
