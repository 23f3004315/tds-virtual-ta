---
chunk_id: course_vector_databases_000
source_url: https://tds.s-anand.net/#/vector-databases
source_title: vector-databases
content_type: course
tokens: 381
---

## Vector Databases

Vector databases are specialized databases that store and search vector embeddings efficiently.

Use vector databases when your embeddings exceed available memory or when you want it run fast at scale. (This is important. If your code runs fast and fits in memory, you **DON'T** need a vector database. You can can use `numpy` for these tasks.)

Vector databases are an evolving space.

The first generation of vector databases were written in C and typically used an algorithm called [HNSW](https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world) (a way to approximately find the nearest neighbor). Some popular ones are:

- **[Chroma](https://docs.trychroma.com/)**: Combines a vector index with a SQLite database. Easy to install, most popular.
- **[LanceDB](https://lancedb.github.io/lancedb/)**: Written in Rust. Faster, easy to install, growing popular.
- **[FAISS](https://github.com/facebookresearch/faiss)**: Meta's lightweight library
- **[Milvus](https://milvus.io/)**: Distributed, cloud-native

In addition, most relational databases now support vector search. For example:

- **[DuckDB](https://duckdb.org/)**: Supports vector search with [`vss`](https://duckdb.org/docs/extensions/vss.html).
- **[SQLite](https://www.sqlite.org/)**: Supports vector search with [`sqlite-vec`](https://github.com/asg017/sqlite-vec).
- **[PostgreSQL](https://www.postgresql.org/)**: Supports vector search with [`pgvector`](https://github.com/pgvector/pgvector).

Take a look at this [Vector DB Comparison](https://superlinked.com/vector-db-comparison).

Watch this Vector Database Tutorial (3 min):
