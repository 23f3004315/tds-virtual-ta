---
chunk_id: discourse_topic_171141_post_404_13
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/404
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 435
username: Haricharan
post_number: 404
topic_id: 171141
---

` uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000
`
**[Discussion Image by Haricharan]** This image depicts a student's attempt at project task C4, where the goal is to determine if the statement "I hate you" has a positive or negative connotation and save the result (POSITIVE or NEGATIVE) to /data/c5.txt in uppercase. The terminal output shows that the task failed (C4 FAILED). The initial POST request to localhost:8000 resulted in an HTTP 400 error ("No connection adapters were found..."). While the subsequent GET request to read the file from /data/c5.txt was successful (HTTP 200 OK), the expected answer was "NEGATIVE", but the result was `[('NEGATIVE',)]`. This indicates a subtle formatting issue in the student's output. The student's score is 6/25. An AIPROXY_TOKEN is visible in the .env file in the VS Code editor, and app.py and other project files are listed in the file explorer..txt`. The console shows an HTTP 400 error: "No connection adapters were found for 'data:text/plain; charset=utf-8, NEGATIVE'" after the POST request, indicating a problem with how the data is being sent in the HTTP request, most likely due to incorrect formatting of the data field. Despite the POST error, the GET request to read `/data/c5.txt` returns HTTP/1.1 200 OK and shows that the expected output was "NEGATIVE" while the result was `[('NEGATIVE',)]`, suggesting a discrepancy in the expected format. The student's score is 6/25 and the .env file containing the AIPROXY_TOKEN is open in the editor." alt="image" data-base62-sha1="foBysNTpTqXcrLMlwn4zNBPzKXx" width="690" height="483" data-dominant-color="201F1F">image1385×971 46.9 KB
