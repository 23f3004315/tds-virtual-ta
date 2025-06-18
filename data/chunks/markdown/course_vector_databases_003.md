---
chunk_id: course_vector_databases_003
source_url: https://tds.s-anand.net/#/vector-databases
source_title: vector-databases
content_type: course
tokens: 579
---

, "vector": embedding}
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

---

```python
# /// script
# requires-python = "==3.12"
# dependencies = [
# "duckdb",
# "sentence-transformers",
# ]
# ///

import duckdb
from sentence_transformers import SentenceTransformer

async def setup_vector_db() -> tuple[duckdb.DuckDBPyConnection, SentenceTransformer]:
 """Initialize DuckDB with VSS extension and embedding model."""
 # Initialize model
 model = SentenceTransformer("BAAI/bge-base-en-v1.5")
 vector_dim = model.get_sentence_embedding_dimension()

# Setup DuckDB with VSS extension
 conn = duckdb.connect(":memory:")
 conn.install_extension("vss")
 conn.load_extension("vss")

# Create table with vector column
 conn.execute(f"""
 CREATE TABLE documents (
 id VARCHAR,
 text VARCHAR,
 vector FLOAT[{vector_dim}]
 )
 """)

# Create HNSW index for vector similarity search
 conn.execute("CREATE INDEX vector_idx ON documents USING HNSW (vector)")
 return conn, model

async def search_similar(conn: duckdb.DuckDBPyConnection, model: SentenceTransformer,
 query: str, n_results: int = 3) -> list[dict]:
 """Search for documents similar to query using vector similarity."""
 # Encode query to vector
 query_vector = model.encode(query).tolist()

# Search using HNSW index with explicit FLOAT[] cast
 results = conn.execute("""
 SELECT id, text, array_distance(vector, CAST(? AS FLOAT[768])) as distance
 FROM documents
 ORDER BY array_distance(vector, CAST(? AS FLOAT[768]))
 LIMIT ?
 """, [query_vector, query_vector, n_results]).fetchall()

return [{"id": r[0], "text": r[1], "distance": float(r[2])} for r in results]

async def main():
 conn, model = await setup_vector_db()

# Add sample documents
 documents = ["Apple is a fruit", "Orange is citrus", "Computer is electronic"]
 embeddings = model.encode(documents).tolist()

# Insert documents and vectors
 conn.executemany("""
 INSERT INTO documents (id, text, vector)
 VALUES (?, ?, ?)
 """, [(str(i), text, embedding)
 for i, (text, embedding) in enumerate(zip(documents, embeddings), 1)])

# Search similar documents
 results = await search_similar(conn, model, "fruit")
 print(results)

if __name__ == "__main__":
 import asyncio
 asyncio.run(main())
```
