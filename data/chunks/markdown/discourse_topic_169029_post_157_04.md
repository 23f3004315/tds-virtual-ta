---
chunk_id: discourse_topic_169029_post_157_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/157
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 384
username: lakshaygarg654
post_number: 157
topic_id: 169029
---

**[Discussion Image by lakshaygarg654]** This image shows a student's attempt to use the `httpx` library to interact with the OpenAI API for sentiment analysis, as part of a TDS project. The code includes constructing a JSON payload with a system message instructing the model to analyze text sentiment as good, bad, or neutral, and a user message containing the text to be analyzed. There's also error handling using a try-except block and a print statement to display the API's "answer" field after loading the JSON response. The student appears to be facing issues with the way the string for `my_response` is formatted, including numerous escaped characters (`\`) and newline characters (`\n`), causing potential errors in the overall request and potentially incorrect or missing `data`.ment` that sends a request to the OpenAI chat completion endpoint. The code snippet shows how the student sets up the API request, including the URL, headers (Authorization with a dummy API key and Content-Type), and data (model and messages for the sentiment analysis task). A crucial aspect is the `my_response` variable containing a stringified JSON with escape characters, intended to embed the entire script within a larger response structure. After defining the API call, the student tries to execute the `analyze_sentiment` function and print the result, catching potential exceptions. Finally, the student attempts to extract the "answer" from the stringified json with `print(json.loads(my_response) ["answer"])` which reveals the student is likely handling the response from an API call outside of the displayed function definition." alt="image" data-base62-sha1="oSGFs53lVoOwkynOOjjV01McE7i" width="690" height="346" data-dominant-color="F1E8E8">image927×466 20.8 KB
