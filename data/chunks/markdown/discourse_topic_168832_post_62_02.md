---
chunk_id: discourse_topic_168832_post_62_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168832/62
source_title: Remote Online Exam [TDS Jan 2025]
content_type: discourse
tokens: 291
username: 23f2000599
post_number: 62
topic_id: 168832
---

 like Maths, Physics, English, Economics, Biology, and Group with integer values. The `dtype: object` suggests that the column types might need further processing. 2x" data-dominant-color="F5F5F5">image1604×678 66.9 KB

---

`!pip install tabula-py
import tabula
import pandas as pd
from google.colab import files

# Path to the PDF file
pdf_path = pdf_path = list(files.upload().keys())[0]

# Extract tables from the PDF, specifying pages and multiple_tables=True
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

# Initialize an empty list to store all DataFrames
all_dfs = []

# Iterate through each table and add a "Group" column based on the page number
for i, table in enumerate(tables):
 # Add a "Group" column to the table
 table["Group"] = i + 1 # Group 1 for Page 1, Group 2 for Page 2, etc.
 # Append the table to the list
 all_dfs.append(table)

# Combine all DataFrames into a single DataFrame
df = pd.concat(all_dfs, ignore_index=True)

# Rename columns for easier access (if necessary)
df.columns = ["Maths", "Physics", "English", "Economics", "Biology", "Group"]
