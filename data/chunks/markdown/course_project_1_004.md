---
chunk_id: course_project_1_004
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 353
---

- **A10**. The SQLite database file `/data/ticket-sales.db` has a `tickets` with columns `type`, `units`, and `price`. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the "Gold" ticket type? Write the number in `/data/ticket-sales-gold.txt`

---

Developers will call the `/run?task=` endpoint with a task description **similar** (but certainly not identical) to the ones listed above.

For example, **Task A3** can be written in these ways - all are equivalent.

- The file `/data/dates.txt` contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to `/data/dates-wednesdays.txt`
- Write the # of Thursdays in `/data/extracts.txt` into `/data/extracts-count.txt`
- `/data/contents.log` में कितने रविवार हैं? गिनो और /data/contents.dates में लिखो
- `/data/contents.log`ல எத்தனை ஞாயிறு இருக்குனு கணக்கு போட்டு, அதை `/data/contents.dates`ல எழுது

Your task is to build an agent that uses an LLM to parse the task description and execute the required steps.
