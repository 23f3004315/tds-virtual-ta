---
chunk_id: discourse_topic_171999_post_2_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171999/2
source_title: Project 1 solution repository link
content_type: discourse
tokens: 342
username: carlton
post_number: 2
topic_id: 171999
---

 == "python":
 result = await execute_python(code)
 else: # bash
 result = await execute_bash(code)
 results.append({"lang": language, **result})

print(f"\n🟡 Results:\n{results}\n")
 return {"response": response, "results": results}

---

@app.get("/read")
async def read_file(path: str):
 """Read contents of a file."""
 # Validate path is within /data
 path = os.path.normpath(path)
 if not path.startswith("/data/"):
 raise HTTPException(status_code=400, detail="Invalid path")
 if not os.path.exists(path):
 raise HTTPException(status_code=404, detail="File not found")
 return FileResponse(path)

@app.post("/execute/python")
async def execute_python(code: str):
 """Execute Python code directly."""
 proc = await asyncio.create_subprocess_exec(
 "python3",
 "-",
 stdin=asyncio.subprocess.PIPE,
 stdout=asyncio.subprocess.PIPE,
 stderr=asyncio.subprocess.PIPE,
 )
 stdout, stderr = await proc.communicate(code.encode())

if proc.returncode != 0:
 print(f"\n🔴 Python execution failed:\n{stderr.decode()}")
 raise HTTPException(status_code=500, detail=f"Execution failed: {stderr.decode()}")

return {"stdout": stdout.decode(), "stderr": stderr.decode()}

@app.post("/execute/bash")
async def execute_bash(code: str):
 """Execute bash code directly."""
 proc = await asyncio.create_subprocess_exec(
 "bash",
 stdin=asyncio.subprocess.PIPE,
 stdout=asyncio.subprocess.PIPE,
 stderr=asyncio.subprocess.PIPE,
 )
 stdout, stderr = await proc.communicate(code.encode())
