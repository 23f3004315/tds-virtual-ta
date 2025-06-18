---
chunk_id: discourse_topic_168449_post_81_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/81
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 288
username: 23f2000599
post_number: 81
topic_id: 168449
---

## Post #81 by 23f2000599

**Direct Link**: [Post #81](https://discourse.onlinedegree.iitm.ac.in/t/168449/81)

`from shapely.geometry import Polygon, Point
import json

with open("regions.json", "r") as f:
 data = json.load(f)

pickup_locations = [
 (6.488, -78.0287),
 (32.0198, -99.7243),
 (16.7257, -58.7811),
 (1.9307, 45.4928),
 (-34.6289, 133.0359)
]

cities = data["cities"]
regions = data["regions"]

matching_regions = []

for request_point in pickup_locations:
 point = Point(request_point)
 region_num = 1

for region in regions:
 region_coordinates = [(cities[city][0], cities[city][1]) for city in region]
 region_polygon = Polygon(region_coordinates)

if region_polygon.contains(point):
 matching_regions.append(str(region_num))
 break # Stop checking once a match is found
 region_num += 1

print(",".join(matching_regions))
`
I have been trying this for the past 1 day and i still cant get the answer for mock roe 2, q5

2 of my coordinates r not giving any value

can someone please help

@carlton
