---
chunk_id: discourse_topic_164277_post_35_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/35
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 348
username: 23f1002382
post_number: 35
topic_id: 164277
---

-312-x86_64-linux-gnu.so: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
`
i updated the libffi package using sudo but while breaking something else can someone pls help me? @carlton @Jivraj @s.anand

---

history of commands in new codespace

` 1 crewai --version
 2 pip install crewai crewai-tools
 3 python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
 4 export PATH=/opt/conda/bin:$PATH
 5 export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
 6 python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
 7 crewai create crew &lt;project_name&gt;
 8 crewai create crew b2b
 9 history
`

UPDATE: IT’s WORKING if you do this in order

` 1 python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
 2 export PATH=/opt/conda/bin:$PATH
 3 export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
 4 python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
 5 pip install --no-cache-dir --force-reinstall typing_extensions pydantic crewai crewai-tools
 6 conda install -c conda-forge typing_extensions
 7 exec bash
 8 crewai create crew "Project 1 - LLM-based Automation Agent"
`
Something about different environment conda and python can the instructors please help me understand it(resources ), so i can trouble shoot this later with better accuracy come precision
