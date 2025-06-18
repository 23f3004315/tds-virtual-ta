---
chunk_id: course_function_calling_000
source_url: https://tds.s-anand.net/#/function-calling
source_title: function-calling
content_type: course
tokens: 485
---

## Function Calling with OpenAI

[Function Calling](https://platform.openai.com/docs/guides/function-calling) allows Large Language Models to convert natural language into structured function calls. This is perfect for building chatbots and AI assistants that need to interact with your backend systems.

OpenAI supports [Function Calling](https://platform.openai.com/docs/guides/function-calling) -- a way for LLMs to suggest what functions to call and how.

[**[Course Image: OpenAI Function Calling - Full Beginner Tutorial]** This image illustrates how to define a function schema for OpenAI's function calling feature, using a Python dictionary. Specifically, it shows the structure for a `get_flight_info` function, defining its `name`, `description`, and `parameters`. The `parameters` field specifies the input requirements, in this case, the `loc_origin` and `loc_destination`, both of which are defined as strings along with descriptive text like "airport, e.g. DUS". The "required" field confirms that both location parameters are necessary for the function to work, guiding the LLM to prompt the user if these aren't initially provided. Understanding this schema is crucial for leveraging function calling to connect LLMs to external tools and APIs within a TDS project.al aspect of function calling: defining function schemas. In the context of OpenAI's function calling feature, a function schema is a JSON-like structure that describes a function to the model, including its name, description, parameters, and the data types for those parameters. Specifically, the example shows a function called `get_flight_info`, designed to retrieve flight information between two locations, with the required parameters being the origin (`loc_origin`) and destination (`loc_destination`), both strings representing airport codes. Understanding how to properly define these schemas is crucial for guiding the language model to call the right functions with the appropriate information. Mastering function calling allows developers to extend the capabilities of language models by connecting them to external tools and data sources.)](https://youtu.be/aqdWSYWC_LI)

Here's a minimal example using Python and OpenAI's function calling that identifies the weather in a given location.

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
# "httpx",
# ]
# ///

import httpx
import os
from typing import Dict, Any
