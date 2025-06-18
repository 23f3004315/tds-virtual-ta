---
chunk_id: discourse_topic_171141_post_440_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/440
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 156
username: Haricharan
post_number: 440
topic_id: 171141
---

 in the previous message, the steps which I used:

`git clone https://github.com/23f2001390/llmagent.git
`
adding `.env` with AIPROXY token and replacing `evaluate.py` and `datagen.py` with new ones according to test environment

---

`docker build -t llm-agent .
`
`docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent
`
and in another terminal

`uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000
`
Thank you

Kind regards
