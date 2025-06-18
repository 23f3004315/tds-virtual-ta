---
chunk_id: discourse_topic_163247_post_138_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/138
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 211
username: sha_512_av
post_number: 138
topic_id: 163247
---

 the API endpoint and confirming its basic functionality. The student has configured the Auth Type to "No Auth" and is viewing the response body in JSON format. 2x" data-dominant-color="242425">Screenshot_20250204_032923991×615 43.7 KB

---

I had used (well gpt) the below two decorators to format:

`class SearchRequest(BaseModel):
 docs: List[str] # The list of documents to search through
 query: str # The search query string

class SearchResponse(BaseModel):
 matches: List[str] # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)

.........

return SearchResponse(matches=sorted_matches[:3])
`
It basically checks the Request and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that
