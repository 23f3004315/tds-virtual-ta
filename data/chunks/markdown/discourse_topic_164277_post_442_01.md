---
chunk_id: discourse_topic_164277_post_442_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/442
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 392
username: 21f2000710
post_number: 442
topic_id: 164277
---

**[Discussion Image by 21f2000710]** The image shows a student encountering an error while building a Docker image for the automation agent project, specifically when trying to pull the `python:3.12-slim-bookworm` base image. The error message "failed to resolve source metadata for docker.io/library/python:3.12-slim-bookworm" indicates a problem connecting to the Docker registry to download the specified image. The detailed error reveals HTTP ReadSeeker failures, suggesting network connectivity issues preventing access to the cloudflarestorage.com domain that hosts Docker images, potentially a DNS resolution problem ("no such host") or a general inability to reach the server. The student is running the `docker build` command from the PowerShell terminal, within the `tds_project_1` directory. This is a student question related to a failed build due to docker image retrieval issues.ratik007thala/automation-agent". The build process fails while trying to load metadata for the base image "python:3.12-slim-bookworm" from docker.io, resulting in an HTTP request error related to resolving source metadata from a Cloudflare storage endpoint. The error message indicates a problem connecting to docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com and states "no such host", suggesting a DNS resolution or network connectivity issue. It seems the student is facing difficulties pulling the specified Python base image, preventing the successful creation of their automation agent Docker image." alt="Screenshot 2025-02-15 212826" data-base62-sha1="eWTsxcch0VyIs8G9dhevCFof78f" width="690" height="178" data-dominant-color="171717">Screenshot 2025-02-15 2128261903×492 32.1 KB
