---
chunk_id: discourse_topic_171141_post_369_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/369
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 299
username: Haricharan
post_number: 369
topic_id: 171141
---

-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

---

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
`
here u can see it installs using pip install …

here it’s requiring `.env` file to be present in the project folder because my project when I was uploading to both git and docker had `.env` file for AIPROXY_TOKEN and I uploaded to docker with that `.env` file but as git doesn’t allow upload of `.env` file I couldn’t upload`.env` to git

the project will still work after downloading the repository when we upload AIPROXY_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because`.env` file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the `.env` file so it didn’t build so I had to create the `.env` file now to create the docker image, and for the dockerimage I had submitted, I built it with the `.env` file(it supports both`.env` file and environment variable one)
