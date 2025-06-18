---
chunk_id: discourse_topic_171477_post_11_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171477/11
source_title: Project 1 Evaluation second mail is not correct and reports files missing while they are present
content_type: discourse
tokens: 464
username: Sudhishnarayan
post_number: 11
topic_id: 171477
---

ourse.onlinedegree.iitm.ac.in/t/171477/11)

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below

---

**[Discussion Image by Sudhishnarayan]** This image shows a command-line terminal output, likely representing a student's attempt to run a Docker container for a TDS (presumably a class or project) application. The top section details the Docker image build process, including extracting layers, copying files (specifically `requirements.txt` to `/app/`), and running `pip install --no-cache-dir -r requirements.txt`. The process ends with naming and unpacking the image to `docker.io/library`. Next, the student executes the `docker run` command, setting the AIPROXY_TOKEN environment variable and mapping port 8000. The output confirms the server started, the application is running, and Uvicorn is serving the application on `http://0.0.0.0:8000`. This indicates a successful build and deployment, addressing initial concerns about missing files reported by the evaluation, suggesting a potential misunderstanding of the image building process..txt), and running pip install to install dependencies based on the requirements file. After building, the image is named and unpacked to docker.io/library/. The next command is a `docker run` command specifying environment variables (AIPROXY_TOKEN) and port mapping (8000:8000), followed by the image ID. The final part indicates that the server has started and is running the Uvicorn application on `http://0.0.0.0:8000`, signaling successful startup. This image likely represents a successful execution of the container, indicating the student may have resolved their "missing files" issue previously discussed." alt="Screenshot 2025-04-12 115342" data-base62-sha1="dBsRyoAfPZZ0uPWv6BaWMFfsBWM" width="690" height="330" data-dominant-color="141C22">Screenshot 2025-04-12 1153421466×702 50.4 KB
