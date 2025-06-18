---
chunk_id: discourse_topic_171141_post_103_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/103
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 334
username: 22f3000519
post_number: 103
topic_id: 171141
---

**[Discussion Image by 22f3000519]** This image shows a traceback from a student's code, indicating a `KeyError: 'USER_EMAIL'`. The traceback reveals the error originates in `/app/main.py`, line 22, where the code attempts to access the `USER_EMAIL` environment variable using `os.environ["USER_EMAIL"]`. The error signifies that the `USER_EMAIL` environment variable is not set. This implies the student needs to define the `USER_EMAIL` environment variable for their application to function correctly; the specific steps to do so depend on their deployment environment. This represents a common issue faced when applications rely on environment variables for configuration.22 of `/app/main.py`, where the code attempts to access the environment variable `USER_EMAIL` using `os.environ["USER_EMAIL"]`. The error means that the `USER_EMAIL` environment variable is not set when the application is run, causing the program to crash when it tries to retrieve the value. To resolve this, the student needs to ensure the `USER_EMAIL` environment variable is properly set before running the Uvicorn server, potentially by setting it in their shell environment or using a `.env` file loaded with a library like `python-dotenv`. This is a peer discussion as the student likely posted the error to get help from peers." alt="Screenshot (423)" data-base62-sha1="jRv3cgpzOzFxkgTGnj3fAbSqqEW" width="690" height="415" data-dominant-color="F1F1F2">Screenshot (423)1486×895 43.2 KB
