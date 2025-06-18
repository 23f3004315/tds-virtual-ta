---
chunk_id: discourse_topic_171141_post_468_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/468
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 112
username: 22f2000526
post_number: 468
topic_id: 171141
---

## Post #468 by 22f2000526

**Direct Link**: [Post #468](https://discourse.onlinedegree.iitm.ac.in/t/171141/468)

@carlton

Thank you i found my mistake in my docker file i wrote this CMD [“uv”, “run”, “app.py”] instead of

CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine
