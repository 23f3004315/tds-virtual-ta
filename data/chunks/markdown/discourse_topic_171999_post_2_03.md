---
chunk_id: discourse_topic_171999_post_2_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171999/2
source_title: Project 1 solution repository link
content_type: discourse
tokens: 342
username: carlton
post_number: 2
topic_id: 171999
---

 this JSON body:
 {
 model: "text-embedding-3-small",
 input: [array of strings],
 }
 Embeddings are in response.data[*].embedding - an array of floats.
 Calculate the dot product of the embeddings (skipping the diagonal) to find the most similar pair of strings.

---

client.post(
 f"{openai_api_base}/embeddings",
 headers={"Authorization": f"Bearer {openai_api_key}"},
 json={"model": "text-embedding-3-small", "input": data},
 )
- When extracting card information, use the system prompt "Extract the EXACT dummy credit card number from this test image"

EXECUTION RULES: An automated agent will blindly run the scripts you provide. So ONLY
write the FINAL script(s) to run in ```bash or ```python code fences.
"""

@app.post("/run")
async def run_task(task: str):
 """Execute a plain-English automation task."""
 response = await llm(system_prompt, task)
 print(f"\n🟡 Running task:\n{task.strip()}\n")
 print(f"\n🟡 {response}\n")

results = []
 for language, code in re.findall(r"```(python|bash)\n(.*?)\n```", response, re.DOTALL):
 print(f"\n🟡 Running {language} code:\n{code}\n")
 if language == "python":
 result = await execute_python(code)
 else: # bash
 result = await execute_bash(code)
 results.append({"lang": language, **result})

print(f"\n🟡 Results:\n{results}\n")
 return {"response": response, "results": results}
