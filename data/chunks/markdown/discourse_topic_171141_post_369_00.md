---
chunk_id: discourse_topic_171141_post_369_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/369
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 272
username: Haricharan
post_number: 369
topic_id: 171141
---

## Post #369 by Haricharan

**Direct Link**: [Post #369](https://discourse.onlinedegree.iitm.ac.in/t/171141/369)

Sir actually my project doesn’t have requirements.txt, instead it installs automatically

when:

`uv run app.py` is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).

my dockerfile from the repo:

`FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh &amp;&amp; rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/
