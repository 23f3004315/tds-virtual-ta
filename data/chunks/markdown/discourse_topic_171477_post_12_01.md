---
chunk_id: discourse_topic_171477_post_12_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171477/12
source_title: Project 1 Evaluation second mail is not correct and reports files missing while they are present
content_type: discourse
tokens: 478
username: Sudhishnarayan
post_number: 12
topic_id: 171477
---

ourse.onlinedegree.iitm.ac.in/t/171477/12)

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below

---

**[Discussion Image by Sudhishnarayan]** This image depicts a student's terminal output showing the successful execution of a Docker build and run process, indicating a peer discussion or instructor guidance scenario. The build output shows steps like copying files, installing requirements via `pip install -r requirements.txt`, and exporting the image layers and manifests. Following the successful build, the student executes the command `docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586b49` to run the container. The subsequent INFO messages confirm the successful startup of the application, with Uvicorn running on `http://0.0.0.0:8000`, suggesting the troubleshooting process successfully resolved any initial "files missing" issues by ensuring the Docker image build and runtime environment were properly configured.yers, setting the working directory, copying files (like 'requirements.txt'), and running 'pip install'. The image shows that Docker is building an image from the Dockerfile, installing dependencies specified in the requirements.txt file and exporting layers. Finally, the student runs the Docker container using `docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586b49`, mapping port 8000, and the logs then indicate "Application startup complete" and that Uvicorn is running, suggesting a successful deployment." alt="Screenshot 2025-04-12 115342" data-base62-sha1="dBsRyoAfPZZ0uPWv6BaWMFfsBWM" width="690" height="330" data-dominant-color="141C22">Screenshot 2025-04-12 1153421466×702 50.4 KB
