---
chunk_id: course_github_actions_001
source_url: https://tds.s-anand.net/#/github-actions
source_title: github-actions
content_type: course
tokens: 521
---

uv@v5

- name: Fetch ISS location data
 run: | # python
 uv run --with requests python << 'EOF'
 import requests

data = requests.get('http://api.open-notify.org/iss-now.json').text
 with open('iss-location.jsonl', 'a') as f:
 f.write(data + '\n')
 'EOF'

---

- name: Commit and push changes
 run: | # shell
 git config --local user.email "github-actions[bot]@users.noreply.github.com"
 git config --local user.name "github-actions[bot]"
 git add iss-location.jsonl
 git commit -m "Update ISS position data [skip ci]" || exit 0
 git push
```

Tools:

- [GitHub CLI](https://cli.github.com/): Manage workflows from terminal
- [Super-Linter](https://github.com/github/super-linter): Validate code style
- [Release Drafter](https://github.com/release-drafter/release-drafter): Automate releases
- [act](https://github.com/nektos/act): Run actions locally

[**[Course Image: Github Actions CI/CD - Everything you need to know to get started]** GitHub Actions are a powerful automation tool directly integrated into GitHub repositories, allowing you to automate tasks in your software development workflow. You can configure Actions to run when specific events occur in your repository, such as a code push, pull request, or even on a scheduled basis. This enables you to automate various processes like building, testing, and deploying your code. The image shows a visual representation of a GitHub Actions workflow, illustrating the sequence of automated tasks that can be defined. By using GitHub Actions effectively, developers can streamline their CI/CD pipelines and improve efficiency.on to GitHub Actions, a CI/CD tool that automates software workflows directly in your GitHub repository. The image visually represents a workflow diagram, where a trigger initiates a series of automated steps (jobs) to build, test, and deploy code. By utilizing GitHub Actions, developers can streamline their development processes, ensuring code quality and faster release cycles through automated checks and deployments. Understanding GitHub Actions is crucial for implementing continuous integration and continuous delivery in TDS projects, allowing for automated testing and deployment pipelines. This helps catch errors early and reduces the manual effort required for software releases.)](https://youtu.be/mFFXuXjVgkU)

- [How to handle secrets in GitHub Actions](https://youtu.be/1tD7km5jK70)
