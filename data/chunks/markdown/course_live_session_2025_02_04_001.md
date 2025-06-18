---
chunk_id: course_live_session_2025_02_04_001
source_url: https://tds.s-anand.net/#/live-session-2025-02-04
source_title: live-session-2025-02-04
content_type: course
tokens: 558
---

, Thunder Client is now a paid service.

**Q2: Previously, I was seeing some things, but now I'm getting the "method not allowed" error. I don't know why.**

**A2:** Let's troubleshoot this. We'll use Thunder Client.

**Q3: After changing my method to POST, what do I do next?**

---

**A3:** Go to the "Body" section in Thunder Client. Create a JSON object using curly braces `{}`. Then, refer to question 7 for the JSON object to copy and paste. Remove the three dots (...) from the copied JSON. Click the "Send" button.

**Q4: I'm getting an error: "API key client option must be set either by passing API key to the client or by setting the OPENAI_API_KEY environment variable." Am I trying to access an OpenAI key?**

**A4:** Yes, you are. Since you don't have a `.env` file, you need to create one. For now, comment out the code after line 172 and replace it with `return "hello"` to test. Restart the server.

**Q5: Thunder Client is not showing any paywall.**

**A5:** Thunder Client has a free version with limitations (e.g., 15 collections and 15 requests).

**Q6: Earlier, Thunder Client was free. When did it change?**

**A6:** Recently.

**Q7: I'm still stuck. Can you spell "Thunder Client"?**

**A7:** T-H-U-N-D-E-R-C-L-I-E-N-T

**Q8: I'm still getting errors. What's wrong?**

**A8:** Let's review your code. You're trying to send a request using the OpenAI module, which won't work. You need to send the request through an API proxy.

**Q9: I tried using an API proxy, but I still got errors.**

**A9:** Let's focus on getting the basic functionality working. We'll create a simple application and send a POST request using Thunder Client.

**Q10: In the code, what goes in the brackets on lines 19, 20, 21, and 23?**

**A10:** Those lines are for allowing requests from external servers. You can list the servers you want to allow. If you use `*`, anyone can access the application. It's better to restrict access by listing specific servers. For example, if you only want to allow access from `server1` and `server2`, you would list them. You only need to mention the domain name.

**Q11: I'm stuck on the Docker part of the assignment.**
