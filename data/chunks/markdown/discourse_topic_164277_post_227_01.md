---
chunk_id: discourse_topic_164277_post_227_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/227
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 328
username: vidushi
post_number: 227
topic_id: 164277
---

**[Discussion Image by vidushi]** This image captures a student question in the TDS Project 1 discussion thread. The student, vidushi, is attempting to run the `app.py` file using the command `uv run app.py` within the `tds-project-1` environment. However, the execution fails with a `ModuleNotFoundError: No module named 'fastapi'`. This error indicates that the `fastapi` library, which is imported in the `app.py` file, is not installed in the current Python environment. The traceback specifies that the error occurs on line 9 of `/home/vidushilinux/tds-project-1/app.py` due to the `from fastapi import FastAPI` statement. To resolve this issue, the student will need to install the `fastapi` package using a package manager like `pip` or `uv`.t the error occurs on line 9 of `app.py` when trying to import `FastAPI`. The specific error message is "ModuleNotFoundError: No module named 'fastapi'", which means the FastAPI library is not installed in the student's Python environment. The command `uv run app.py` was used to run the application, which likely uses the uv package manager. To resolve this, vidushi needs to install FastAPI using a package manager such as `pip install fastapi`." alt="image" data-base62-sha1="oFVA3JKtDSmA2FNzMT1OoeZWyHj" width="671" height="109">image671×109 8.64 KB
