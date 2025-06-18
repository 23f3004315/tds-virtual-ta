---
chunk_id: discourse_topic_164277_post_141_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/141
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 248
username: 22f3001307
post_number: 141
topic_id: 164277
---

## Post #141 by 22f3001307

**Direct Link**: [Post #141](https://discourse.onlinedegree.iitm.ac.in/t/164277/141)

Hi @carlton @Jivraj,

I followed what you taught in Feb 11 session and tried implementing task A1. My understanding is once i run the subprocess, datagen.py file should be run and /data folder should be created in the project folder. But it is not happening to me. I am getting the following error

`Traceback (most recent call last):
 File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/datagen4COEF3.py", line 284, in &lt;module&gt;
 os.makedirs(config["root"], exist_ok=True)
 ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 File "&lt;frozen os&gt;", line 227, in makedirs
OSError: [Errno 30] Read-only file system: '/data'
`
If i can’t automate this process, i don’t see the point writing code for other tasks. Can anyone help me solving this error?
