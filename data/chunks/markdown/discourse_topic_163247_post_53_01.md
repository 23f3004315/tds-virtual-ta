---
chunk_id: discourse_topic_163247_post_53_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/53
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 356
username: 22f2000113
post_number: 53
topic_id: 163247
---

**[Discussion Image by 22f2000113]** This image shows a Python error message, specifically a `ModuleNotFoundError` for the 'scipy' module within a Pyodide environment. The traceback indicates the error occurred while executing code, and the message explicitly states that 'scipy' is part of the Pyodide distribution but not yet installed. The error message provides two solutions: install 'scipy' using `await micropip.install("scipy")` in Python or `await pyodide.loadPackage("scipy")` in JavaScript. A link to the Pyodide documentation on loading packages is also included for further guidance. This likely represents a student's question about how to resolve this dependency issue when using Pyodide in the course. error is a "ModuleNotFoundError" indicating that the 'scipy' module is not installed, despite being part of the Pyodide distribution; the traceback points to the error originating from the file "/lib/python312.zip/_pyodide/_base.py". The error message provides the student with instructions on how to resolve the issue: by running `await micropip.install("scipy")` in Python or `await pyodide.loadPackage("scipy")` in JavaScript, and directs them to the pyodide documentation for further assistance. This suggests the student encountered this error while attempting to use scipy in a Pyodide environment and is likely seeking guidance on the correct installation method." alt="image" data-base62-sha1="eZsMNUCHY7ybnsM46OSmArByV3P" width="690" height="71" data-dominant-color="F6ECED">image1731×180 13.1 KB
