---
chunk_id: discourse_topic_165959_post_244_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/244
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 315
username: AryanTikam
post_number: 244
topic_id: 165959
---

. Therefore, the student needs to investigate the naming of the GitHub Actions run to include the specified email component. 2x" data-dominant-color="292A2E">Screenshot from 2025-02-09 17-40-581599×155 26.4 KB

---

Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.

main.yml:

`name: Daily Commit Workflow

on:
 schedule:
 - cron: '10 17 * * *' 
 workflow_dispatch:

jobs:
 commit:
 runs-on: ubuntu-latest

steps:
 - name: Checkout repository
 uses: actions/checkout@v3

- name: Add commit using 23f2001216@ds.study.iitm.ac.in
 env:
 PAT: ${{ secrets.PAT }} # PAT stored as a secret
 run: |
 git config --global user.name "Aryan"
 git config --global user.email "23f2001216@ds.study.iitm.ac.in"

echo "Daily commit on $(date)" &gt;&gt; daily-log.txt

git add daily-log.txt
 git commit -m "Automated daily commit on $(date)"

ls -la
 git status

git push origin main 
 git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main
`
