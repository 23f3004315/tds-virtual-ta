---
chunk_id: discourse_topic_171141_post_110_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/110
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 453
username: 23f2004644
post_number: 110
topic_id: 171141
---

110](https://discourse.onlinedegree.iitm.ac.in/t/171141/110)

Sir, I checked my evaluation log, and the error occurred because the **AI proxy token limit was exceeded**. I ran the evaluation script to verify, and I scored **12/20**.

---

**[Discussion Image by 23f2004644]** This image captures a console output showing a series of errors encountered while running a Flask application, indicative of a student troubleshooting their code during project development. The output begins with the Flask app initialization, including debugging mode being on and running on specific IP addresses and ports. Subsequently, a series of 500 and 404 errors are reported, stemming from `POST` and `GET` requests to the `/run` and `/read` endpoints, respectively, indicating issues with the task execution and file retrieval. The core error is a `TypeError: 'NoneType' object has no attribute 'lower'`, originating from `app.py` line 22 within the `run_task` function, suggesting the `classification.get("action", "")` call is returning `None`, and further requests result in similar errors with different tasks and file paths, demonstrating a recurring problem in how the application handles requests and data.ates from `app.py`, line 22, specifically an `AttributeError: 'NoneType' object has no attribute 'lower'`. This occurs when trying to call `.lower()` on a value retrieved from `classification.get("action", "")` that is `None`. Subsequent lines show various failed requests to `/run` with different tasks, as well as 404 errors when trying to GET `/read?path=/data/format.md`, suggesting potential issues with file paths or task parameters. The errors point to a problem in how the application is handling input parameters for different tasks, particularly when the `action` is not properly defined or retrieved in the `classification` lookup." alt="image" data-base62-sha1="gwD7SZY75yucA5CeD6a6hXj3CuA" width="690" height="362" data-dominant-color="F5F5F5">image1456×765 41.6 KB
