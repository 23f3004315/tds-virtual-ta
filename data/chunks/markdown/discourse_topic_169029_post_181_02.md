---
chunk_id: discourse_topic_169029_post_181_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/181
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 355
username: Jivraj
post_number: 181
topic_id: 169029
---

pt-4o-mini` as the model.
The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
The second message must be **exactly** the text contained above.

---

This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.

**Note**: This uses a dummy `httpx` library, not the real one. You can only use:

`response = httpx.get(url, **kwargs)`
`response = httpx.post(url, json=None, **kwargs)`
`response.raise_for_status()`
`response.json()`

`
[quote="22f3000819, post:173, topic:169029"]
The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?
[/quote]

[quote="22f3000819, post:173, topic:169029"]
The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?
[/quote]

Full link will be part of question.`
