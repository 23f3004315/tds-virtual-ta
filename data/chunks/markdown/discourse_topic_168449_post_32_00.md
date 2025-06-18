---
chunk_id: discourse_topic_168449_post_32_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/32
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 266
username: 23f1002382
post_number: 32
topic_id: 168449
---

## Post #32 by 23f1002382

**Direct Link**: [Post #32](https://discourse.onlinedegree.iitm.ac.in/t/168449/32)

Q2: Download and unzip q-least-unique-subjects-from-csv.zip. It has 2 files:

`students.csv` has 2 columns:
studentId: A unique identifier for each student
class: The class (including section) of the student
`subjects.csv` has 2 columns:
studentId: The identifier for each student
subject: The name of the subject they have chosen

What are the least number of subjects any class has taken up? List the 3 lowest count of subjects in order.

`!unzip /content/q-least-unique-subjects-from-csv.zip -d /content/extracted_folder
import pandas as pd
df1 = pd.read_csv("/content/extracted_folder/students.csv")
df2 = pd.read_csv("/content/extracted_folder/subjects.csv")
merged_df = pd.merge(df1, df2, on="studentId")
class_subject_counts = merged_df.groupby("class")["subject"].nunique()
lowest_subject_counts = class_subject_counts.nsmallest(3)
print(lowest_subject_counts)
`
@all
