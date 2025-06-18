---
chunk_id: course_llm_text_extraction_000
source_url: https://tds.s-anand.net/#/llm-text-extraction
source_title: llm-text-extraction
content_type: course
tokens: 396
---

## LLM Text Extraction

[JSON](json.md) is one of the most widely used formats in the world for applications to exchange data.

[**[Course Image: LLM Extraction]** This instructional content focuses on extracting text using LLMs, specifically in a Colab notebook environment. It highlights storing sensitive information like API keys securely using the "Secrets" feature in Colab, showing configuration for LLMFOUNDRY, LLMPROXY_JW, and OPENAI_API_KEY. The code snippet demonstrates how to make a POST request to an API using stored credentials, parse the JSON response, and extract specific content from the LLM's output. It also shows an example of extracting address information, iterating through addresses, and updating items with the extracted details using a `get_address` function that makes use of `requests.post` to query an LLM API. This process is essential for automating data extraction tasks and using LLMs to process unstructured text.erived from the image, focusing on LLM text extraction.

To effectively utilize LLMs for text extraction, sensitive information like API keys are securely stored using a secrets management tool, as demonstrated with "LLMFOUNDRY," "LLMPROXY_JW," and "OPENAI_API_KE" within a Colab notebook. The Python code shows how to construct a request to the LLM API using the stored API key, and defines functions like 'get_address' to parse extracted data from the LLM's JSON response, specifically targeting address information. The example code iterates through a list of addresses and leverages the LLM to extract components such as state name, zip code, and country. Understanding API interactions, JSON parsing, and secure key management are key to successful LLM-based text extraction.)](https://youtu.be/72514uGffPE)

This video explains how to use LLMs to extract structure from unstructured data, covering:
