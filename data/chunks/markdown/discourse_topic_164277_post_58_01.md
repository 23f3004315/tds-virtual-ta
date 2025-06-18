---
chunk_id: discourse_topic_164277_post_58_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/58
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 206
username: 23f1002382
post_number: 58
topic_id: 164277
---

 sqlite3; print(sqlite3.sqlite_version)"

- cd to latest_ai_development and run cmd [ crewai run] which set up server 
- Then in a separate bash terminal run "python evaluate.py" 
- also make sure to enter openai or sanand api key in crew.py

---

# Simple history of commands
1. Terminal 1 
 - 1 python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
 - 2 export PATH=/opt/conda/bin:$PATH
 - 3 export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
 - 4 python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
 - 5 cd latest_ai_development/
 - 7 pip install crewai crewai-tools
`

This file has been truncated. show original

My take on autonomous agents. Limited by model capabilities to some extent. Will use function calling hence forth but here is a quick look at using crewai for agent tasks.
