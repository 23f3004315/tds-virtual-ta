---
chunk_id: discourse_topic_167172_post_1_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/1
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 247
username: Sakshi6479
post_number: 1
topic_id: 167172
---

additionalProperties": False
 },
 "strict": True
 },
}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]

---

def query_gpt(user_input: str, tools: list[dict] = tools) -&gt; dict:
 response = requests.post(
 url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
 headers={
 "Content-Type": "application/json",
 "Authorization": f"Bearer {AIPROXY_TOKEN}"
 },
 json={
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "user",
 "content": user_input
 }
 ],
 "tools": tools,
 "tool_choice": "auto"
 }
 )
 return response.json()

@app.get("/")
def home():
 return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
 try:
 with open(path, "r") as f:
 return f.read()
 except Exception as e:
 raise HTTPException(status_code=404, detail="File does not exist")
