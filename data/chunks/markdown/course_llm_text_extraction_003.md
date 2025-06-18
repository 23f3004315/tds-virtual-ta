---
chunk_id: course_llm_text_extraction_003
source_url: https://tds.s-anand.net/#/llm-text-extraction
source_title: llm-text-extraction
content_type: course
tokens: 467
---

 "output"],
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

---

- `"type": "json_schema"`: We want you to generate a JSON response that follows this schema.
- `"json_schema":`: We're going to give you a schema.
 - `"name": "math_response"`: The schema is called `math_response`. (We can call it anything.)
 - `"strict": true`: Follow the schema exactly.
 - `"schema":`: Now, here's the actual JSON schema.
 - `"type": "object"`: Return an object. ⚠️ The root object **must** be an object.
 - `"properties":`: The object has these properties:
 - `"steps":`: There's a `steps` property.
 - `"type": "array"`: It's an array.
 - `"items":`: Each item in the array...
 - `"type": "object"`: ... is an object.
 - `"properties":`: The object has these properties:
 - `"explanation":`: There's an `explanation` property.
 - `"type": "string"`: ... which is a string.
 - `"output":`: There's an `output` property.
 - `"type": "string"`: ... which is a string, too.
 - `"required": ["explanation", "output"]`: ⚠️ You **must** add `"required": [...]` and include **all** fields int he object.
 - `"additionalProperties": false`: ⚠️ OpenAI requires every object to have `"additionalProperties": false`.
 - `"final_answer":`: There's a `final_answer` property.
 - `"type": "string"`: ... which is a string.
 - `"required": ["steps", "final_answer"]`: ⚠️ You **must** add `"required": [...]` and include **all** fields in the object.
 - `"additionalProperties": false`: ⚠️ OpenAI requires every object to have `"additionalProperties": false`.
