---
chunk_id: discourse_topic_164277_post_202_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/202
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 313
username: 21f2000709
post_number: 202
topic_id: 164277
---

**[Discussion Image by 21f2000709]** This image shows instructor guidance in the TDS discussion forum, instructing students on how to run their Docker image using Podman. The provided command, `podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000`, sets the `AIPROXY_TOKEN` environment variable and maps port 8000 to the same port in the container, so the API will be accessible at `http://localhost:8000/run?task=...`. This command aims to automate the process of running the image and ensures that the API is correctly configured for access. Students can directly use this command, after filling in the image name, to ensure correct setup and deployment of the service in their project. available at `http://localhost:8000/run?task=...`. The `podman run` command includes environment variable setup with `-e AIPROXY_TOKEN=$AIPROXY_TOKEN` and port mapping with `-p 8000:8000`. The purpose is to guide students on how to properly set up and access the API exposed by the containerized application, ensuring it runs and is accessible via localhost." alt="Screenshot 2025-02-13 at 1.31.01 PM" data-base62-sha1="23Nzhqv7fQsw7MQIWGUG4ZEkERS" width="690" height="75" data-dominant-color="353F44">
