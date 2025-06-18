---
chunk_id: course_vector_databases_001
source_url: https://tds.s-anand.net/#/vector-databases
source_title: vector-databases
content_type: course
tokens: 572
---

vec`](https://github.com/asg017/sqlite-vec).
- **[PostgreSQL](https://www.postgresql.org/)**: Supports vector search with [`pgvector`](https://github.com/pgvector/pgvector).

Take a look at this [Vector DB Comparison](https://superlinked.com/vector-db-comparison).

Watch this Vector Database Tutorial (3 min):

---

[**[Course Image: Vector databases are so hot right now. WTF are they? (3 min)]** This image is a thumbnail for a 3-minute video titled "Vector databases are so hot right now. WTF are they?". It frames the current landscape as a "Vector Database Race," implying a competitive environment among different vector database technologies. Students should understand that choosing the right vector database depends on specific project requirements and performance considerations. The visual style is humorous, aiming to make a potentially complex topic more engaging. This video likely provides a high-level overview and comparison of prominent vector database solutions.be video thumbnail from "The Code Report" titled "Vector Database Race," which provides a brief introduction to vector databases. The video aims to explain what vector databases are and their growing importance, emphasizing the competitive landscape within the field. Students can expect to gain a foundational understanding of vector databases, and their relevance in modern data management and machine learning workflows. The video serves as an introductory resource, setting the stage for learning about specific vector database solutions like ChromaDB, which is introduced later in the course material. This understanding is crucial before delving into practical applications and TDS projects involving vector databases.)](https://youtu.be/klTvEwg3oJ4)

### ChromaDB

Here's a minimal example using Chroma:

```python
# /// script
# requires-python = "==3.12"
# dependencies = [
# "chromadb",
# "sentence-transformers",
# ]
# ///

import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

async def setup_vector_db():
 """Initialize Chroma DB with an embedding function."""
 sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
 model_name="BAAI/bge-base-en-v1.5"
 )
 client = chromadb.PersistentClient(path="./vector_db")
 collection = client.create_collection(
 name="documents",
 embedding_function=sentence_transformer_ef
 )
 return collection

async def search_similar(collection, query: str, n_results: int = 3) -> list[dict]:
 """Search for documents similar to the query."""
 d = collection.query(query_texts=[query], n_results=n_results)
 return [
 {"id": id, "text": text, "distance": distance}
 for id, text, distance in zip(d["ids"][0], d["documents"][0], d["distances"][0])
 ]
