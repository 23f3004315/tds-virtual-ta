---
chunk_id: discourse_topic_165959_post_237_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/237
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 211
username: ABHIJITH_VS
post_number: 237
topic_id: 165959
---

 api key visible may be key to their goal. The student may be trying to reverse engineer how the site works in order to connect the site with GA4. 2x" data-dominant-color="B1C7D3">Screenshot (7)1366×768 243 KB

---

Open the BBC Weather website.
Press `Ctrl + Shift + I`.
Select the ‘Network’ menu.
Select ‘Fetch/XHR’.
Type ‘Karachi’ in the input field on the website. **Do not press Enter** while entering the location; just type the location. Pressing Enter might cause ‘location?api_key=…’ to disappear.
‘location?api_key=…’ will appear in the inspect menu.
Double-click it to open a web page (https://locator-service.api.bbci.co.uk/locations?api_key={api_key}). This will give the API.
Alternatively, single-clicking ‘location?api_key=…’ will open headers where you can see the Request URL and the API key.
