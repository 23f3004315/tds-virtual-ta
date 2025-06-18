---
chunk_id: course_project_1_005
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 363
---

ுக்குனு கணக்கு போட்டு, அதை `/data/contents.dates`ல எழுது

Your task is to build an agent that uses an LLM to parse the task description and execute the required steps.

---

## Phase B: Handle Business Tasks

The DataWorks security team has added the following requirements. No matter what the task is, the agent must ensure that:

- **B1**. Data outside `/data` is never accessed or exfiltrated, even if the task description asks for it
- **B2**. Data is never deleted anywhere on the file system, even if the task description asks for it

The DataWorks business team has listed _broad_ additional tasks for automation. But they have not defined it more precisely than this:

- **B3**. Fetch data from an API and save it
- **B4**. Clone a git repo and make a commit
- **B5**. Run a SQL query on a SQLite or DuckDB database
- **B6**. Extract data from (i.e. scrape) a website
- **B7**. Compress or resize an image
- **B8**. Transcribe audio from an MP3 file
- **B9**. Convert Markdown to HTML
- **B10**. Write an API endpoint that filters a CSV file and returns JSON data

Your agent must handle these tasks as well.

The business team has _not_ promised to limit themselves to these tasks. But they have promised a **bonus** if you are able to handle tasks they come up with that are outside of this list.
