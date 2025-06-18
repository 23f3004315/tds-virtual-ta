---
chunk_id: discourse_topic_165959_post_189_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/189
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 274
username: koustubhr
post_number: 189
topic_id: 165959
---

## Post #189 by koustubhr

**Direct Link**: [Post #189](https://discourse.onlinedegree.iitm.ac.in/t/165959/189)

Request help on Q4 aboutBBC weather data, the instructions in the question tell us to use BBC broker API and get issueDate &amp; enhancedWeatherdescription value pairs. However, it seems there are only 2 unique values of issueDate (not the expected 14 days)

Please clarify, sharing code and output below for reference.

Code:

`import requests

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/" + getlocid('Bogota')
response = requests.get(url)
json_data=response.json()
print(f"The number of days data is {len(json_data['forecasts'])}")

weather_data = {}

for i in range(len(json_data['forecasts'])): # Use range to create an iterable sequence of indices
 issue_date = json_data['forecasts'][i]['summary']['issueDate']
 weather_description = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
 weather_data[issue_date]=weather_description
 print("Iteration No. " + str(i))
 print(issue_date)
 print(weather_description)
 
print("Final Weather Data json below")
print(weather_data)
`
Output
