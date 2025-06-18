---
chunk_id: course_live_session_2025_01_30_001
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 559
---

**

**A2:** The error likely stems from your `requirements.txt` file. Did you create a new virtual environment for this project, or did you install Flask on your global environment? When deploying Flask applications on Vercel, you need to keep a few things in mind. I'll show you how to create a `requirements.txt` file without manually typing it.

---

**Q3: I added a requirements.txt file with Flask and Flask-Cors, but Kartal sir said I could use the example in the question. Should I remove the requirements.txt file and rewrite the code? The code is working, but I'm getting a null output instead of a list of integers as requested.**

**A3:** Let's see your screen. The Flask application might be running fine as intended, but you might not be seeing the output. Sharing your screen would help me understand what's happening. You are getting a null output because you are not using a virtual environment. Let's create one.

**Q4: When writing tools needed in requirements.txt, do we need to specify the version?**

**A4:** Yes, you have to specify the version. But you don't have to manually type the `requirements.txt` file. You can use a single-line command in Python: `pip freeze > requirements.txt`. This will create the file with all the libraries and their versions in your virtual environment (or global environment if you don't have a virtual environment).

**Q5: I tried to create a virtual environment, but it showed an error. I'm using Vercel CLI.**

**A5:** Let's try `python -m venv venv` in PowerShell. If you are using a virtual environment, it will only return the libraries specifically present in that environment. Since you are currently using a global environment, it returns every library.

**Q6: Have you tried the optional exercise I gave you for the Flask API (Zodiac sign one)?**

**A6:** No one has tried it yet. The assignment was to ask for a person's month of birth and return their zodiac sign.

**Q7: The main problem is that I'm spending almost 2-3 days on the TDS assignments. The GAs have 10-18 questions on average.**

**A7:** I understand. The GAs are time-consuming. If you get some time and are in the mood, you can work on the optional mini-project. You can have many more types of ideas and execute them using Flask API.

**Q8: Currently, I'm not in the directory that contains the Vercel file (vercel.json).**

**A8:** I'm just demonstrating how to create the `requirements.txt` file.
