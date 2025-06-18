---
chunk_id: discourse_topic_169029_post_686_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/686
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 292
username: Algsoch
post_number: 686
topic_id: 169029
---

 the key XF appeared throughout the structure.

Here’s the actual response I got using this cURL command:

curl -X POST https://app.algsoch.tech/api/ \

-H “accept: application/json” \

-F “question=…How many times does XF appear as a key?” \

---

-F “file=@E:\data science tool\GA5\q-extract-nested-json-keys.json”

API Output:{“answer”:“14602”}

This indicates that my logic worked correctly and the key XF appeared 14,602 times, exactly as intended.

What Went Wrong on API Side:
The API returned a parsing error, indicating:

“invalid literal for int() with base 10: ‘Error: Invalid JSON in the file…’”

However:

My file was valid JSON, properly parsed.

The actual issue seems to be on the API’s side — possibly mishandling the file read or decoding before passing it to the evaluator.

It may have expected an integer but received a string-wrapped error or non-integer data, causing it to crash.

Insight:
If the original question was about counting the key XF, my solution was 100% correct.

However, if the question dynamically changed the key name or added extra criteria (e.g., only count if value == true, or only under a certain section), then the result might differ. But from the default XF-focused question, my logic and result match perfectly.
