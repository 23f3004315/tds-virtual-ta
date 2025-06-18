---
chunk_id: discourse_topic_168449_post_35_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168449/35
source_title: Mock ROE 1, 2, 3, 4 [TDS Jan 2025]
content_type: discourse
tokens: 985
username: 23f1002382
post_number: 35
topic_id: 168449
---

 `Muscat`.

World Courier has a fleet of aircraft that can fly directly between specific cities. The distance between two cities is the Haversine distance.

What is the sequence of cities that you should fly to minimize the total distance traveled?

Write the answer as a sequence of cities separated by commas.

---

`HTML2= """"
&lt;table class="table"&gt;
 &lt;thead&gt;
 &lt;tr&gt;
 &lt;th&gt;City&lt;/th&gt;
 &lt;th&gt;Latitude&lt;/th&gt;
 &lt;th&gt;Longitude&lt;/th&gt;
 &lt;/tr&gt;
 &lt;/thead&gt;
 &lt;tbody&gt;
 &lt;!--?lit$901276210$--&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;New York&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;40.7128&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;-74.006&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lGET DATA FROM QUESTION
 &lt;/tr&gt;&lt;!----&gt;
 &lt;/tbody&gt;
 &lt;/table&gt;
"""
HTML = """&lt;table class="table"&gt;
 &lt;thead&gt;
 &lt;tr&gt;
 &lt;th&gt;From&lt;/th&gt;
 &lt;th&gt;To&lt;/th&gt;
 &lt;/tr&gt;
 &lt;/thead&gt;
 &lt;tbody&gt;
 &lt;!--?lit$901276210$--&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;New York&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;London&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Tokyo&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Sydney&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Paris&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Berlin&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Dubai&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Mumbai&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;San Francisco&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Tokyo&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Toronto&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;New York&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Shanghai&lt;/td&gt;
 &lt;td&gt;&lt;!--?lit$901276210$--&gt;Singapore&lt;/td&gt;
 &lt;/tr&gt;&lt;!----&gt;...............GET DATA FROM QUESTION
 &lt;/tr&gt;&lt;!----&gt;
 &lt;/tbody&gt;
 &lt;/table&gt;"""
import pandas as pd
from bs4 import BeautifulSoup
soup = BeautifulSoup(HTML, "html.parser")
