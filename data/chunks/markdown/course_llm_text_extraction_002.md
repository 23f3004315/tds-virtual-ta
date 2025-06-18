---
chunk_id: course_llm_text_extraction_002
source_url: https://tds.s-anand.net/#/llm-text-extraction
source_title: llm-text-extraction
content_type: course
tokens: 368
---

](https://platform.openai.com/docs/guides/function-calling)

Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied
[JSON Schema](https://json-schema.org/overview/what-is-jsonschema), so you don't need to worry about the model omitting a required key,
or hallucinating an invalid enum value.

---

```bash
curl https://api.openai.com/v1/chat/completions \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gpt-4o-2024-08-06",
 "messages": [
 { "role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step." },
 { "role": "user", "content": "how can I solve 8x + 7 = -23" }
 ],
 "response_format": {
 "type": "json_schema",
 "json_schema": {
 "name": "math_response",
 "strict": true
 "schema": {
 "type": "object",
 "properties": {
 "steps": {
 "type": "array",
 "items": {
 "type": "object",
 "properties": { "explanation": { "type": "string" }, "output": { "type": "string" } },
 "required": ["explanation", "output"],
 "additionalProperties": false
 }
 },
 "final_answer": { "type": "string" }
 },
 "required": ["steps", "final_answer"],
 "additionalProperties": false
 }
 }
 }
}'
```

Here's what the `response_format` tells OpenAI. The items marked ⚠️ are OpenAI specific requirements for the JSON schema.
