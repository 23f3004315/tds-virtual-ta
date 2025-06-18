---
chunk_id: discourse_topic_171141_post_427_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/427
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 229
username: 23F300327
post_number: 427
topic_id: 171141
---

## Post #427 by 23F300327

**Direct Link**: [Post #427](https://discourse.onlinedegree.iitm.ac.in/t/171141/427)

My code uses `npx` to format Markdown files using Prettier, specifically via `subprocess.run(["npx", "prettier@3.4.2", "--write", ...])`, which assumes that `npx` is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or `npx`, this results in an error during evaluation.

To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

bash:` apt-get update &amp;&amp; apt-get install -y nodejs npm`

Once installed, `npx prettier@3.4.2` should work as expected.

For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where `npx` is available by default.
