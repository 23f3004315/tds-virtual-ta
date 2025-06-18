---
chunk_id: course_live_session_2025_01_31_001
source_url: https://tds.s-anand.net/#/live-session-2025-01-31
source_title: live-session-2025-01-31
content_type: course
tokens: 570
---

: What is the goal of the program?**

**A3:** The program aims to automate the process of ordering something from an online store. It will take a user's order in plain English, understand the request, and place the order. It will also include a feature for updating existing orders.

**Q4: How will the program understand the user's prompt?**

---

**A4:** The program will send the user's prompt to OpenAI. OpenAI will use its function calling capabilities to identify the appropriate function to call from a predefined set of functions within your application, and return the function name and parameters in a JSON format.

**Q5: What are the predefined functions?**

**A5:** The predefined functions are a set of tools your application provides. Examples include `get_weather_info` (which takes a location as a parameter) and `best_hotels` (which also takes a location). OpenAI will determine which function to call based on the user's prompt.

**Q6: How does OpenAI determine which function to call?**

**A6:** OpenAI analyzes the user's prompt and, based on its understanding of the context and semantics, selects the appropriate function from the predefined set. The response from OpenAI will include the function name and its required parameters in JSON format.

**Q7: How does the program use the OpenAI response?**

**A7:** Your application receives the JSON response from OpenAI, extracts the function name and parameters, and then executes the function with those parameters. The result is then sent back to the user. OpenAI acts as a proxy for a human agent, handling natural language input and translating it into structured data for your application.

**Q8: Is the `order` function dependent on the above-written cell?**

**A8:** Yes, the `order` function uses variables defined in previous cells.

**Q9: How is the JSON response handled?**

**A9:** The JSON response from OpenAI is structured data that your application can easily process. It contains the function name and the parameters needed to execute that function.

**Q10: How can we handle cases where the user doesn't provide complete information?**

**A10:** You can instruct OpenAI to request missing information. The handling of incomplete requests depends on your application's design. OpenAI itself might request the missing data.

**Q11: How can we integrate a voice model?**

**A11:** You can integrate a speech-to-text model (like Whisper from OpenAI) to convert voice commands into text prompts for your application.

**Q12: How do we package the Colab notebook into a full-fledged application?**

**A12:** We'll demonstrate this in a future session by creating another function and packaging the entire application into a Docker image.
