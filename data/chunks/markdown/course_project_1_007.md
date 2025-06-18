---
chunk_id: course_project_1_007
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 270
---

FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog)
 the URL of your GitHub repository (`https://github.com/user-name/repo-name`) and your Docker image name (`user-name/repo-name`)

Note:

---

- **Use the `AIPROXY_TOKEN` environment variable**. DON'T commit your AI Proxy token to your repository. Instead, set the `AIPROXY_TOKEN` environment variable before running your script. Use `os.environ["AIPROXY_TOKEN"]` as the token in your script.
- **Use your AI Proxy token**. Your [AI Proxy token](https://aiproxy.sanand.workers.dev/) now has a $1 limit. You may use it. If you run out of tokens, ask the TDS team for more. (But try and avoid that.)
- **Stick to GPT-4o-Mini**. This is the only generation model that AI Proxy currently supports. When this page says "LLM", it means GPT-4o-Mini.
- **Keep your prompts short and concise**. Each call to `/run` and `/read` must complete within 20 seconds.
