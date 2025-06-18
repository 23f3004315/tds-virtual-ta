---
chunk_id: discourse_topic_164277_post_157_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/157
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 905
username: 22f3002771
post_number: 157
topic_id: 164277
---

1

**Direct Link**: [Post #157](https://discourse.onlinedegree.iitm.ac.in/t/164277/157)

hi @carlton @Jivraj

for A2 i am getting this particular error and i don’t know what i am doing wrong in this

---

**[Discussion Image by 22f3002771]** This image shows a code execution log from a TDS project where a student is running a task to format the contents of `/data/format.md` using prettier version 3.4.2, and updating the file in place. The log first shows a successful HTTP POST request to the `/run` endpoint, with the task details including file path and prettier version, which returned HTTP 200 OK. Then a GET request is made to `/read?path=/data/format.md` that also results in 200 OK, with the log displaying the contents of `/data/format.md`, which includes "#Unformatted Markdown", sample paragraph, lists, and python code with print statement. The red dot probably indicates that the formatting was not performed as expected, and the displayed content is the "before" state.ing with mixed content." alt="Screenshot from 2025-02-12 19-31-47" data-base62-sha1="a1qItFSCXcfheeTQHIxQNQK6b84" width="690" height="259" srcset="**[Discussion Image by 22f3002771]** This image depicts a student's attempt to format a markdown file using prettier within an LLM-based automation agent project. It shows the system running a task to format the content of `/data/format.md` using `prettier@3.4.2`. A POST request to `http://localhost:8000/run` with task details results in a successful HTTP 200 response, indicating the function `format_file_with_prettier` was invoked with the specified file path and prettier version. A subsequent GET request reads the file content and displays the "EXPECTED" (desired formatted output) alongside the "RESULT" (unformatted content). The markdown file contains an unformatted header, sample paragraph, and list, indicating the prettier formatting has not been applied as expected which is potentially a point of confusion for the student., **[Discussion Image by 22f3002771]** This image shows a snippet from a student's attempt to format a markdown file using Prettier within the TDS project 1 environment. The screenshot captures the output of a task execution, indicating that the student is using the `format_file_with_prettier` function with the file path `/data/format.md` and Prettier version 3.4.2. The HTTP requests and responses are visible, including a POST request to run the task and a GET request to read the file contents. Crucially, the "EXPECTED" and "RESULT" sections show that the markdown file remains unformatted despite the task execution, which indicates a problem with the Prettier formatting process. The student appears to be troubleshooting why the file is not being formatted as expected, initiating peer or instructor discussion about potential issues with the task execution or Prettier configuration. 1.5x, **[Discussion Image by 22f3002771]** This image shows the execution of an LLM-based automation agent task within the TDS "Project 1" discussion thread. The agent is attempting to format the `/data/format.md` file using `prettier@3.4.2`, updating the file in-place. A POST request to `http://localhost:8000/run` initiates the formatting, specifying the task as formatting the file with Prettier, and includes the file path and prettier version in the arguments. Subsequently, a GET request to `http://localhost:8000/read?path=/data/format.md` retrieves the file content, revealing that the formatting has not been applied as expected, showing that the file is still "Unformatted Markdown" with the original content including extra spaces. This suggests a potential problem with the execution of the prettier command or how the updated file is being written back, indicating a debugging opportunity for the student. 2x" data-dominant-color="1B1B1B">Screenshot from 2025-02-12 19-31-471501×564 44.7 KB
