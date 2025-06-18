---
chunk_id: discourse_topic_168449_post_35_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/35
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 163
username: 23f1002382
post_number: 35
topic_id: 168449
---

 lat2, lon2 = cities_df[cities_df["City"] == city2][["Latitude", "Longitude"]].values[0]
 
 distance = haversine(lat1, lon1, lat2, lon2)
 G.add_edge(city1, city2, weight=distance)

---

# Step 5: Find Shortest Path using Dijkstra's Algorithm
shortest_path = nx.shortest_path(G, source="Doha", target="Muscat", weight="weight")
shortest_distance = nx.shortest_path_length(G, source="Doha", target="Muscat", weight="weight")

# Output the result
print("Shortest Path:", " → ".join(shortest_path))
print(f"Total Distance: {shortest_distance:.2f} km")

`
@all
