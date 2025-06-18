---
chunk_id: discourse_topic_164277_post_138_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/138
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 240
username: Adithya
post_number: 138
topic_id: 164277
---

ier@3.4.2", "--write", filepath],
 check=False, # Don't raise exception automatically
 capture_output=True,
 text=True
 )

if result.returncode != 0:
 return {"success": False, "message": f"Prettier write failed: {result.stderr}"}

---

if verify_prettier_formatting(filepath):
 return {"success": True, "message": "Formatted and verified successfully!"}
 else:
 logging.info("Verification failed. Retrying formatting...") #Log the retry
 # If verification fails, the loop continues and prettier --write is executed again.

except Exception as e:
 return {"success": False, "message": str(e)}

def verify_prettier_formatting(filepath):
 try:
 subprocess.run(["npx", "prettier@3.4.2", "--check", filepath], check=True, capture_output=True, text=True) #Capture output
 return True # File is formatted correctly
 except subprocess.CalledProcessError as e:
 logging.error(f"Prettier check failed: {e.stderr}") # Log the error from prettier check
 return False # File is not formatted correctly
`
What am I missing here?
