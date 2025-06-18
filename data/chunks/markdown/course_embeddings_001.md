---
chunk_id: course_embeddings_001
source_url: https://tds.s-anand.net/#/embeddings
source_title: embeddings
content_type: course
tokens: 567
---

 numbers in the array. Smaller dimensions are cheaper to store.
4. **Max Tokens**. Higher is better. This is the number of input tokens (words) the model can take in a _single_ input.
5. Look for higher scores in the columns for Classification, Clustering, Summarization, etc. based on your needs.

### Local Embeddings

---

[**[Course Image: Guide to Local Embeddings with Sentence Transformers]** This image introduces the concept of text embeddings and their application in semantic search, likely using sentence transformers. Text embeddings transform words or sentences into numerical vectors that capture their semantic meaning. Semantic search utilizes these embeddings to find results based on the meaning of a query, rather than just keyword matching. This method allows for more accurate and relevant search results by understanding the context and relationships between words. Understanding how to generate and utilize embeddings is crucial for various NLP tasks, enabling applications like document retrieval, question answering, and similarity analysis.ncept of text embeddings and their application in semantic search, which is a method of searching based on the meaning of words rather than exact matches. Text embeddings involve transforming text into numerical vectors that capture the semantic relationships between words and phrases, allowing you to perform similarity comparisons. The video, featuring Lewis, likely delves into how text embeddings enable more intuitive and context-aware search functionalities. Understanding this will help in TDS projects where you need to find relevant information based on the meaning of the query, rather than simple keyword matching. Using these embeddings, systems can identify documents with similar meanings, even if they don't share the same keywords.)](https://youtu.be/OATCgQtNX2o)

Here's a minimal example using a local embedding model:

```python
# /// script
# requires-python = "==3.12"
# dependencies = [
# "sentence-transformers",
# "httpx",
# "numpy",
# ]
# ///

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('BAAI/bge-base-en-v1.5') # A small, high quality model

async def embed(text: str) -> list[float]:
 """Get embedding vector for text using local model."""
 return model.encode(text).tolist()

async def get_similarity(text1: str, text2: str) -> float:
 """Calculate cosine similarity between two texts."""
 emb1 = np.array(await embed(text1))
 emb2 = np.array(await embed(text2))
 return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))

async def main():
 print(await get_similarity("Apple", "Orange"))
 print(await get_similarity("Apple", "Lightning"))

if __name__ == "__main__":
 import asyncio
 asyncio.run(main())
```
