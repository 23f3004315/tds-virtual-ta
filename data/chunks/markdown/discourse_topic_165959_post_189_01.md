---
chunk_id: discourse_topic_165959_post_189_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/189
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 599
username: koustubhr
post_number: 189
topic_id: 165959
---

 = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
 weather_data[issue_date]=weather_description
 print("Iteration No. " + str(i))
 print(issue_date)
 print(weather_description)
 
print("Final Weather Data json below")
print(weather_data)
`
Output

---

`The number of days data is 14
Iteration No. 0
2025-02-08T04:00:00-05:00
Light rain showers and a gentle breeze
Iteration No. 1
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 2
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 3
2025-02-08T04:00:00-05:00
Thundery showers and light winds
Iteration No. 4
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 5
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 6
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 7
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 8
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 9
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 10
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 11
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 12
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 13
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Final Weather Data json below
{'2025-02-08T04:00:00-05:00': 'Thundery showers and a gentle breeze', '2025-02-08T16:01:58-05:00': 'Thundery showers and a gentle breeze'}
`
Edit: For now, I have worked around with code posted by @21f3002277. But the doubt about the question remains
