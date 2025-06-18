---
chunk_id: discourse_topic_169029_post_341_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/341
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 362
username: Algsoch
post_number: 341
topic_id: 169029
---

 or execute even moderately dynamic queries.

Then I thought—what if I manually mapped questions and answers using a **static JSON structure**? That quickly broke when users passed **different parameters, different files**, or queried in **non-standard formats** like “code -s” or “code -v”.

---

The next idea: write **individual Python scripts per question** from our Graded Assignments (GA1–GA5). But that lacked flexibility and reusability. Creating multiple files became unmanageable and non-scalable.

The Breakthrough: Dynamic Function Mapping
After multiple iterations and failed prototypes, I finally found the right architecture:

Centralized engine in `vicky_server.py`

Uses **regex-based pattern matching** to detect question types, extract parameters, and identify the correct solution

Each solution is a structured Python function like `ga1_first_solution(query=None)`

Supports dynamic parameter injection, command-line variations, file-based queries, and more

Acts like a **mini compiler for data science tools**

Presenting Vicky – The Mini Chatbot for TDS 
Vicky is a **smart, modular chatbot** built specifically for **Tool for Data Science at IIT Madras**. It’s packed with real functionality—not just templates.

Key Features:
 **Graded Assignment Solver**

Handles dynamic, real-world questions from GA1 to GA5 like:

`code -s` / `code -v` → VS terminal commands
Create FastAPI API for CSV with filtering/searching
GitHub automation: repo creation, GitHub Actions setup
Data cleaning, scraping from IMDb, image compression

**File Upload with Query Matching**

Users can upload a file (CSV, JSON, Excel) and ask file-specific queries. The system understands context and dynamically links the query to the uploaded file.
