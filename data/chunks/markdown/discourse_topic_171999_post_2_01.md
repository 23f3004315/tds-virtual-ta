---
chunk_id: discourse_topic_171999_post_2_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171999/2
source_title: Project 1 solution repository link
content_type: discourse
tokens: 239
username: carlton
post_number: 2
topic_id: 171999
---

.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import httpx
import re
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

token = os.environ["LLMFOUNDRY_TOKEN"]

---

async def llm(system_prompt: str, user_prompt: str) -&gt; str:
 """Call GPT-4o-Mini via AI Proxy."""
 async with httpx.AsyncClient(timeout=30.0) as client:
 response = await client.post(
 "https://llmfoundry.straive.com/v1/chat/completions",
 headers={"Authorization": f"Bearer {token}"},
 json={
 "model": "gpt-4o-mini",
 "messages": [
 {"role": "system", "content": system_prompt},
 {"role": "user", "content": user_prompt},
 ],
 },
 )
 response.raise_for_status()
 return response.json()["choices"][0]["message"]["content"]

system_prompt = """The user will provide a task description.
Write one or more `bash` or `python` scripts to execute the task.

CODING RULES:
