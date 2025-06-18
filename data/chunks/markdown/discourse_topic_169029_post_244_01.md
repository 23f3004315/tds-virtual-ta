---
chunk_id: discourse_topic_169029_post_244_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/244
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 168
username: 21f3002277
post_number: 244
topic_id: 169029
---

 nodejs &amp;&amp; \
 node -v &amp;&amp; \
 npm install -g prettier@3.4.2

# Copy dependencies file first to leverage caching
COPY re.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r re.txt

---

# Install `uv` package manager from Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create and set working directory
WORKDIR /app

# Copy application files
COPY main.py .
COPY llm_functions.py .
COPY llm_tools_functions_calls.py .
COPY server.py .

# Set default command to start the FastAPI server with `uv`
CMD ["uv", "run", "main.py"]

`
@carlton @Jivraj
