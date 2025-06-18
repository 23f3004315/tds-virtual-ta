---
chunk_id: discourse_topic_168832_post_62_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168832/62
source_title: Remote Online Exam [TDS Jan 2025]
content_type: discourse
tokens: 288
username: 23f2000599
post_number: 62
topic_id: 168832
---

fs.append(table)

# Combine all DataFrames into a single DataFrame
df = pd.concat(all_dfs, ignore_index=True)

# Rename columns for easier access (if necessary)
df.columns = ["Maths", "Physics", "English", "Economics", "Biology", "Group"]

---

# Convert marks to numerical data types
df["Maths"] = pd.to_numeric(df["Maths"], errors="coerce")
df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")
df["English"] = pd.to_numeric(df["English"], errors="coerce")
df["Economics"] = pd.to_numeric(df["Economics"], errors="coerce")
df["Biology"] = pd.to_numeric(df["Biology"], errors="coerce")
df["Group"] = pd.to_numeric(df["Group"], errors="coerce")

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Display the first few rows of the combined DataFrame
print(df.head())

# Display the data types of the columns
print(df.dtypes)
filtered_df = df[(df["Biology"] &gt;= 30) &amp; (df["Group"].between(1, 28))]

total_biology_marks = filtered_df["Maths"].sum()
print(total_biology_marks)
`
Ignore the variables name, i got my value as 34919
