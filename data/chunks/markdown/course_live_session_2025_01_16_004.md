---
chunk_id: course_live_session_2025_01_16_004
source_url: https://tds.s-anand.net/#/live-session-2025-01-16
source_title: live-session-2025-01-16
content_type: course
tokens: 486
---

, JavaScript will work on the entire site unless you use selectors to target specific elements.

**Q29: What is the origin of the exercise to extract names from the meeting participants?**

**A29:** The instructor created this exercise to encourage participation. A random participant is selected to answer a question.

**Q30: Can we go back to the syntax we typed?**

---

**A30:** The syntax was `$$(".className").map(...)`. The `$$` selects elements with the specified class, and `map` iterates through them. The instructor demonstrates how to extract the movie names using this. The instructor also explains the difference between `innerText` and `innerHTML`. `innerText` returns only the text, while `innerHTML` returns the entire HTML code. `innerText` is generally preferred for data extraction. If `text` doesn't work, use `innerText`.

**Q31: Should the `innerText` be written exactly as it appears, or can we modify the case (e.g., make "T" lowercase)?**

**A31:** Use the text exactly as it appears.

**Q32: What is the role of npx in this context?**

**A32:** npx creates a separate environment for a project, installing dependencies locally without affecting other projects. It's an alternative to npm, which installs globally.

**Q33: Does npx run primarily on Linux?**

**A33:** npx works on both PowerShell and Bash, but sha256sum might not work on Windows. You can run the npx command separately and use sha256sum on the resulting file.

**Q34: While showing `innerText`, you made the movie list extremely neat. Why?**

**A34:** That's how the console presents the data, organizing it into groups of 100 for readability.

**Q35: How can I copy the entire list from the console?**

**A35:** Use the `copy()` function in the console to copy the output to your clipboard.

**Q36: What should we focus on when using the Elements, Console, and Network tabs?**

**A36:** For the Elements tab, focus on extracting data using CSS selectors (classes and IDs). The Console tab is used for running JavaScript, particularly for data scraping with CSS selectors. The Network tab shows what the browser is fetching. The instructor recommends exploring these tabs and having fun with them.
