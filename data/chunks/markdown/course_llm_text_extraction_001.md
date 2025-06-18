---
chunk_id: course_llm_text_extraction_001
source_url: https://tds.s-anand.net/#/llm-text-extraction
source_title: llm-text-extraction
content_type: course
tokens: 362
---

 of addresses and leverages the LLM to extract components such as state name, zip code, and country. Understanding API interactions, JSON parsing, and secure key management are key to successful LLM-based text extraction.)](https://youtu.be/72514uGffPE)

This video explains how to use LLMs to extract structure from unstructured data, covering:

---

- **LLM for Data Extraction**: Use OpenAI's API to extract structured information from unstructured data like addresses.
- **JSON Schema**: Define a JSON schema to ensure consistent and structured output from the LLM.
- **Prompt Engineering**: Craft effective prompts to guide the LLM's response and improve accuracy.
- **Data Cleaning**: Use string functions and OpenAI's API to clean and standardize data.
- **Data Analysis**: Analyze extracted data using Pandas to gain insights.
- **LLM Limitations**: Understand the limitations of LLMs, including potential errors and inconsistencies in output.
- **Production Use Cases**: Explore real-world applications of LLMs for data extraction, such as customer service email analysis.

Here are the links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1Z8mG-RPTSYY4qwkoNdzRTc4StbnwOXeE)
- [JSON Schema](https://json-schema.org/)
- [Function calling](https://platform.openai.com/docs/guides/function-calling)

Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied
[JSON Schema](https://json-schema.org/overview/what-is-jsonschema), so you don't need to worry about the model omitting a required key,
or hallucinating an invalid enum value.
