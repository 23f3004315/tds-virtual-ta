---
chunk_id: discourse_topic_165959_post_27_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/27
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 200
username: daksh76
post_number: 27
topic_id: 165959
---

## Post #27 by daksh76

**Direct Link**: [Post #27](https://discourse.onlinedegree.iitm.ac.in/t/165959/27)

name: Daily Commit

on:

schedule:

- cron: ‘0 0 * * *’ # Runs once a day at midnight UTC

workflow_dispatch: # Allows manual triggering of the workflow

jobs:

commit:

runs-on: ubuntu-latest

`steps:
- name: Checkout repository
 uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
 run: |
 echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" &gt;&gt; daily_commit.txt
 git add index.html
 git commit -m "Daily commit"
 git push
 env:
 GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
`
sir this is my code and im getting a error in this
