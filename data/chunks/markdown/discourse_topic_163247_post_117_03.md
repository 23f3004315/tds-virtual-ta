---
chunk_id: discourse_topic_163247_post_117_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/117
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 180
username: 23f3002537
post_number: 117
topic_id: 163247
---

async def find_similar_docs(request: SimilarityRequest):
 try:
 cleaned_docs = [clean_text(doc) for doc in request.docs]
 cleaned_query = clean_text(request.query)

vectorizer = TfidfVectorizer()
 tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

---

query_vector = tfidf_matrix[-1]
 doc_vectors = tfidf_matrix[:-1]
 similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
 matched_docs = [request.docs[i] for i in top_indices]

return {"matches": matched_docs}

except Exception as e:
 raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
 return {"message": f"Executing query: {q}"}

`
