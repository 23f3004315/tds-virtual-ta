---
chunk_id: course_parsing_json_002
source_url: https://tds.s-anand.net/#/parsing-json
source_title: parsing-json
content_type: course
tokens: 535
---

 {id, name}'

# Transform JSON structure
cat data.json | jq '.items[] | {name: .name, count: .details.count}'

# Filter and aggregate
cat events.jsonl | jq -s 'group_by(.category) | map({category: .[0].category, count: length})'
```

### JMESPath Queries

---

[JMESPath](https://jmespath.org/) offers a declarative query language to extract and transform data from nested JSON structures without needing verbose code. It's a neat alternative when you want to quickly pull out specific values or filter collections based on conditions.

**Example:** Extracting user emails or filtering out inactive records from a complex JSON payload received from a cloud service.

```python
import jmespath

# Example queries
data = {
 "locations": [
 {"name": "Seattle", "state": "WA", "info": {"population": 737015}},
 {"name": "Portland", "state": "OR", "info": {"population": 652503}}
 ]
}

# Find all cities with population > 700000
cities = jmespath.search("locations[?info.population > `700000`].name", data)
```

### Streaming with ijson

Loading huge JSON files all at once can quickly exhaust system memory. [ijson](https://ijson.readthedocs.io/en/latest/) lets you stream and process JSON incrementally. This method is ideal when your JSON file is too large or when you only need to work with part of the data.

**Example:** Processing a continuous feed from an API that returns a large JSON array, such as sensor data or event logs, while filtering on the fly.

```python
import ijson

async def process_large_json(filepath: str) -> list:
 """Process a large JSON file without loading it entirely into memory."""
 results = []

with open(filepath, 'rb') as file:
 # Stream objects under the 'items' key
 parser = ijson.items(file, 'items.item')
 async for item in parser:
 if item['value'] > 100: # Process conditionally
 results.append(item)

return results
```

### Pandas JSON Columns

[Pandas](https://pandas.pydata.org/) makes it easy to work with tabular data that includes JSON strings. When you receive API data where one column holds nested JSON, flattening these structures lets you analyze and visualize the data using familiar DataFrame operations.

**Example:** Flattening customer records stored as nested JSON in a CSV file to extract demographic details and spending patterns.

```python
import pandas as pd
