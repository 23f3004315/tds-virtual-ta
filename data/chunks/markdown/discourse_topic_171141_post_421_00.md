---
chunk_id: discourse_topic_171141_post_421_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/421
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 294
username: 22f3002902
post_number: 421
topic_id: 171141
---

## Post #421 by 22f3002902

**Direct Link**: [Post #421](https://discourse.onlinedegree.iitm.ac.in/t/171141/421)

Dear @carlton

This is Senthur. I have reviewed the logs, and it indicates that the

`/app/app/main.py` file is missing. However, in my project directory, the

`main.py` file is located in the `app/` folder, and the `run.py` file is in the root folder of the project, which is `LLM_Automation_Agent` . This structure allows the `run.py` file to run the project without any issues by calling the appropriate functions from `app/main.py`.

To run the project, the command I used is:

`python run.py
`
Since `run.py` is placed in the root folder and not in any subfolder, it should properly execute the project without any errors, as it redirects the calls to `app/main.py`.

I believe the evaluation may have been incorrect because the project was not executed in the way it was intended. I kindly request you to re-run the project using the `run.py` script located in the root folder (`llm-automation-agent`).

For your reference, I have attached screenshots from my local machine where the project was tested successfully, along with my GitHub screenshot.

Here is the GitHub link to my project:

github.com
