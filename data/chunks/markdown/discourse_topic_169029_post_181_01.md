---
chunk_id: discourse_topic_169029_post_181_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/181
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 326
username: Jivraj
post_number: 181
topic_id: 169029
---

, Q7 - Create a GitHub action, Q8 - Push an Image to Docker Hub: Similar to GA1 Q13, these too have my email or roll number as parameter. These too **WILL NOT** be checked against any other email, right?

Same answer as Q13 GA1

---

22f3000819:
[Quote]: 
Can you please give an example of how questions of this GA will be sent in the request, especially any of Q1 or Q2 or Q5 or Q6 or Q7 or Q8 which have code-blocks containing text crucial to the question? I just want to decide whether regex or function-calling would be more appropriate her

We will take Q1 in this format, which is just copy pasting from portal```

One of the test cases involves sending a sample piece of meaningless text:

`au7BK3 33 H 5 lKz6y4n oQmbgoX 0 hNW3JH 68Q1u
`
Write a Python program that uses `httpx` to send a POST request to OpenAI’s API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:

Make sure you pass an Authorization header with dummy API key.
Use `gpt-4o-mini` as the model.
The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
The second message must be **exactly** the text contained above.
