---
chunk_id: discourse_topic_164277_post_202_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/202
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 416
username: 21f2000709
post_number: 202
topic_id: 164277
---

 such file or directory: OCI runtime attempted to invoke a command that was not found`

However the correct command seems to be:

`podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 $IMAGE_NAME`

This works totally fine.

---

**[Discussion Image by 21f2000709]** This image captures a terminal output demonstrating the successful startup of the Uvicorn server for the TDS Project, part of an LLM-based automation agent. It shows the execution of a `podman run` command with the AIPROXY_TOKEN environment variable set and port 8000 mapped, indicating a containerized deployment. The system messages confirm the server process has started, the application has initialized successfully, and Uvicorn is running on `http://0.0.0.0:8000`. This output would typically be shared by a student showing that their server setup for the project is working correctly. No immediate error messages are present; however, the image hints at a discussion about server setup and potentially AIPROXY_TOKEN configuration in the broader context of the discussion thread.ng the `AIPROXY_TOKEN` environment variable and mapping port 8000. The output confirms that the server process started, the application startup completed, and Uvicorn is running on `http://0.0.0.0:8000`, with instructions to quit using CTRL+C. The student's command is: `podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 tds-project-pradeep-mondal`. This suggests the student has successfully deployed the application using Podman, and the server is running correctly." alt="Screenshot 2025-02-13 at 1.33.21 PM" data-base62-sha1="tCcab37inD3OmPbAYgJPLdNROyb" width="690" height="45" data-dominant-color="252525">
