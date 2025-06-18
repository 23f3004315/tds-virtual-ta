---
chunk_id: discourse_topic_169029_post_687_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/687
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 328
username: Priya5379
post_number: 687
topic_id: 169029
---

**[Discussion Image by Priya5379]** This image shows a JSON response indicating an error in a student's SQL query, likely submitted for the "Project 2 - TDS Solver." The JSON includes the API endpoint being used and the test code "GA1_q18". The "status" field is "ERROR," and the "error" field contains the raw SQL query that triggered the syntax error, specifically in the `WHERE LOWER(type) = 'gold';` clause. The SQL query attempts to calculate the total sales of 'gold' tickets from the 'tickets' table, summing the product of 'price' and 'units'. The error message suggests a syntax issue close to where the query specifies `WHERE LOWER(type) = 'gold';` and that could be related to the single quotes, since `type` seems to be a string.he error "near ```sql\nSELECT SUM (price * units) AS total_sales\nFROM tickets\nWHERE LOWER(type) = 'gold';\n```: syntax error" suggests there's an issue in the SQL query being used for test case "GA1_q18". The query aims to calculate the total sales for tickets of type 'gold' and involves summing the product of price and units from the "tickets" table. The student needs to review and correct the SQL syntax." alt="image" data-base62-sha1="yYbrBa3tw7AwLEPLLlhhPGlWeOd" width="690" height="76" data-dominant-color="FAFAFA">image1491×166 5.46 KB
