---
chunk_id: discourse_topic_171141_post_431_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/431
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 483
username: 24ds3000090
post_number: 431
topic_id: 171141
---

aransh_Saini @carlton

As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.

---

**[Discussion Image by 24ds3000090]** This image shows instructions for a project, including steps to create a Dockerfile, publish the Docker image to Docker Hub, and run the image using a `podman run` command. The `podman run` command includes flags to remove the container after it exits (`--rm`), set an environment variable (`-e AIPROXY_TOKEN=$AIPROXY_TOKEN`), map port 8000 (`-p 8000:8000`), and specify the image name (`$IMAGE_NAME`). Running the image should automatically serve the API at the specified localhost URLs. The instructions also require students to submit their GitHub repository URL and Docker image name via a Google Form, with placeholders for `user-name` and `repo-name`. This is likely project guidelines, offering step-by-step instructions, and it could be used for both instructor clarification and peer discussion around implementation details.age runs correctly using the provided `podman run` command with environment variables and port mapping: `podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`, which should serve the API at `http://localhost:8000/run?task=...` and `http://localhost:8000/read?path=...`. Finally, it directs the student to submit their GitHub repository URL (using the format `https://github.com/user-name/repo-name`) and Docker image name (using the format `user-name/repo-name`) in a Google Form. These instructions are a likely source of questions/confusion for students due to the syntax of the `podman` command and the required URLs." alt="Screenshot 2025-04-07 233513" data-base62-sha1="hCTkBDgDY5RETIdMAkhDpLOtTex" width="690" height="168" data-dominant-color="39444A">Screenshot 2025-04-07 233513805×197 9.52 KB
