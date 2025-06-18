---
chunk_id: discourse_topic_171141_post_433_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/433
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 945
username: carlton
post_number: 433
topic_id: 171141
---

 #433 by carlton

**Direct Link**: [Post #433](https://discourse.onlinedegree.iitm.ac.in/t/171141/433)

Hi Haricharan

Your Dockerfile does not build the repo. Its misconfigured.

This is the error when building it:

---

`=&gt; ERROR [8/8] COPY .env /app/ 0.0s
------
 &gt; [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
 18 | # Copy application files
 19 | COPY *.py /app/
 20 | &gt;&gt;&gt; COPY .env /app/
 21 | 
 22 | # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found
`
**[Discussion Image by carlton]** This image represents a code snippet shared in a student discussion on TDS Project 1 discrepancies. The code sets up the application directory using "WORKDIR /app" and copies application files. Specifically, it copies all Python files with the command "COPY *.py /app/" and the .env file with "COPY .env /app/" into the /app directory. An orange rectangle is drawn around the "COPY .env /app/" line, which might be a point of discussion or question in the thread. The code appears to be related to a Dockerfile, where these commands are used to configure the container environment.rrectly copied. The student is likely seeking confirmation or clarification on these Dockerfile commands." alt="Screenshot 2025-04-08 at 11.12.18 am" data-base62-sha1="iWIIlgMm6iiSN3X2eus14cfi7sL" width="690" height="276" srcset="**[Discussion Image by carlton]** This image depicts a code snippet from a Dockerfile, likely shared by a student seeking clarification or confirming correctness during a project. The Dockerfile instructions first set the working directory to `/app` using `WORKDIR /app`. Then, it copies Python files (`*.py`) and the `.env` file to the `/app/` directory inside the Docker container, using the `COPY` command. The red arrow and box around the `COPY .env /app/` line suggest the student is focusing on the inclusion of environment variables during the image build process. The student might be questioning if it's necessary to copy the .env file or if there is a better approach to inject environment variables, such as using Docker's `-e` flag or ENV instruction. This is a snippet that aims to copy all .py files and the .env file to the /app/ directory when building the image., **[Discussion Image by carlton]** This image shows a code snippet from a Dockerfile, specifically commands related to setting up the application directory and copying application files. The `WORKDIR /app` command sets the working directory to `/app`. The line `COPY *.py /app/` copies all Python files (`.py`) to the `/app` directory. A key instruction highlighted with an orange box is `COPY .env /app/`, which copies the `.env` file containing environment variables to the `/app` directory within the Docker image. The surrounding comments indicate these are part of setting up the application environment within the container. 1.5x, **[Discussion Image by carlton]** This image shows a snippet of a Dockerfile, likely part of a project setup, and appears in a student discussion about discrepancies in the project. The Dockerfile first sets the working directory to `/app` using `WORKDIR /app`. It then copies all Python files (`*.py`) and the `.env` file into the `/app` directory. The student discussion likely revolves around the correctness or implications of copying the `.env` file into the Docker image, which could raise security concerns if the image is shared. The line `COPY .env /app/` is highlighted, indicating this might be a point of discussion or confusion. 2x" data-dominant-color="2E2C2B">Screenshot 2025-04-08 at 11.12.18 am754×302 41 KB
