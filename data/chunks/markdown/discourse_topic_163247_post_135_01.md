---
chunk_id: discourse_topic_163247_post_135_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/135
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 361
username: Sakshi6479
post_number: 135
topic_id: 163247
---

iddleware(
 CORSMiddleware,
 allow_origins=["http://localhost:3000"], # Allow only this specific origin
 allow_credentials=True,
 allow_methods=["POST", "OPTIONS"], # Allow only POST and OPTIONS methods
 allow_headers=["Content-Type", "Authorization"], # Allow only specific headers
)

---

# OpenAI API key (use your own key)
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDY3NDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tMJtqZrzRqREY7E3wsFMd9PkElXEbRBpCkb533ORGEU'

# Request body model for /similarity endpoint
class SimilarityRequest(BaseModel):
 docs: List[str]
 query: str

# Function to get embeddings (using OpenAI API)
def get_embedding(text: str):
 response = openai.Embedding.create(
 model="text-embedding-ada-003", # Use the correct model
 input=text
 )
 return response['data'][0]['embedding']

# POST /similarity endpoint
@app.post("/similarity")
async def similarity(request: SimilarityRequest):
 docs = request.docs
 query = request.query
 query_embedding = get_embedding(query)
 doc_embeddings = [get_embedding(doc) for doc in docs]
 
 # Cosine similarity
 similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
 ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]
 
 return JSONResponse(content={"matches": ranked_docs[:3]})
