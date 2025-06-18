---
chunk_id: discourse_topic_168832_post_94_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168832/94
source_title: Remote Online Exam [TDS Jan 2025]
content_type: discourse
tokens: 281
username: Saransh_Saini
post_number: 94
topic_id: 168832
---

## Post #94 by Saransh_Saini

**Direct Link**: [Post #94](https://discourse.onlinedegree.iitm.ac.in/t/168832/94)

Hi @23f3002537

The problem is that, here you are sending headers unnecessary and overwriting the original headers. Moreover you were returning the text of the response instead of the json. Here is the revised version.

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
 response = await client.get(url)
 return response.json()
 except httpx.RequestError as e:
 raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")

if __name__ == "__main__":
 uvicorn.run(app, host="127.0.0.1", port=8000)
`
