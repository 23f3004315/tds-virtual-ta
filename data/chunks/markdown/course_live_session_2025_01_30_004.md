---
chunk_id: course_live_session_2025_01_30_004
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 529
---

api`.**

**A20:** Should I remove the `.vercel` folder and redeploy? No, that won't work. Vercel CLI created that folder; it contains build instructions.

**Q21: Show your folder structure.**

**A21:** I created the directory, then another folder `api`, and then `index.py` inside `api`.

---

**Q22: If I use `uv`, will it only copy the tools in the virtual environment?**

**A22:** Yes.

**Q23: What is more convenient? Directly integrating GitHub and creating files there, saving space on my local system?**

**A23:** I don't think that will save space on your local system because you have to create files locally before pushing them to Git.

**Q24: Can we use the query function?**

**A24:** Yes, absolutely. It's working like this. I'll comment it out, duplicate it, and comment it out once. Then we can run this. The query function is working. We have got the entire row where the city was. We can extract the population using this. It's working perfectly fine. It returned the population of Delhi.

**Q25: Do we need to mention values [square bracket] zero, values zero, if we are mentioning population only?**

**A25:** That's a very good question. If you use this, it will return a series (a Pandas term). It's just a column; it won't give you the exact value. We have to extract the zeroth value. We have to extract the values. `values` will return this.

**Q26: Question 9: I don't know how to use `class` as a variable name.**

**A26:** `class` is a keyword. You can't use it as a variable name. Create a different variable name. I used an alias.

**Q27: Question 6: Can you take the last of the class now, or should I wait?**

**A27:** Let's arrange a separate meeting to discuss this. I'll also look into your file. You can share it on Discourse or email it to me.

**Q28: Can we use `httpie` instead of `requests`?**

**A28:** Yes, you can change it to `httpx`. `httpie` is a command-line tool, not a Python module. I'm not sure about `httpie`.

**Q29: Can we get the names of the words and their embeddings separately in the JSON?**
