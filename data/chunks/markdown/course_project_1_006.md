---
chunk_id: course_project_1_006
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 402
---

 Convert Markdown to HTML
- **B10**. Write an API endpoint that filters a CSV file and returns JSON data

Your agent must handle these tasks as well.

The business team has _not_ promised to limit themselves to these tasks. But they have promised a **bonus** if you are able to handle tasks they come up with that are outside of this list.

---

## Deliverables

- [Create a new _public_ GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Add an MIT `LICENSE` file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)
- Write and test your code. Call `POST /run?task=...` with a few tasks and check if `GET /read?path=...` creates the correct files.
- Commit and push your code
- Create a [Dockerfile](https://docs.docker.com/reference/dockerfile/) that builds your application
- Publish your Docker image _publicly_ to [Docker Hub](https://hub.docker.com/)
- Ensure that running your image via `podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME` automatically serves the API at `http://localhost:8000/run?task=...` and `http://localhost:8000/read?path=...`
- [Submit in this Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog)
 the URL of your GitHub repository (`https://github.com/user-name/repo-name`) and your Docker image name (`user-name/repo-name`)

Note:
