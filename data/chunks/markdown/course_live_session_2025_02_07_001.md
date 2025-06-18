---
chunk_id: course_live_session_2025_02_07_001
source_url: https://tds.s-anand.net/#/live-session-2025-02-07
source_title: live-session-2025-02-07
content_type: course
tokens: 560
---

 assignments will decrease.

**Q2: Where can I find the recording of yesterday's session?**

**A2:** It's already uploaded to your calendar associated with your IIT-DS ID. It takes Google about an hour or two to process the video.

**Q3: How do I use the BBC Weather API to get weather data for a specific location?**

---

**A3:** First, use the BBC location service API to get the location ID for your city (e.g., Delhi). You can use the Thunder Client extension or Postman to send the API request. The instructor demonstrates using Postman. Once you have the location ID, use it in the BBC Weather API endpoint.

**Q4: How do I access data from a JSON object in Python?**

**A4:** JSON objects are like Python dictionaries. You can access the data using standard Python dictionary access methods. The instructor shows how to access the "reports" key.

**Q5: How do I prepare for the upcoming R.O.E.?**

**A5:** The instructor recommends creating your own code and keeping it ready. Separate sessions will be held to cover this.

**Q6: How do I use Nominatim to get geolocation data?**

**A6:** Nominatim is an API used for extracting geolocation data. The instructor demonstrates how to use it with Postman, showing how to pass parameters for the location (e.g., "Delhi") and specify the desired format (JSON). The instructor notes that Nominatim may return multiple results if there are multiple locations with the same name (e.g., Delhi in India and Delhi in the United States).

**Q7: How do I use Beautiful Soup to parse XML data?**

**A7:** The instructor demonstrates using Beautiful Soup to parse XML data from the Hacker News API. The instructor explains how to use the `find_all` function to locate specific tags (e.g., "item") and extract the desired information. The instructor also explains the difference between `find` and `findall` functions. The instructor notes that if you encounter issues, you can use an XML viewer to examine the structure of the XML file. The instructor also explains that you should use an XML parser (lxml) instead of an HTML parser.

**Q8: How do I handle situations where the number of values in different lists doesn't match?**

**A8:** If the lengths of lists (e.g., product names, prices, links) don't match, it usually means there's an extra value. The instructor shows how to handle this by checking the lengths of the lists and potentially removing extra values.

**Q9: How do I save the extracted data to a CSV file?**
