---
chunk_id: discourse_topic_164277_post_638_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/638
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 331
username: Sakshi6479
post_number: 638
topic_id: 164277
---

 "type": "array",
 "items": {
 "type": "object",
 "properties": {
 "module": {
 "type": "string",
 "description": "Name of the python module"
 }
 },
 "required": ["module"],
 "additionalProperties": False
 }
 }
 }
 }
}
}

---

primary_prompt = """
 You are an automated agent, so generate python code that does the specified task.
 Assume that uv and python are pre-installed.
 Assume that code you generate will be executed inside a docker container.
 Inorder to perform any task if some python package is required to install, provide name of those modules. 
"""

app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["GET", "POST"],
 allow_headers=["*"],
)

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
headers = {
 "Content-Type": "application/json",
 "Authorization": f"Bearer {AIPROXY_TOKEN}"
}

@app.get("/")
def home():
 return {"welcome to the task runner"}
@app.post("/run")
def task_runnner(task: str):
 url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
 data = {
 "model": "gpt-4o-mini", 
 "messages": [
 {
 "role": "user", 
 "content": task
 },
 {
 "role": "system",
 "content": f"""{primary_prompt}"""
 }
 ],
 "response_format": response_format
 }

response = requests.post(url=url, headers=headers, json=data)
 r = response.json()

return r
