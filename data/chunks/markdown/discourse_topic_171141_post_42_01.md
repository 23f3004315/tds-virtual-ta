---
chunk_id: discourse_topic_171141_post_42_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/42
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 294
username: Jack_sparrow1
post_number: 42
topic_id: 171141
---

**[Discussion Image by Jack_sparrow1]** This image depicts a student question in a TDS project discussion, showcasing a traceback error. The error message indicates a `KeyError: 'AIRPROXY_TOKEN'`, originating from line 30 of `/app/app.py`, where the code attempts to retrieve the environment variable `AIRPROXY_TOKEN` using `os.environ['AIRPROXY_TOKEN']`. The traceback reveals that the specified environment variable is not set, leading to the `KeyError` during the `getitem` operation within the `os` module. This suggests the student has not properly configured or set the required environment variable before running the application. The resolution will likely involve setting the `AIRPROXY_TOKEN` environment variable to the correct value.Y_TOKEN'`, arising from line 30 of the `/app/app.py` file. This line attempts to retrieve the value of the environment variable "AIRPROXY_TOKEN" using `os.environ['AIRPROXY_TOKEN']`. The `KeyError` signifies that the specified environment variable is not defined or accessible within the current environment. This likely points to a configuration issue where the student hasn't properly set the `AIRPROXY_TOKEN` environment variable before running the script." alt="image" data-base62-sha1="xqSaHAFarUTS4I13ycaCKbHTBFc" width="633" height="197">image633×197 4.25 KB
