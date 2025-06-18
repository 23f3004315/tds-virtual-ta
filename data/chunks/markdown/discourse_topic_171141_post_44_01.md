---
chunk_id: discourse_topic_171141_post_44_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/44
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 367
username: carlton
post_number: 44
topic_id: 171141
---

**Direct Link**: [Post #44](https://discourse.onlinedegree.iitm.ac.in/t/171141/44)

You have a misspelling in your environment variable, thats why it failed. We do pass the token to your docker exactly as specified in Project 1 page.

---

**[Discussion Image by carlton]** This image depicts a Python traceback, indicating a runtime error in the TDS project. Specifically, it shows a `KeyError: 'AIRPROXY_TOKEN'`, arising when the script attempts to retrieve the `AIRPROXY_TOKEN` environment variable on line 30 of `/app/app.py` using `os.environ`. This means the environment variable 'AIRPROXY_TOKEN' is not defined in the environment where the script is running. The error suggests a student question regarding missing environment variables. A likely resolution involves correctly setting the 'AIRPROXY_TOKEN' environment variable before executing the Python script.am attempts to access an environment variable named 'AIRPROXY_TOKEN' using `os.environ['AIRPROXY_TOKEN']` on line 30, but the system cannot find an environment variable with that name, leading to the `KeyError`. The traceback also points to a frozen os module, which is a part of Python's internal implementation for accessing environment variables. This suggests the student either hasn't set the `AIRPROXY_TOKEN` environment variable or there's a typo in the variable name within the code or when setting it in the environment. The red box emphasizes the 'AIRPROXY_TOKEN' within the code snippet where the error is triggered." alt="image" data-base62-sha1="cQ8bgXIjD37N3gxBAEHvJ8iStNL" width="633" height="197">image633×197 5.21 KB
