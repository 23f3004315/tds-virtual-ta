---
chunk_id: course_live_session_2025_01_29_002
source_url: https://tds.s-anand.net/#/live-session-2025-01-29
source_title: live-session-2025-01-29
content_type: course
tokens: 563
---

 steps, including checking the code, going to the Vercel dashboard, and appending `/api` to the URL. The issue is that the Flask module is not installed on Vercel. The instructor suggests using a capital 'F' in `Flask` in the requirements.txt file. The instructor also suggests using GitHub, where a requirements.txt file is not needed.)

---

**Q8: In the FastAPI question, I'm pushing the website, but it's not taking the conditions (API class equals 1A or class equals 1B) mentioned in the question. It's also giving the whole JSON file. What should I do?**

**A8:** Regarding the Vercel question, you can mention a capital 'F' for Flask, but I think it won't install because... I've just checked, and on the GitHub page, I don't have a requirements file. If you push it to GitHub and it's connected to GitHub, you don't need the requirements file. Something else is the issue. It's not able to pull the Flask module. You should not have to install it separately while running the file. I used `http.server`. There's example code given in GA2 itself for question 6. There's sample code there that uses `http.server`. I just modified that bit and put my function in there, and it works without any issues. The only difference is that I modified that and put the function inside that piece of code that handles the request. You don't need a separate `requirements.txt` file; Vercel can run the program without that. You still need to verify that your function actually runs. That's one thing you'll have to check. Regarding the FastAPI question, there's a logic error in your code. It shouldn't fetch all of it. Your query actually says `class` (CLASSS) without an underscore. If you put an underscore there, it will probably give you the correct response.

**Q9: I'm getting an error in question 10 of GA2. (Student shares screen.)**

**A9:** Please close the picture-in-picture; it won't disconnect the session. (The instructor then guides the student through troubleshooting steps, including copying the error and posting it on Discourse and tagging Anand. The instructor suggests using the ngrok URL (the one in front of forwarding in the terminal). The error is a Cloudflare error. The instructor suggests copying the error and sending it on Discourse and tagging Anand.)

**Q10: I wanted to say that while installing ngrok with the terminal, I wasn't able to do that, so I installed it in a different directory using the app. Is it doing anything? When I run it from here...**
