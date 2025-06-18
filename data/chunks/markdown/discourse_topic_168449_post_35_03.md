---
chunk_id: discourse_topic_168449_post_35_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/35
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 321
username: 23f1002382
post_number: 35
topic_id: 168449
---

x as nx
from math import radians, sin, cos, sqrt, atan2

cities_df = df2

flights_df = df
cities_df["Latitude"] = pd.to_numeric(cities_df["Latitude"])
cities_df["Longitude"] = pd.to_numeric(cities_df["Longitude"])

---

# Step 3: Define Haversine Distance Function
def haversine(lat1, lon1, lat2, lon2):
 R = 6371 # Earth radius in km
 lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
 dlat, dlon = lat2 - lat1, lon2 - lon1
 a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
 return 2 * R * atan2(sqrt(a), sqrt(1 - a))

# Step 4: Build Graph with NetworkX
G = nx.Graph()

for _, row in flights_df.iterrows():
 city1, city2 = row["From"], row["To"]
 
 lat1, lon1 = cities_df[cities_df["City"] == city1][["Latitude", "Longitude"]].values[0]
 lat2, lon2 = cities_df[cities_df["City"] == city2][["Latitude", "Longitude"]].values[0]
 
 distance = haversine(lat1, lon1, lat2, lon2)
 G.add_edge(city1, city2, weight=distance)
