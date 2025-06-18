---
chunk_id: course_live_session_2025_01_30_002
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 573
---

 some time and are in the mood, you can work on the optional mini-project. You can have many more types of ideas and execute them using Flask API.

**Q8: Currently, I'm not in the directory that contains the Vercel file (vercel.json).**

**A8:** I'm just demonstrating how to create the `requirements.txt` file.

---

**Q9: If I'm running a virtual environment with `uv`, will it only copy out the tools that are in the virtual environment?**

**A9:** Exactly. That's a downside of `uv`. When using `uv`, you are not installing those libraries. If they are not installed, they won't be present in your virtual environment, and therefore won't be in your `requirements.txt` file. For minor projects that you don't need to deploy, `uv` is fine. Otherwise, create a virtual environment and install the libraries there.

**Q10: Now it's showing nothing. I don't know why.**

**A10:** Your server is not running. Run `vercel deploy --prod` again. I'm not a big fan of Vercel CLI; I usually push to GitHub and then establish a connection between Vercel and GitHub. Let's open the dev tools (right-click, inspect), go to the console, and reload. Show me your code.

**Q11: I'm using httpx.**

**A11:** Yesterday, I told you that you can use the example file from the question. That's why you rewrote the code. Otherwise, you would have created the `requirements.txt` file and deployed both. This was working yesterday; now it's showing blank. Can you show me the code?

**Q12: It was working perfectly yesterday. Now it's showing blank. An error page is showing. Sir told me to add `/api` to the URL, and it would show some data. When I entered that link in the assignment, it gave me a null list.**

**A12:** That's what happens when nothing is showing. Can you scroll down? You're using CORS. You've used a lot of complexity; you've made it a lot more complex. You took help from ChatGPT. That explains the comments. It's not directing you somewhere. The JSON file is not present in the API folder. Let's go to line 5 of your code. Add `../` before `q` to include the parent directory. Save and redeploy.

**Q13: Should I remove the `.vercel` folder and redeploy?**

**A13:** No, that won't work. Vercel CLI created that folder; it contains build instructions.

**Q14: Are the vercel.json and everything inside the API file?**
