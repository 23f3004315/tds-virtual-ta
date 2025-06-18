---
chunk_id: course_live_session_2025_01_23_001
source_url: https://tds.s-anand.net/#/live-session-2025-01-23
source_title: live-session-2025-01-23
content_type: course
tokens: 570
---

 git repository.

**Q2: I'm having trouble viewing my GA1. It's showing zero ones. Can you help?**

**A2:** Let's look at your screen. It appears there are different timestamps. I'll help you troubleshoot.

**Q3: How can I move files from multiple subfolders into a single folder using the command line?**

---

**A3:** I used a bash script that combines the `find` command (to locate files of a specific type, like `.txt` files) and the `mv` command (to move them). The `find` command searches the current directory (`./`) for files (`-type f`) and the `-exec` option executes the `mv` command on each file found. The curly braces `{}` are placeholders for the filenames.

**Q4: Will knowing only six SQL commands (SELECT, FROM, GROUP BY, etc.) be enough to complete this course?**

**A4:** You'll only need basic SQL for this course, mainly for extracting data. We're not covering a full DBMS course. A good resource to learn more is SQLZoo. While you might not need more than six commands for this course, ChatGPT can help if you encounter more complex SQL queries.

**Q5: How can I deploy a Flask application to Vercel?**

**A5:** First, set up a git repository and connect it to your GitHub account. Then, create a virtual environment for your Python project using `python -m venv `. Activate it using the appropriate script (e.g., `.\env\Scripts\activate`). Install Flask using `pip install flask`. Create a `.gitignore` file to exclude the virtual environment folder. Then, create a `vercel.json` file with build instructions for Vercel. Commit and push your code to GitHub. Finally, add your project to Vercel, selecting the correct repository and build settings (Python, not Node). Vercel will automatically redeploy your application whenever you push changes to GitHub. This is called CI/CD (Continuous Integration/Continuous Deployment).

**Q6: What does the port number matter when deploying to Vercel?**

**A6:** When deploying to Vercel, the port number you use locally doesn't matter because Vercel will assign your application its own domain. You should remove `debug=True` from your Flask application before deploying to production.

**Q7: Why do I need administrator permissions to use ngrok?**

**A7:** ngrok is a command-line tool that forwards requests to your local host. It doesn't need to be installed in your virtual environment. However, you might need administrator privileges to forward requests through a port. If you encounter permission issues, try running PowerShell as administrator.
