---
chunk_id: discourse_topic_171141_post_33_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/33
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 972
username: Jivraj
post_number: 33
topic_id: 171141
---

 also rerun evaluations for all the x86 and arm images one more time, before pushing to the dashboard.

23f3003302:
[Quote]: 
Hi @jivraj,

@23f3003302 output from your server’s response is correct, we will update our evaluation script.

---

23f2004912:
[Quote]: 
**[Discussion Image by Jivraj]** This image captures a failed test case in a student's project related to data scraping, specifically 'B6'. The test expects a flat list of author names, but the actual result is nested under a ".author" key within a JSON structure, revealed by the "RESULT" section showing author names listed under `".author": [...]`. The error message indicates a mismatch between the expected output `['Albert Einstein', 'J.K. Rowling', ... 'Steve Martin']` and the actual structure. Additionally, the scraped data is saved to `./data/b6.json`, as confirmed by the initial "HTTP 200" message, and the HTTP request to retrieve the data is `GET http://localhost:8052/read?path=/data/b6.json`. The encoding of 'André Gide' is also visible as "Andr\\u00e9 Gide" in the result.to be incorrect in the result, showing "Andr\u00e9 Gide". This likely indicates an issue with the data transformation or parsing logic within the student's code that needs to be addressed to match the expected format." alt="image" data-base62-sha1="bhTEWgYwF8mPxpMmqTUo8H2BOwB" width="690" height="276" srcset="**[Discussion Image by Jivraj]** This image shows a student's attempt at Project 1, specifically task B6, which has failed. The output indicates the scraped data was saved to "./data/b6.json". The test failed because the expected output (a simple list of author names) does not match the actual result (a nested JSON structure with ".author" as the key and the list of names as the value). The expected list is `['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']` and the actual result is a JSON array with the author nested in a key `.author`. This discrepancy means the student's code is creating a nested JSON structure, instead of a flat list as required by test B6. The Unicode representation of "André" (\u00e9) suggests the scraped data might have encoding issues as well., **[Discussion Image by Jivraj]** This image shows a discrepancy during Project 1, likely a student's attempt to solve task B6, and depicts a failing test case. The system output indicates that while the scraping was successful and the data was saved to `/data/b6.json`, the content of the saved file does not match the expected output. The expected output is a JSON array of strings: `['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']`. However, the actual result shows a JSON object with a key `"author"` and a value that is an array of strings, revealing an incorrect JSON structure. The difference is that the result data is nested one level deeper inside the `"author"` field, and the "André Gide" string contains a unicode escape character sequence. The test case "B6 FAILED" indicates the student needs to correct their data transformation or scraping logic to ensure the data matches the expected format. 1.5x, **[Discussion Image by Jivraj]** This image captures a student encountering an issue in TDS Project 1, specifically with test case B6. The log shows the scraper successfully saved data to `./data/b6.json` and that a GET request to retrieve the file was also successful. However, the test failed because the "EXPECTED" output (a list of author names) doesn't match the "RESULT" output, which contains a ".author" key wrapping the author list. The student's scraper is returning the author list nested within a dictionary, rather than as a flat list as required by the test. The problem suggests that the student needs to adjust their scraping logic to extract the author names directly into a list without the extra dictionary layer. 2x" data-dominant-color="FCFCFC">image1460×585 24.9 KB
