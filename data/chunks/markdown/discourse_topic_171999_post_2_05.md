---
chunk_id: discourse_topic_171999_post_2_05
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171999/2
source_title: Project 1 solution repository link
content_type: discourse
tokens: 175
username: carlton
post_number: 2
topic_id: 171999
---

_bash(code: str):
 """Execute bash code directly."""
 proc = await asyncio.create_subprocess_exec(
 "bash",
 stdin=asyncio.subprocess.PIPE,
 stdout=asyncio.subprocess.PIPE,
 stderr=asyncio.subprocess.PIPE,
 )
 stdout, stderr = await proc.communicate(code.encode())

---

if proc.returncode != 0:
 print(f"\n🔴 Bash execution failed:\n{stderr.decode()}")
 raise HTTPException(status_code=500, detail=f"Execution failed: {stderr.decode()}")

return {"stdout": stdout.decode(), "stderr": stderr.decode()}

@app.get("/")
async def read_root():
 """Serve the index.html file."""
 return FileResponse("static/index.html")

if __name__ == "__main__":
 import uvicorn

uvicorn.run(app, host="0.0.0.0", port=8000)
`
