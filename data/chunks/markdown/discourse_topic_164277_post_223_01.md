---
chunk_id: discourse_topic_164277_post_223_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/223
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 348
username: 22f3002771
post_number: 223
topic_id: 164277
---

&gt; float:
 # """Calculate cosine similarity between two texts."""
 # emb1 = await embed(text1)
 # emb2 = await embed(text2)
 return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))

---

# async def embed_list(text_list: list[str]) -&gt; list[float]:
async def embed_list(text_list: list[str]) -&gt; list[float]:
 OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
 OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"
 """Get embedding vector for text using OpenAI's API."""
 try:
 async with httpx.AsyncClient() as client:
 # with httpx.AsyncClient() as client:
 response = await client.post(
 # response = httpx.post(
 OPENAI_API_URL,
 headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
 
 json={"model": "text-embedding-3-small", "input": text_list},
 )
 # print(f'{response.json()["data"][0]["embedding"]}')
 emb_list = [emb["embedding"] for emb in response.json()["data"]]
 print(f"Number of embeddings returned = {len(emb_list)}")
 return emb_list

except KeyError as e:
 print(f"INSIDE EMBED_LIST IN A9. KeyError occurred while querying GPT: {e}")
 raise HTTPException(status_code=400, detail=str(e))

except Exception as e:
 print(f"INSIDE EMBED_LIST IN A9. General Error while querying gpt: {str(e)}")
 raise HTTPException(status_code=500, detail=str(e))
