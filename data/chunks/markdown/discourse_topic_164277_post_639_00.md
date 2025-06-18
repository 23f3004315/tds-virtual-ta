---
chunk_id: discourse_topic_164277_post_639_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/639
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 290
username: carlton
post_number: 639
topic_id: 164277
---

## Post #639 by carlton

**Direct Link**: [Post #639](https://discourse.onlinedegree.iitm.ac.in/t/164277/639)

Sakshi6479:
[Quote]: 
`{
 "type": "json",
 "json_schema": {
 "name": "taks_runner",
 "schema": {
 "type": "object",
 "required": ["python_dependencies","python_code"],
 "properties": {
 "python_code": {
 "type": "string",
 "description": "Python code to perform the task"
 },
 "python_dependencies": {
 "type": "array",
 "items": {
 "type": "object",
 "properties": {
 "module": {
 "type": "string",
 "description": "Name of the python module"
 }
 },
 "required": ["module"],
 "additionalProperties": False
 }
 }
 }
 }
}
}
`

It clearly says in your error message:

Invalid value: ‘json’

if you look at the “type” key in your response_format variable at the top,

the value cannot be “json”

The error is telling you what the supported values are

‘json_object’, ‘json_schema’, and ‘text’

Since you are defining a schema the correct value should be ‘json_schema’

So therefore you should change

`"type": "json"
`
to

`"type": "json_schema"
`
If you have trouble constructing Json schemas,
