---
chunk_id: discourse_topic_172333_post_1_08
source_url: https://discourse.onlinedegree.iitm.ac.in/t/172333/1
source_title: END TERM MOCK [TDS Jan 25]
content_type: discourse
tokens: 359
username: carlton
post_number: 1
topic_id: 172333
---

, FIND(",", A1)-1)`
B. `=RIGHT(A1, LEN(A1) - FIND(",", A1))`
C. `=MID(A1, FIND(",", A1)+2, LEN(A1))`
D. `=SPLIT(A1, ",")`

---

**Answer**: C — The `MID` function extracts text from the middle of a string. By finding the position of the comma and adding 2 (to skip the comma and space), it extracts the first name. Option A extracts the last name, Option B results in an error due to incorrect syntax, and Option D is not a valid Excel function.

Module: Data Sourcing
**Q2: Web Scraping Ethics**

When performing web scraping to collect data, which of the following practices is considered unethical?

A. Respecting the website’s `robots.txt` file.
B. Sending requests at a rate that mimics human browsing behavior.
C. Scraping data from a website that requires login without permission.
D. Citing the source of the data collected.

**Answer**: C — Scraping data from a website that requires login without permission violates the site’s terms of service and user privacy. Options A, B, and D are ethical practices that respect the website’s policies and data ownership.

Module: Data Preparation
**Q3: Handling Missing Data**

In a dataset, you notice that several entries in the “Age” column are missing. Which method is generally **not** appropriate for handling these missing values?

A. Replacing missing values with the mean age.
B. Deleting rows with missing age values.
C. Replacing missing values with a fixed age, such as 0.
D. Leaving the missing values as they are without any action.
