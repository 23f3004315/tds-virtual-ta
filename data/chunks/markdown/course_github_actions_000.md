---
chunk_id: course_github_actions_000
source_url: https://tds.s-anand.net/#/github-actions
source_title: github-actions
content_type: course
tokens: 458
---

## CI/CD: GitHub Actions

[GitHub Actions](https://github.com/features/actions) is a powerful automation platform built into GitHub. It helps automate your development workflow - running tests, deploying applications, updating datasets, retraining models, etc.

- Understand the basics of [YAML configuration files](https://docs.github.com/en/actions/writing-workflows/quickstart)
- Explore the [pre-built actions from the marketplace](https://github.com/marketplace?type=actions)
- How to [handle secrets securely](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Triggering a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
- Staying within the [free tier limits](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)
- [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)

Here is a sample `.github/workflows/iss-location.yml` that runs daily, appends the International Space Station location data into `iss-location.json`, and commits it to the repository.

```yaml
name: Log ISS Location Data Daily

on:
 schedule:
 # Runs at 12:00 UTC (noon) every day
 - cron: "0 12 * * *"
 workflow_dispatch: # Allows manual triggering

jobs:
 collect-iss-data:
 runs-on: ubuntu-latest
 permissions:
 contents: write

steps:
 - name: Checkout repository
 uses: actions/checkout@v4

- name: Install uv
 uses: astral-sh/setup-uv@v5

- name: Fetch ISS location data
 run: | # python
 uv run --with requests python << 'EOF'
 import requests

data = requests.get('http://api.open-notify.org/iss-now.json').text
 with open('iss-location.jsonl', 'a') as f:
 f.write(data + '\n')
 'EOF'
