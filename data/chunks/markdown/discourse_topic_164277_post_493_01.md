---
chunk_id: discourse_topic_164277_post_493_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/493
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 257
username: 22f3000819
post_number: 493
topic_id: 164277
---

 passes. I can’t understand why this is happening.

I also ran the image in both docker and podman in interactive mode as show in the below snippet from terminal.

When run using docker, `which node` gives `/usr/bin/node` as output but when run using podman, nothing.

---

`shiva@shiva:~/Desktop/tdsp1$ sudo podman run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo docker run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
/usr/bin/node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --user=root --rm -it docker.io/myusername/myreponame /bin/sh
# which node
# which node
# exit
`
