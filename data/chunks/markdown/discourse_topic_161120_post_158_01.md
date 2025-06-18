---
chunk_id: discourse_topic_161120_post_158_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/158
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 1006
username: Jivraj
post_number: 158
topic_id: 161120
---

](https://discourse.onlinedegree.iitm.ac.in/t/161120/158)

Hi @23f2000573 ,

As error mentions to add tag to image.

Adding different tags is like versioning your docker image, image with a particular tag can be pulled.

For adding tag use

---

**[Discussion Image by Jivraj]** This image is from a student discussion thread focusing on container deployment tools, specifically showing command-line instructions. It gives a step-by-step guide on building, running, and deploying a container named `py-hello` using `podman`. First, the user must create a Docker Hub account and log in using `podman login docker.io`. The commands provided are for building the image (`podman build -t py-hello .`), running it interactively (`podman run -it py-hello`), and pushing it to Docker Hub. The push command includes a placeholder `$DOCKER_HUB_USERNAME` which users need to replace with their actual Docker Hub username, and an example of tagging the image with "dev" (`TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG`).t docker.io/$DOCKER_HUB_USERNAME/py-hello`. Lastly, it shows how to push the container with a specific tag, such as "dev", using `TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG`. This post likely aims to help students understand the basic workflow for containerizing applications and pushing them to a container registry." alt="image" data-base62-sha1="hB9lW2tQ5rKxQfOECDJcZMvB4Ve" width="690" height="295" srcset="**[Discussion Image by Jivraj]** This image shows an instructor's post, providing step-by-step commands to build, run, and deploy a container using Podman. The instructions begin with creating an account on Docker Hub and logging in using `podman login docker.io`. Next, commands are provided to build and run the container: `podman build -t py-hello .` and `podman run -it py-hello`. The post continues to guide users on how to push the container to Docker Hub, emphasizing the need to replace `$DOCKER_HUB_USERNAME` with their actual Docker Hub username, using the command `podman push py-hello:latest docker.io/$DOCKER_HUB_USERNAME/py-hello`. Finally, the post explains how to push the container with a specific tag (e.g., "dev"), using the command `TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG`., **[Discussion Image by Jivraj]** This image shows a code snippet providing instructions on how to build, run, and deploy a container using `podman`, which is likely part of instructor-provided materials or guidance. The instructions include the following steps: logging into Docker Hub using `podman login docker.io`, building and running the container with commands `podman build -t py-hello .` and `podman run -it py-hello`, pushing the container to Docker Hub after replacing `$DOCKER_HUB_USERNAME` with the user's Docker Hub username using `podman push py-hello:latest docker.io/$DOCKER_HUB_USERNAME/py-hello`, and pushing a specific tag (e.g., `dev`) with `TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG`. These commands guide students through the standard containerization workflow, from local development to deployment on Docker Hub, with an explanation on how to tag containers. 1.5x, **[Discussion Image by Jivraj]** This image is from a student discussion on deployment tools, specifically using Podman. The image provides a series of commands to build, run, and deploy a container. First, it instructs the user to create an account on Docker Hub and then login using `podman login docker.io`. Then, it shows how to build the container with `podman build -t py-hello .` and run it interactively with `podman run -it py-hello`. Finally, the instructions show how to push the container to Docker Hub, reminding the user to replace `$DOCKER_HUB_USERNAME` with their actual Docker Hub username using the command `podman push py-hello:latest docker.io/$DOCKER_HUB_USERNAME/py-hello`, and how to add a specific tag, e.g. dev, using `TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG`. These commands appear to be provided as a reference or a solution for deploying a "py-hello" container. 2x" data-dominant-color="161B21">image1351×578 40.8 KB
