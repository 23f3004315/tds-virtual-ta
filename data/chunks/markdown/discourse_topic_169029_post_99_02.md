---
chunk_id: discourse_topic_169029_post_99_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/99
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 334
username: 23f2003751
post_number: 99
topic_id: 169029
---

\",\"age\":92},{\"name\":\"Henry\",\"age\":94},{\"name\":\"Mary\",\"age\":97}]"
 }
`
Is it ok for GA 1 Question 9 answer output to look like this because it matches with the answer just it has the extra back slash…What should i do

---

`def sort_json_array(json_array: str, sort_keys: list) -&gt; str:
 """
 Sort a JSON array based on specified criteria

Args:
 json_array: JSON array as a string
 sort_keys: List of keys to sort by

Returns:
 Sorted JSON array as a string
 """
 try:
 # Parse the JSON array
 data = json.loads(json_array)

# Sort the data based on the specified keys
 for key in reversed(sort_keys):
 data = sorted(data, key=lambda x: x.get(key, ""))

# Return the sorted JSON as a string without whitespace
 return json.dumps(data, separators=(",", ":"))

except Exception as e:
 return f"Error sorting JSON array: {str(e)}"
`
`{
 "type": "function",
 "function": {
 "name": "sort_json_array",
 "description": "Sort a JSON array based on specified criteria",
 "parameters": {
 "type": "object",
 "properties": {
 "json_array": {
 "type": "string",
 "description": "JSON array to sort",
 },
 "sort_keys": {
 "type": "array",
 "items": {"type": "string"},
 "description": "List of keys to sort by",
 },
 },
 "required": ["json_array", "sort_keys"],
 },
 },
 },
`
@carlton @Jivraj
