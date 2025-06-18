---
chunk_id: course_embeddings_002
source_url: https://tds.s-anand.net/#/embeddings
source_title: embeddings
content_type: course
tokens: 276
---

.array(await embed(text2))
 return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))

async def main():
 print(await get_similarity("Apple", "Orange"))
 print(await get_similarity("Apple", "Lightning"))

if __name__ == "__main__":
 import asyncio
 asyncio.run(main())
```

---

Note the `get_similarity` function. It uses a [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) to calculate the similarity between two embeddings.

### OpenAI Embeddings

For comparison, here's how to use OpenAI's API with direct HTTP calls. Replace the `embed` function in the earlier script:

```python
import os
import httpx

async def embed(text: str) -> list[float]:
 """Get embedding vector for text using OpenAI's API."""
 async with httpx.AsyncClient() as client:
 response = await client.post(
 "https://api.openai.com/v1/embeddings",
 headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
 json={"model": "text-embedding-3-small", "input": text}
 )
 return response.json()["data"][0]["embedding"]
```

**NOTE**: You need to set the `OPENAI_API_KEY` environment variable for this to work.
