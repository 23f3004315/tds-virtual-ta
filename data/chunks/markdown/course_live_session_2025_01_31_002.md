---
chunk_id: course_live_session_2025_01_31_002
source_url: https://tds.s-anand.net/#/live-session-2025-01-31
source_title: live-session-2025-01-31
content_type: course
tokens: 478
---

A11:** You can integrate a speech-to-text model (like Whisper from OpenAI) to convert voice commands into text prompts for your application.

**Q12: How do we package the Colab notebook into a full-fledged application?**

**A12:** We'll demonstrate this in a future session by creating another function and packaging the entire application into a Docker image.

---

**Q13: What is the role of prompt engineering in this process?**

**A13:** Prompt engineering is less about a specific science and more about understanding how the system works to write effective prompts that yield the desired results. The course will cover this in more detail.

**Q14: What if the `order` function doesn't work as expected?**

**A14:** The instructor suggests checking the code, ensuring the correct parameters are passed, and handling potential errors gracefully. The instructor also suggests using `json.loads` to convert strings to JSON objects.

**Q15: What is the duration of the Review of Exercises (ROE)?**

**A15:** The ROE duration varies from term to term, ranging from 45 minutes to 1.5 hours. It's recommended to save your work frequently.

**Q16: What if the user's prompt is missing information?**

**A16:** The instructor suggests adding a system prompt to OpenAI to explicitly request missing parameters.

**Q17: How do we handle the `UUID` generation to ensure uniqueness?**

**A17:** The `UUID` library generally provides unique identifiers. If you need to reduce the chance of collisions, you can increase the size of the UUID. More information is available in the UUID documentation.

**Q18: How do we handle the file path in a deployed application?**

**A18:** Instead of using absolute paths (`os.path`), use relative paths to ensure the application works correctly in different environments. For deployed applications, you would typically use a `.env` file to store sensitive information like API keys.

**Q19: What is the overall approach to building this application?**

**A19:** The approach is to use OpenAI's function calling capabilities to translate natural language prompts into structured data that your application can process. This allows for a more natural user experience without the need for a complex UI. The instructor emphasizes the importance of understanding how to parse JSON responses and handle errors.
