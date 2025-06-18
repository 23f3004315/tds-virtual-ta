---
chunk_id: discourse_topic_169029_post_28_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/28
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 296
username: 23f1001231
post_number: 28
topic_id: 169029
---

 which we have to install in the vercel instance using `apt` package manager.

But, Vercel does not provide sudo access which is required to install packages.
In GA 2 ques 10, we have to use local LLM (Llamafile), will vercel allow that?

---

Also after that, we have to give answer as the ngrok public url for which we have to first install `ngrok` package.
In GA 2 ques 8, uploading an image to Dockerhub requires `docker` package installed.
In GA 2 ques 6, Deploy a Python API to Vercel in a Vercel instance?
Many ques require writing and running FastAPI server to serve data with CORS enabled. Can Vercel allow/do that?
And many more

Most tasks mentioned above like installing packages etc. requires sudo privilages or may face restrictions set by Vercel.

Vercel does not provide sudo access or any form of root access to its hosting environment which is required to perform the above tasks.

Many of these task can be done in our local systems (exposing to internet using cloudflare tunnels/ngrok), but we cannot run our systems 24*7 during evaluation.

I can see only one option left that is renting a VPS from server providers like digitalocean, gcp, aws etc, which will provide us sudo access and 100% uptime.

Also, some ques requires external toolings like
