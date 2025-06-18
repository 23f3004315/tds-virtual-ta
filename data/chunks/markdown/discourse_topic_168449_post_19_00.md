---
chunk_id: discourse_topic_168449_post_19_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/19
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 238
username: shubhamatkal
post_number: 19
topic_id: 168449
---

## Post #19 by shubhamatkal

**Direct Link**: [Post #19](https://discourse.onlinedegree.iitm.ac.in/t/168449/19)

Hello @carlton sir , for me given constituency was `"SRI GOBINDPUR"`

and in the dataset there are multiple names for this constituency i think over the period names were changed of this constituency

i have filtered constituencies from punjab using below code in colab

`df_gobindpur = df[df["AC"].str.contains("SRI GOBINDPUR|SRIHARGOBINDPUR|SRI HARGOBINDPUR", case=False, na=False)]
`
is this correct approach or i have to consider only SRI GOBINDPUR name only? but then this constituency is not availble after 1957

using above filtering i got below data for SRI GOBINDPUR

drive.google.com

df_gobindpur.csv

Google Drive file.

then i used margin formula as

`margin_percentage = ((winner_votes - runner_up_votes) / total_votes) * 100
`
using this i got answer for 1st question as
