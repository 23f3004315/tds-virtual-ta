---
chunk_id: course_live_session_2025_01_29_006
source_url: https://tds.s-anand.net/#/live-session-2025-01-29
source_title: live-session-2025-01-29
content_type: course
tokens: 561
---

 I've noted this error. It is from Cloudflare. You could just try again. When did you try this, apart from just now? You got the same error yesterday as well? Yeah, so that's some logic error in your code. It should not fetch all of it. There is some logic error.

**Q20: Should I install it separately?**

---

**A20:** No, you won't require requirements for it. Vercel is able to run the program without that.

**Q21: For Vercel, I will take the example code and try to run it. One more question: in question 9 (FastAPI), I'm giving the URL, but when I run the file, it shows the whole data. When I add conditions, it also shows the whole data. I'll show you that.**

**A21:** You should use the requests module and send a request using headers and all those informations. What you are using is actually OpenAI's own library, and that will not work. You will have to use the requests module and send the request just like the examples shown. There will be a URL, a header, and a payload. If you use their own library, it will not construct it correctly. Because the proxy has its own method of doing some of these functions that don't match OpenAI's. For 3.5, it worked, but that was more of a coincidence. If you use the documentation that is there on the AI proxy that Anand has provided, there's documentation there. If you use that documentation, then that might help. If you go back to where you get the token... You'll have to provide the documentation in this form. You'll use the requests instead of using the curl command. You just use the requests and send the inputs to it.

**Q22: This was in ROE last term. I'm getting an error. How?**

**A22:** This was a really fascinating question. There is a way, in fact many ways, to get it to say yes. You just have to trick it into saying yes. Just look up previous Discourse posts; you will probably find suggestions on there as well.

**Q23: Can I get the code for this?**

**A23:** He will... didn't he provide that in a Discourse post? Someone has pasted it on Discourse. If not, we can always ask him to provide it.

**Q24: I've taken one more course, something on business BA or something like that. There is no GA at all for this. There is a GA, but you don't submit here. These two courses are somewhat different.**

**A24:** Right, right.
