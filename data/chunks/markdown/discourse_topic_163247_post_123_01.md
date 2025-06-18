---
chunk_id: discourse_topic_163247_post_123_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/123
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 212
username: Sudhishnarayan
post_number: 123
topic_id: 163247
---

 = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], # Allows all origins
 allow_credentials=True,
 allow_methods=["OPTIONS", "POST"], # Allows all methods (GET, POST, OPTIONS, etc.)
 allow_headers=["*"], # Allows all headers
)

---

class similarity1(BaseModel):
 docs: list[str]
 query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
 docs = similarity1.docs
 query = similarity1.query
 results_docs = model.encode(docs)
 results_query = model.encode(query)
 similarities = {}
 output = []
 for i in range(len(results_docs)):
 c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
 similarities[c] = docs[i]
 k = sorted(list(similarities.keys()))
 for i in k[::-1][:3]:
 output.append(similarities[i])
 return {"matches" : output}
if __name__ == "__main__":
 (uvicorn.run(app))

`
