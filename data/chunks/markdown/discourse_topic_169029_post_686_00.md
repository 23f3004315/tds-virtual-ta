---
chunk_id: discourse_topic_169029_post_686_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/686
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 296
username: Algsoch
post_number: 686
topic_id: 169029
---

## Post #686 by Algsoch

**Direct Link**: [Post #686](https://discourse.onlinedegree.iitm.ac.in/t/169029/686)

Case 3: JSON Key Count – XF Parameter (GA5_q7)

{

“api”: “https://app.algsoch.tech/api/”,

“test_code”: “GA5_q7”,

“status”: “ERROR”,

“error”: “invalid literal for int() with base 10: ‘Error: Invalid JSON in the file. Expecting value: line 1 column 1 (char 0)’”

}

What Was Expected:
The question required developing a script that:

Parses a large, deeply nested JSON log file, and

Counts how many times a specific key — represented by XF — appears in the JSON structure.

It was explicitly stated that:

Only key matches for XF are to be counted, not values.

The file to be used was:

E:\data science tool\GA5\q-extract-nested-json-keys.json

What I Did:
I used the correct approach, parsing the nested JSON file and counting how many times the key XF appeared throughout the structure.

Here’s the actual response I got using this cURL command:

curl -X POST https://app.algsoch.tech/api/ \

-H “accept: application/json” \

-F “question=…How many times does XF appear as a key?” \
