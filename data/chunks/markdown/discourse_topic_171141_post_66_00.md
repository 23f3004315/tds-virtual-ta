---
chunk_id: discourse_topic_171141_post_66_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/66
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 278
username: Jivraj
post_number: 66
topic_id: 171141
---

## Post #66 by Jivraj

**Direct Link**: [Post #66](https://discourse.onlinedegree.iitm.ac.in/t/171141/66)

Yeah, it’s there on your local machine, but you didn’t copy it to docker container.

Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.

`FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh &amp;&amp; rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
`
