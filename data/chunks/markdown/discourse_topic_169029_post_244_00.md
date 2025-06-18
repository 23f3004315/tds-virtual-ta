---
chunk_id: discourse_topic_169029_post_244_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/244
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 293
username: 21f3002277
post_number: 244
topic_id: 169029
---

## Post #244 by 21f3002277

**Direct Link**: [Post #244](https://discourse.onlinedegree.iitm.ac.in/t/169029/244)

what is the problem in my Dockerfile it’s not working and crashing my system

`# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHON_VERSION=3.11

# Install system dependencies
RUN apt-get update &amp;&amp; apt-get install -y \
 python3.11 \
 python3-pip \
 python3-dev \
 git \
 curl \
 wget \
 ffmpeg \
 imagemagick \
 build-essential \
 libpq-dev \
 &amp;&amp; rm -rf /var/lib/apt/lists/*

# Ensure python3.11 is the default python version
RUN ln -sf /usr/bin/python3.11 /usr/bin/python

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh &amp;&amp; \
 bash nodesource_setup.sh &amp;&amp; \
 apt-get install -y nodejs &amp;&amp; \
 node -v &amp;&amp; \
 npm install -g prettier@3.4.2

# Copy dependencies file first to leverage caching
COPY re.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r re.txt
