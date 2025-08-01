---
chunk_id: discourse_topic_167072_post_2_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167072/2
source_title: Sudo permission needed to create data folder in root?
content_type: discourse
tokens: 303
username: carlton
post_number: 2
topic_id: 167072
---

## Post #2 by carlton

**Direct Link**: [Post #2](https://discourse.onlinedegree.iitm.ac.in/t/167072/2)

Hi Vikram,

This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py

Inside the docker container, permission for the data folder is set by the Dockerfile

which then allows your application to access the root folder inside your docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

You create your application server that serves 2 endpoints on localhost:8000
You create a docker image that runs this application server.
You run the docker image using podman as described in the project page.
For mimicking the testing conditions. You need two files:

evaluate.py and datagen.py to be in the same folder where you are running these two scripts.
Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.

Hope that gives clarity.
