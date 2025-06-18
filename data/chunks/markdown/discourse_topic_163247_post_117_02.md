---
chunk_id: discourse_topic_163247_post_117_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/117
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 355
username: 23f3002537
post_number: 117
topic_id: 163247
---

 a potential logical flaw or subtle difference from the expected outcome. The student has 7/9.5 points remaining with about 2 hours and 10 minutes left in the assessment. 2x" data-dominant-color="1A2020">image1915×999 143 KB

---

@carlton @Jivraj Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!

I m attaching my codes:

`from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"], 
 allow_credentials=True,
 allow_methods=["OPTION","POST"], 
 allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
 docs: List[str]
 query: str

def clean_text(text: str):
 """Clean text by lowering case, removing punctuation, and extra spaces."""
 text = text.lower() 
 text = re.sub(r'\s+', ' ', text) 
 text = re.sub(r'[^\w\s]', '', text) 
 return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
 try:
 cleaned_docs = [clean_text(doc) for doc in request.docs]
 cleaned_query = clean_text(request.query)

vectorizer = TfidfVectorizer()
 tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])
