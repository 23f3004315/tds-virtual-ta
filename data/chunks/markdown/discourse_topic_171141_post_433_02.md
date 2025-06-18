---
chunk_id: discourse_topic_171141_post_433_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/433
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 129
username: carlton
post_number: 433
topic_id: 171141
---

COPY .env /app/` is highlighted, indicating this might be a point of discussion or confusion. 2x" data-dominant-color="2E2C2B">Screenshot 2025-04-08 at 11.12.18 am754×302 41 KB

---

This is because if you look at your Dockerfile .env does not exist in your repo.

Therefore it does not build.

Your docker is supposed to take the AIPROXY token from our environment not from yours.

This is passed dynamically at runtime of the Docker.

Since it fails to build, we cannot evaluate it.

Kind regards
