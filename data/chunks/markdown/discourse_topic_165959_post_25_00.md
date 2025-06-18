---
chunk_id: discourse_topic_165959_post_25_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/25
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 264
username: 23f2003853
post_number: 25
topic_id: 165959
---

## Post #25 by 23f2003853

**Direct Link**: [Post #25](https://discourse.onlinedegree.iitm.ac.in/t/165959/25)

Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following

" name: Daily Commit

on:

schedule:

- cron: ‘0 12 * * *’ # Runs daily at 12:00 PM UTC

workflow_dispatch: # This allows manual trigger

jobs:

commit:

runs-on: ubuntu-latest

`steps:
- name: Checkout repository
 uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
 run: |
 echo "This is a daily commit" &gt; daily_commit.txt
 git config --global user.email "23f2003853@ds.study.iitm.ac.in"
 git config --global user.name "23f2003853"
 git add daily_commit.txt
 git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
 git push"
`
@Jivraj can help me to fix the issue
