---
chunk_id: course_nominatim_api_with_python_001
source_url: https://tds.s-anand.net/#/nominatim-api-with-python
source_title: nominatim-api-with-python
content_type: course
tokens: 436
---

 to write Python code to query the Nominatim API and incorporate location data into your data science projects. This is essential for tasks like mapping, spatial analysis, and creating location-based services.)](https://youtu.be/f0PZ-pphAXE)

You'll learn how to get the latitude and longitude of any city from the Nominatim API.

---

- **Introduction to Nominatim**: Understand how Nominatim, from OpenStreetMap, works similarly to Google Maps for geocoding.
- **Installation and Import**: Learn to install and import [geopy](https://geopy.readthedocs.io/) and [nominatim](https://nominatim.org/).
- **Using the Locator**: Create a locator object using Nominatim and set up a user agent.
- **Geocoding an Address**: Use `locator.geocode` to input an address (e.g., Eiffel Tower) and fetch geocoded data.
- **Extracting Data**: Access detailed information like latitude, longitude, bounding box, and accurate address from the JSON response.
- **Classifying Locations**: Identify the type of place (e.g., tourism, university) using the response data.
- **Practical Example**: Geocode "IIT Madras" and retrieve its full address, type (university), and other relevant information.

Here are links and references:

- [Geocoding using Nominatim - Notebook](https://colab.research.google.com/drive/1-vvP-UyMjHgBqc-hdsUhm3Bsbgi7oO6g)
- Learn about the [`geocoders` module in the `geopy` package](https://geopy.readthedocs.io/)
- Learn about the [`nominatim` package](https://nominatim.org/release-docs/develop/api/Overview/)
- If you get a HTTP Error 403 from Nominatim, use your email ID or your name instead of "myGeocoder" in `Nominatim(user_agent="myGeocoder")`
