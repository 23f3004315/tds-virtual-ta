---
chunk_id: discourse_topic_168449_post_35_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/35
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 276
username: 23f1002382
post_number: 35
topic_id: 168449
---

;&lt;!----&gt;...............GET DATA FROM QUESTION
 &lt;/tr&gt;&lt;!----&gt;
 &lt;/tbody&gt;
 &lt;/table&gt;"""
import pandas as pd
from bs4 import BeautifulSoup
soup = BeautifulSoup(HTML, "html.parser")

---

# Extract table rows
rows = []
for tr in soup.find_all("tr"):
 cells = [td.get_text(strip=True) for td in tr.find_all("td")]
 if cells: # Ensure the row is not empty
 rows.append(cells)

# Convert extracted data into a pandas DataFrame
df = pd.DataFrame(rows, columns=["From", "To"])

soup = BeautifulSoup(HTML2, "html.parser")
rows = []
for tr in soup.find_all("tr"):
 cells = [td.get_text(strip=True) for td in tr.find_all("td")]
 if cells: # Ensure the row is not empty
 rows.append(cells)

# Convert extracted data into a pandas DataFrame
df2 = pd.DataFrame(rows, columns=["City", "Latitude","Longitude"])
import networkx as nx
from math import radians, sin, cos, sqrt, atan2

cities_df = df2

flights_df = df
cities_df["Latitude"] = pd.to_numeric(cities_df["Latitude"])
cities_df["Longitude"] = pd.to_numeric(cities_df["Longitude"])
