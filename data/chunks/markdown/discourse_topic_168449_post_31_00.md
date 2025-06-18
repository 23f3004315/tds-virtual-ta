---
chunk_id: discourse_topic_168449_post_31_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/31
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 253
username: 23f1002382
post_number: 31
topic_id: 168449
---

## Post #31 by 23f1002382

**Direct Link**: [Post #31](https://discourse.onlinedegree.iitm.ac.in/t/168449/31)

Q1: Download and unzip q-count-gold-ticket-sales-from-html.zip. It has a set of HTML files, each with tables of 3 columns: Type, Units, and Price.

What is the total sales of all the items in the “Gold” ticket type? Round to 2 decimal places (e.g. 123.40).

`!unzip /content/q-count-gold-ticket-sales-from-html.zip -d /content/extracted_folder
`
`import os
import pandas as pd
from bs4 import BeautifulSoup

total_sales = 0
html_folder = "/content/extracted_folder" # Update if the folder name is different

for file in os.listdir(html_folder):
 if file.endswith(".html"):
 file_path = os.path.join(html_folder, file)

# Step 3: Read the HTML content and extract tables
 with open(file_path, "r", encoding="utf-8") as f:
 soup = BeautifulSoup(f, "html.parser")
 
 tables = pd.read_html(str(soup)) # Extract all tables
