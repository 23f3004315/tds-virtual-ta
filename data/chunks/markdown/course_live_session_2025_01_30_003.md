---
chunk_id: course_live_session_2025_01_30_003
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 564
---

` before `q` to include the parent directory. Save and redeploy.

**Q13: Should I remove the `.vercel` folder and redeploy?**

**A13:** No, that won't work. Vercel CLI created that folder; it contains build instructions.

**Q14: Are the vercel.json and everything inside the API file?**

---

**A14:** No, they are in the `vercel-python/api` directory.

**Q15: I don't know how to use `class` as a variable name in question 9.**

**A15:** `class` is a keyword in Python. You can't use it as a variable name. I'll explain how to handle this. You need a different variable name. I used an alias. I'll explain what that means.

**Q16: When passing multiple parameters with the same name, how do I handle it?**

**A16:** You need to use lists. Import `List` from the `typing` library. I got this from ChatGPT. Always learn from ChatGPT, but also learn from the process. The query will take all the strings and put them into one list. The default value is used if no parameter is passed. An alias is another name for a variable. The variable name is `className`, but we can use the `class` parameter using this alias.

**Q17: My code was working correctly except for the name. I don't know how to write it.**

**A17:** You are using `httpx`. You're also using `index.py`. This is not Flask-based; it's more like an HTTP server.

**Q18: I'll try to do it again according to the requirements and add the requirements.txt file. After that, I'll share my screen.**

**A18:** Okay, you can do that. The Flask-based code is not needed here.

**Q19: I'm confused because it was working perfectly (or at least working) yesterday.**

**A19:** Can you open Vercel again? Yesterday, was this particular box showing "Not Found"? When you added `/api` to the URL, it showed a dictionary. It was returning a JSON object. Show me your folder structure.

**Q20: I created the directory, then another folder `api`, and then `index.py` inside `api`.**

**A20:** Should I remove the `.vercel` folder and redeploy? No, that won't work. Vercel CLI created that folder; it contains build instructions.

**Q21: Show your folder structure.**

**A21:** I created the directory, then another folder `api`, and then `index.py` inside `api`.
