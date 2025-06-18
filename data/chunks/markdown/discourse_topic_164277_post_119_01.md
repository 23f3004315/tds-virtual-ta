---
chunk_id: discourse_topic_164277_post_119_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/119
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 449
username: 23f1002104
post_number: 119
topic_id: 164277
---

**[Discussion Image by 23f1002104]** This image depicts a student's terminal, showing an error encountered while running a Python script for Project 1 of the TDS course. The student, abhro014, is attempting to execute a script called `datagen.py` from a remote URL using the command `uv run https://raw.githubusercontent.com/sanand/tools-in-data-science-public/tds-2025-01/project-1/datagen.py 23f1002104@ds.study.iitm.ac.in`. The error message "PermissionError: [Errno 13] Permission denied: '/data'" indicates that the script is trying to create a directory named `/data`, but the user does not have the necessary permissions to do so, which typically suggests file system permission issues on the student's system. The traceback points to the `os.makedirs` function in the script as the source of the problem, specifically line 284 in the `/tmp/datagen2eQ208.py` file, which attempts to create the directory based on a configuration value "root". A possible solution or workaround would involve changing the script to create the data directory in a location where the student has write permissions, or modifying permissions of the /data directory./raw.githubusercontent.com/sanand.../datagen.py`. The traceback indicates that the error occurs during the `os.makedirs` call in the script, specifically when trying to create a directory named '/data'. The error message "Permission denied: '/data'" signifies that the user account running the script does not have the necessary permissions to create directories in the root ('/') directory, which is usually restricted. This highlights a potential issue where the script is trying to create a directory in a location without appropriate permissions, requiring modification of the script or granting necessary permissions to the user." alt="Screenshot 2025-02-11 181453" data-base62-sha1="qcYKVrgkNokn9jbch4vRvh7U3Aq" width="690" height="97" data-dominant-color="181518">Screenshot 2025-02-11 1814531459×207 15.3 KB
