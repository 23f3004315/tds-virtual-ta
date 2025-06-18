---
chunk_id: discourse_topic_164277_post_216_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/216
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 431
username: vikramjncasr
post_number: 216
topic_id: 164277
---

**Direct Link**: [Post #216](https://discourse.onlinedegree.iitm.ac.in/t/164277/216)

@Jivraj sir I get this error

but my app.py is able to get the server running on localhost and not on 0.0.0.

---

**[Discussion Image by vikramjncasr]** This image depicts a student question in the TDS Project 1 discussion, specifically an error encountered while running the automation agent. The student, vikramjncasr, attempts to run a container using the command `podman run 20511982f949`. This results in a traceback originating from `/app/app.py`, indicating a `ModuleNotFoundError: No module named 'fastapi'`. The error suggests that the `fastapi` Python package is not installed within the container environment, causing the application to fail during the import statement. To resolve this, the student needs to install the `fastapi` package inside the container, likely using `pip install fastapi` or a similar package manager command, or rebuild the image after adding the dependency to the requirements.txt file. This indicates a common dependency management issue faced during containerized application development.in `/app/app.py` on the line `import fastapi`, meaning the `fastapi` Python package is not installed within the container environment. The student executed the command `podman run 20511982f949` from the `/mnt/c/IIT_Madras/TDS_Project` directory. This reveals a dependency issue where the required `fastapi` library is missing from the container. To resolve this, the student needs to ensure that the `fastapi` package is included in the container's build process or installed before running the application, potentially using `pip install fastapi` within the container." alt="image" data-base62-sha1="xRq27aO3iKC8e2tH9JXnzpGWF0T" width="690" height="129" data-dominant-color="222425">image1014×190 18.2 KB
