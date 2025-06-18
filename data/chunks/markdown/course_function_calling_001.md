---
chunk_id: course_function_calling_001
source_url: https://tds.s-anand.net/#/function-calling
source_title: function-calling
content_type: course
tokens: 579
---

.be/aqdWSYWC_LI)

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

---

def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
 response = httpx.post(
 "https://api.openai.com/v1/chat/completions",
 headers={
 "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
 "Content-Type": "application/json",
 },
 json={
 "model": "gpt-4o-mini",
 "messages": [{"role": "user", "content": user_input}],
 "tools": tools,
 "tool_choice": "auto",
 },
 )
 return response.json()["choices"][0]["message"]

WEATHER_TOOL = {
 "type": "function",
 "function": {
 "name": "get_weather",
 "description": "Get the current weather for a location",
 "parameters": {
 "type": "object",
 "properties": {
 "location": {"type": "string", "description": "City name or coordinates"}
 },
 "required": ["location"],
 "additionalProperties": False,
 },
 "strict": True,
 },
}

if __name__ == "__main__":
 response = query_gpt("What is the weather in San Francisco?", [WEATHER_TOOL])
 print([tool_call["function"] for tool_call in response["tool_calls"]])
```

### How to define functions

The function definition is a [JSON schema](https://json-schema.org/) with a few OpenAI specific properties.
See the [Supported schemas](https://platform.openai.com/docs/guides/structured-outputs#supported-schemas).

Here's an example of a function definition for scheduling a meeting:

```python
MEETING_TOOL = {
 "type": "function",
 "function": {
 "name": "schedule_meeting",
 "description": "Schedule a meeting room for a specific date and time",
 "parameters": {
 "type": "object",
 "properties": {
 "date": {
 "type": "string",
 "description": "Meeting date in YYYY-MM-DD format"
 },
 "time": {
 "type": "string",
 "description": "Meeting time in HH:MM format"
 },
 "meeting_room": {
 "type": "string",
 "description": "Name of the meeting room"
 }
 },
 "required": ["date", "time", "meeting_room"],
 "additionalProperties": False
 },
 "strict": True
 }
}
```

### How to define multiple functions

You can define multiple functions by passing a list of function definitions to the `tools` parameter.
