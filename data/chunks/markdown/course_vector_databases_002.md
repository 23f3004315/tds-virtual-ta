---
chunk_id: course_vector_databases_002
source_url: https://tds.s-anand.net/#/vector-databases
source_title: vector-databases
content_type: course
tokens: 552
---

3) -> list[dict]:
 """Search for documents similar to the query."""
 d = collection.query(query_texts=[query], n_results=n_results)
 return [
 {"id": id, "text": text, "distance": distance}
 for id, text, distance in zip(d["ids"][0], d["documents"][0], d["distances"][0])
 ]

---

async def main():
 collection = await setup_vector_db()

# Add some documents
 collection.add(
 documents=["Apple is a fruit", "Orange is citrus", "Computer is electronic"],
 ids=["1", "2", "3"]
 )

# Search
 results = await search_similar(collection, "fruit")
 print(results)

if __name__ == "__main__":
 import asyncio
 asyncio.run(main())
```

### LanceDB

Here's the same example using LanceDB:

```python
# /// script
# requires-python = "==3.12"
# dependencies = [
# "lancedb",
# "pyarrow",
# "sentence-transformers",
# ]
# ///

import lancedb
import pyarrow as pa
from sentence_transformers import SentenceTransformer

async def setup_vector_db():
 """Initialize LanceDB with an embedding function."""
 model = SentenceTransformer("BAAI/bge-base-en-v1.5")
 db = lancedb.connect("./vector_db")

# Create table with schema for documents
 table = db.create_table(
 "documents",
 schema=pa.schema([
 pa.field("id", pa.string()),
 pa.field("text", pa.string()),
 pa.field("vector", pa.list_(pa.float32(), list_size=768))
 ])
 )
 return table, model

async def search_similar(table, model, query: str, n_results: int = 3) -> list[dict]:
 """Search for documents similar to the query."""
 query_embedding = model.encode(query)
 results = table.search(query_embedding).limit(n_results).to_list()
 return [{"id": r["id"], "text": r["text"], "distance": float(r["_distance"])} for r in results]

async def main():
 table, model = await setup_vector_db()

# Add some documents
 documents = ["Apple is a fruit", "Orange is citrus", "Computer is electronic"]
 embeddings = model.encode(documents)

table.add(data=[
 {"id": str(i), "text": text, "vector": embedding}
 for i, (text, embedding) in enumerate(zip(documents, embeddings), 1)
 ])

# Search
 results = await search_similar(table, model, "fruit")
 print(results)

if __name__ == "__main__":
 import asyncio
 asyncio.run(main())
```

### DuckDB

Here's the same example using DuckDB:
