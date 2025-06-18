---
chunk_id: course_topic_modeling_000
source_url: https://tds.s-anand.net/#/topic-modeling
source_title: topic-modeling
content_type: course
tokens: 362
---

## Topic Modeling

[**[Course Image: LLM Topic Modeling]** Here's how to leverage text embeddings for topic modeling using OpenAI's API within a Google Colab notebook: First, you'll need to securely store your OpenAI API key using Colab's Secrets feature, allowing you to access it in your code without exposing it directly, using the `userdata.get('secretName')` function. Then, use the `requests` and `json` libraries in Python to make API calls, specifying the text to be embedded in the `input` field and the embedding model in the `model` field. The code demonstrates how to structure the API request with the appropriate headers (including your API key for authorization) and payload to obtain text embeddings from OpenAI, which can then be used for similarity analysis and topic extraction. The response contains the embeddings which will allow you to determine the topics within your data. text embeddings with the OpenAI API to perform topic modeling in a Google Colab environment. The first step is securely storing your OpenAI API key as a Colab secret for safe access, accomplished via the "Secrets" tab on the left-hand side. Next, the code uses the `requests` library to send a POST request to the OpenAI embeddings endpoint, with the API key passed in the authorization header. This code snippet showcases how to format the request with parameters like "input," "model," and "encoding_format" to generate embeddings for a given list of words. By obtaining embeddings, you can quantitatively analyze the semantic similarities between words and group them into topics for topic modeling.)](https://youtu.be/eQUNhq91DlI)

You'll learn to use text embeddings to find text similarity and use that to create topics automatically from text, covering:
