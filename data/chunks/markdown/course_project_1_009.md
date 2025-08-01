---
chunk_id: course_project_1_009
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 527
---

ed differently. It may use a different prettier version. But the broad task is the same.
2. Call `GET http://localhost:8000/read?path=/data/format.md` and get the revised file contents.
3. Verify that the response was formatted using `prettier@3.4.2`.

Here's how we will score the results.

---

- **Pre-requisites**: Your repository **MUST** meet the following criteria to be eligible for evaluation
 - Your GitHub repository exists and is publicly accessible
 - Your GitHub repository has a `LICENSE` file with the MIT license
 - Your GitHub repository has a valid `Dockerfile`
 - Your Docker image is publicly accessible and runs via `podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`
 - Your Docker image uses the same Dockerfile as in your GitHub repository
- **Phase A: 10 marks**. 1 mark for each Phase A task that the agent handles correctly.
 - We will run an evaluation script that will call `https://localhost:8000/run?task=...` on the task and call `https://localhost:8000/read?path=...` to verify the output
- **Phase B: 10 marks**. 1 mark for each Phase B task that the agent handles correctly.
 - The evaluation script will call `https://localhost:8000/run?task=...` on the task and call `https://localhost:8000/read?path=...` to verify the output
- **Bonus: Additional tasks**. We _may_ pass additional tasks beyond the list above. If your code handles them correctly, you get 1 bonus mark per task.
- **Bonus: Code diversity**. You're encouraged to copy code and learn from each other. We encourage diversity too. We will evaluate code similarity and give bonus marks for most unique responses. (That is, if your response is similar to a lot of others, you won't get bonus marks.)

Your score will be the sum of the marks above. No normalization, i.e. whether it's 0/20 or 22/20, what you get is what you get.

This execution will be automated via:

- [`validate.py`](project-1/validate.py) to check the pre-requisites and generate the eligible `images.txt`
- `export AIPROXY_TOKEN=...` to set the AI Proxy token
- [`run.sh`](project-1/run.sh) to evaluate all submissions.
