---
chunk_id: discourse_topic_164277_post_374_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/374
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 218
username: Jaideep
post_number: 374
topic_id: 164277
---

## Post #374 by Jaideep

**Direct Link**: [Post #374](https://discourse.onlinedegree.iitm.ac.in/t/164277/374)

it usually happens in some GNU/Linux OS. since you are using some distribution based on Debian namely Ubuntu or whatever try doing sudo apt install python-packagename (replace package name with fastapi for fastapi)

then it works. It usually happens due to manual intervention with pip3 the user might break some system dependencies which require some python3 package. No need to worry about it.

Another Fix: try using a virtual environment which is highly suggested since there is no chance for you to interfere with the system packages.

create a venv using python3 -m venv name_of_venv

add this line to your .bashrc in ~ folder as source /path/to/your/venv/location

and run source .bashrc. This time no error occurs as you do everything in your virtual environment you can install anything python3 package using pip3 install package name.

It even happened for me
