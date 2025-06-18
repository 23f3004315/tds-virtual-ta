---
chunk_id: course_live_session_2025_02_01_001
source_url: https://tds.s-anand.net/#/live-session-2025-02-01
source_title: live-session-2025-02-01
content_type: course
tokens: 572
---

 defined order of execution, unlike notebooks where code cells may not necessarily branch from one section to another. Notebooks are great for sharing with others who may not understand the code, as you can add Markdown to explain each step.

**Q2: In the delete order function, could a wrong order ID get deleted if the prompt contains multiple things that could match multiple orders?**

---

**A2:** That's a good question. This application isn't built to be very robust. The goal is to demonstrate GPT's ability to convert natural language into functions that the application understands. A real-world application would have a more robust interface (website or local app) with precisely crafted inputs to map to functions, preventing such errors.

**Q3: How can I avoid manually managing virtual environments and dependencies when deploying my application?**

**A3:** Use `uv`. `uv` is similar to Docker in that it handles dependencies without requiring manual management of virtual environments. You just specify your dependencies at the top of your code, and `uv` handles everything else, including creating and disposing of the virtual environment. This is especially useful when dealing with many submissions with different package requirements, as seen in a previous project with nearly 700 submissions.

**Q4: How does the application know which function to run based on the user's request?**

**A4:** You send the user's natural language request (prompt) and a list of your application's capabilities to GPT. GPT determines which function to run and the required parameters, returning this information as structured JSON. Your application then uses this JSON to execute the appropriate function.

**Q5: What is the purpose of `if __name__ == "__main__":`?**

**A5:** This is the entry point for your application. The Python interpreter runs from top to bottom, but it won't run the code within this block unless the file is the starting file of the application. This is crucial for multi-file applications where the interpreter needs to know where to begin.

**Q6: Should I create a tunnel for this application?**

**A6:** No, there's no need to create a tunnel if you want others to try it. Using a tool like ngrok allows others to access your server directly and send queries. However, be aware that this might crash your system if the queries aren't clean, as there's no robust error handling.

**Q7: How do I pass URL-encoded parameters to a FastAPI application?**

**A7:** You pass them in the URL itself. For example, `localhost:8000/order?q=Laptop,2,123 Main St,2024-02-29`. The application then reads the parameter from the URL.

**Q8: Why is my application returning a null response or a 422 error?**
