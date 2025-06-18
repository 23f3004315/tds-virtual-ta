---
chunk_id: course_live_session_2025_01_28_005
source_url: https://tds.s-anand.net/#/live-session-2025-01-28
source_title: live-session-2025-01-28
content_type: course
tokens: 573
---

 line mean?**

**A32:** For question 10, you need to use inverted double quotes for the key and value in the JSON file. For question 11, you need to right-click and inspect the element to find the class name. The data value should be 35.

**Q33: What are some other core concepts that are important to understand?**

---

**A33:** Before I talk about those, let's start with a simple example of how to make an API call to an LLM. API calls are powerful because you can use them in your programs.

**Q34: How do I get my API key?**

**A34:** You can find the link to get your proxy token on the GitHub page. I'll demonstrate using this proxy, but you can use something similar for other LLMs.

**Q35: What is a proxy?**

**A35:** OpenAI provides the service, but you don't interact with them directly. Anand has purchased tokens from OpenAI and provides access via a proxy. The proxy acts as a middleman between you and OpenAI.

**Q36: How many tokens does a prompt take?**

**A36:** The prompt we used took 32 tokens. The response ("negative") took two tokens. The total was 34 tokens. This cost us 1/10,000 of a dollar. Keep track of your token usage.

**Q37: How can I keep track of token usage?**

**A37:** Keep track of the prompt and the cost in a file. This will help you be efficient.

**Q38: How are API calls made?**

**A38:** You'll need a URL, headers (including authorization), and a JSON payload. The payload includes the model, messages, and response format. The response format should be strictly defined to avoid unexpected output.

**Q39: Can you share the notebook file?**

**A39:** No, we don't typically share the notebook file itself, as it prevents you from fully grasping the concepts. However, a sample file is available.

**Q40: What about function calling?**

**A40:** We'll cover function calling in a later session. It's a key part of the project. Function calling allows your LLM to decide which function to call based on the prompt. We'll use last term's Project Two to demonstrate.

**Q41: What about embeddings?**

**A41:** Embeddings are another important topic. They reduce the cost of using tokens by an order of magnitude. You can download embeddings from Hugging Face. We'll demonstrate this in a future session.

**Q42: What about text extraction?**

**A42:** We'll cover this in a future session.

**Q43: What about Base64 encoding?**
