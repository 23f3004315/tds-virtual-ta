---
chunk_id: discourse_topic_164277_post_513_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/513
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 472
username: 23f2001286
post_number: 513
topic_id: 164277
---

@jkmadathil @carlton @Jivraj

Sir earlier my code was running fine, but after the assigment of the new token,

it is now showing 400 bad request, which simply implies there is something wrong with the token…

plz do something sir…

---

**[Discussion Image by 23f2001286]** This image shows a log from the TDS Project 1 discussion, indicating a student is encountering issues with their LLM-based automation agent. The log displays two errors: a "400 Bad Request" error from a POST request to the "/run" endpoint, indicating a problem with the task prompt, which includes a SQLite database query to calculate ticket sales for "Gold" type tickets. The prompt instructs the agent to write the number to `/data/ticket-sales-gold.txt`. A subsequent "404 Not Found" error arises from a GET request to "/read?path=/data/ticket-sales-gold.txt," implying that the agent either failed to write the output to the file correctly, or the file was not created at all, leading to the error during retrieval. The student likely needs to review the task prompt for syntax errors, ensure proper database connection, and verify the file writing operation within their agent to resolve the issue.rror in response to a "POST" request to the "/run" endpoint, likely triggered by a task involving querying a SQLite database ('ticket-sales.db') about concert tickets and writing the total sales of Gold tickets to 'ticket-sales-gold.txt'. The URL-encoded query asks to sum sales of items of "Gold" ticket type, which is possibly malformed causing the bad request. The second line shows a "404 Not Found" error for a "GET" request to "/read?path=/data/ticket-sales-gold.txt", indicating that the agent could not locate the file it was supposed to write to in the previous failed step, likely due to the preceding "400 Bad Request" error. The discussion probably revolves around the student debugging the query construction or file path issues." alt="image" data-base62-sha1="l0fCGZdX1ZTq0lLZMhY1m9blb3A" width="690" height="41" data-dominant-color="3A3939">
