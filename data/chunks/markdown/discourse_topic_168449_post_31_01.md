---
chunk_id: discourse_topic_168449_post_31_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/31
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 181
username: 23f1002382
post_number: 31
topic_id: 168449
---

.path.join(html_folder, file)

# Step 3: Read the HTML content and extract tables
 with open(file_path, "r", encoding="utf-8") as f:
 soup = BeautifulSoup(f, "html.parser")
 
 tables = pd.read_html(str(soup)) # Extract all tables

---

for table in tables:
 if {"Type", "Units", "Price"}.issubset(table.columns):
 # Step 4: Filter "Gold" ticket type and calculate total sales
 table["Type"] = table["Type"].str.strip().str.lower()
 gold_sales = table[table["Type"] == "gold"]["Units"] * table[table["Type"] == "gold"]["Price"]
 total_sales += gold_sales.sum()
# Step 5: Print the result rounded to 2 decimal places
print(f"Total Gold Ticket Sales: {total_sales:.2f}")

`
@all
