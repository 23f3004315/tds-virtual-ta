---
chunk_id: course_live_session_2025_02_01_002
source_url: https://tds.s-anand.net/#/live-session-2025-02-01
source_title: live-session-2025-02-01
content_type: course
tokens: 452
---

 parameters to a FastAPI application?**

**A7:** You pass them in the URL itself. For example, `localhost:8000/order?q=Laptop,2,123 Main St,2024-02-29`. The application then reads the parameter from the URL.

**Q8: Why is my application returning a null response or a 422 error?**

---

**A8:** Several things could cause this. Ensure that:

- The `prices` dictionary is defined globally, not within a function.
- The prompt is correctly formatted and includes all necessary information (items, address, time).
- The application can communicate with the outside world (check network connectivity).
- You are using the correct key in the JSON response (`.keys()`).

**Q9: How do I use Docker?**

**A9:** Docker creates lightweight, self-contained images that run inside a Docker engine. This isolates your application from the underlying system, making it portable and easy to deploy anywhere. You build the image using `podman build -t tds-hello .` (the `.` refers to the current working directory). Then, you run it using `podman run -it tds-hello bash`. The `bash` command opens an interactive shell within the Docker container.

**Q10: What are the use cases for Docker?**

**A10:** Docker is useful for deploying applications to various environments without worrying about dependencies or system specifics. You create a Docker image containing your application and its dependencies. Anyone can then download and run the image regardless of their operating system. This is especially helpful for teams with different setups or when deploying to multiple clients.

**Q11: What should I focus on for the GA3 project?**

**A11:** The GA3 project will involve using the concepts covered today, but on a larger scale. You'll need to create more robust error handling and focus on prompt engineering to ensure the LLM generates the correct code. A previous session covered the basics of LLM calls, tokenization, embeddings, and image URI encoding. Review that session and the material on prompt engineering to prepare. The goal is to create a self-writing program that uses the LLM to generate and correct code dynamically.
