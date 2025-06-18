---
chunk_id: course_live_session_2025_01_21_002
source_url: https://tds.s-anand.net/#/live-session-2025-01-21
source_title: live-session-2025-01-21
content_type: course
tokens: 560
---

 do?**

**A8:** This will be addressed toward the end of the session.

**Q9: When running UVicorn on WSL, there are no issues. But on Windows, it seems there's an issue with anti-something, some shielders, or something on my computer, flagging it and preventing it from running. What should I do?**

---

**A9:** Most web infrastructure runs on Linux servers (maybe 80%). These tools are designed with Linux in mind, and later ported to Windows. There will be some issues running them on Windows. You can get Linux in Windows now using the Windows Subsystem for Linux (WSL). You need at least 8 GB of RAM to run it with reasonable performance. Anything less won't work or will work poorly. If you can, install WSL; it's worth it. Then these tools will work out of the box.

**Q10: What is CI/CD?**

**A10:** Continuous Integration/Continuous Deployment. It automates tasks such as compiling, running, and sending code to devices. It reduces the time lag between finding a bug, fixing it, and pushing the fix to the devices that need it. This is useful in data science when pulling data from various places and quickly integrating findings into a workflow.

**Q11: What is Vercel?**

**A11:** Vercel is a platform to deploy applications. You can deploy quickly and easily, and it automatically rebuilds when you push an update. You can deploy directly from your GitHub repo.

**Q12: What is the difference between Docker run and Docker compose?**

**A12:** Docker compose is for local testing. You can create a local network, give it a name, and test with four or five containers. For larger deployments, use Swarm (provided by Docker), Kubernetes, or Mesos.

**Q13: Can we wrap our MAD1 and MAD2 projects using Docker?**

**A13:** Yes, that's possible.

**Q14: Is there a demo where all the tools are used in a single project?**

**A14:** There will be a separate session for the project, towards the end of this week or the beginning of next week. This session will show how all the tools fit together.

**Q15: If someone goes through CSS, JavaScript, GitHub, and REST API, will that cover 50% of the course?**

**A15:** Yes, roughly. The core technologies (REST APIs, JavaScript, HTML, CSS) haven't changed much in 30 years. Learning these will give you a foundation to learn other tools more easily. The course will also spend significant time on LLMs and how they fit into the workflow.
