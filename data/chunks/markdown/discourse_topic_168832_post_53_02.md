---
chunk_id: discourse_topic_168832_post_53_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168832/53
source_title: Remote Online Exam [TDS Jan 2025]
content_type: discourse
tokens: 296
username: 23f3002537
post_number: 53
topic_id: 168832
---

 issue with an earlier request. The core confusion is the discrepancy between the successful data retrieval in Thunder Client and the "Incorrect response" error shown within the exam interface. 2x" data-dominant-color="1E2424">Screenshot (92)1920×1080 352 KB

---

@carlton @Saransh_Saini Sir, can you please tell me why this was not accepted? here is my code:

`from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uvicorn

app = FastAPI()

# Add CORS middleware to handle preflight OPTIONS requests
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

@app.get("/api")
async def proxy(url: str, request: Request):
 headers = {key: value for key, value in request.headers.items() if key.lower() != "host"}
 try:
 async with httpx.AsyncClient() as client:
 response = await client.get(url, headers=headers)
 return response.text
 except httpx.RequestError as e:
 raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")

if __name__ == "__main__":
 uvicorn.run(app, host="127.0.0.1", port=8000)
`
here are the responses:
