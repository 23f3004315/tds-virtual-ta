---
chunk_id: discourse_topic_169029_post_157_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/157
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 466
username: lakshaygarg654
post_number: 157
topic_id: 169029
---

](https://discourse.onlinedegree.iitm.ac.in/t/169029/157)

@carlton

I am bit confused about answer evaluation process. Can you tell which one is correct process.

1st process ( I used json.dumps() to get my_response as json formatted string)

---

**[Discussion Image by lakshaygarg654]** This image depicts a student sharing a code snippet and its output in the TDS "Project 2 - TDS Solver" discussion thread, demonstrating how to correctly parse a JSON response to extract the value associated with the "answer" key. The Python code first imports the `json` library, then defines a string `my_response` containing a JSON object with a key-value pair: `"answer": "26272"`. The core of the example lies in the `print` statement, where `json.loads(my_response)` converts the JSON string into a Python dictionary, and then `["answer"]` accesses the value associated with the key "answer". The correct extraction and printing of the string "26272" to the console confirms that the student successfully parsed the JSON response and accessed the desired value, showcasing a fundamental technique for handling API responses or data in JSON format within their TDS solver project. This demonstrates understanding of JSON parsing in Python and specifically how to extract data nested within a JSON structure.ts the `json` library, defines a string variable `my_response` containing a JSON string where the key "answer" has the value "26272". Subsequently, it uses `json.loads()` to parse the JSON string into a Python dictionary and then accesses the value associated with the key "answer" to print it to the console. The displayed output after running the code is "26272", indicating successful extraction of the desired value from the JSON string. This example likely serves as a simple illustration of how to handle JSON responses, potentially in the context of the TDS solver project, and hints at a question or solution related to parsing JSON data." alt="image" data-base62-sha1="pvtuUeKF4UrJMTad3XVQkLGmjxy" width="517" height="159" data-dominant-color="F5F4F4">image726×224 4.68 KB
