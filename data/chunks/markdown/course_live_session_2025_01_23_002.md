---
chunk_id: course_live_session_2025_01_23_002
source_url: https://tds.s-anand.net/#/live-session-2025-01-23
source_title: live-session-2025-01-23
content_type: course
tokens: 334
---

 production.

**Q7: Why do I need administrator permissions to use ngrok?**

**A7:** ngrok is a command-line tool that forwards requests to your local host. It doesn't need to be installed in your virtual environment. However, you might need administrator privileges to forward requests through a port. If you encounter permission issues, try running PowerShell as administrator.

---

**Q8: What is ngrok and how does it work?**

**A8:** ngrok creates a public URL that forwards requests to your locally running application. This allows anyone on the internet to access your application, even though it's running on your local machine. Your computer acts as a server. Note that ngrok only works while your local server is running. For a permanent solution, deploy to a platform like Vercel or Netlify.

**Q9: What is a virtual environment and why is it useful?**

**A9:** A virtual environment creates a separate, isolated environment for your project. This prevents conflicts between different project dependencies. Think of it like creating a separate section in a swimming pool for a child, where the depth is less than the main pool. You can install libraries (like Flask and Pandas) within the virtual environment without affecting your global Python packages.

**Q10: What is the assignment?**

**A10:** Create a Flask application that takes a user's birth month as input and returns their zodiac sign. This is a fun exercise to improve your Flask skills. You can deploy it to Vercel or Netlify and share the link. Remember to create a `.gitignore` file to exclude the virtual environment folder.
