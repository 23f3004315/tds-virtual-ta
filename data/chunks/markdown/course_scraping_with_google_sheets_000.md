---
chunk_id: course_scraping_with_google_sheets_000
source_url: https://tds.s-anand.net/#/scraping-with-google-sheets
source_title: scraping-with-google-sheets
content_type: course
tokens: 390
---

## Scraping with Google Sheets

[**[Course Image: Scraping with Google Sheets]** To scrape data with Google Sheets, you can use the `IMPORTHTML` function. The syntax is `IMPORTHTML(url, query, index)`, where the URL is the webpage to scrape, the query is either "list" or "table" depending on the desired data structure, and the index specifies which table or list to return, starting at 1. As a sample usage, you could use `IMPORTHTML("http://en.wikipedia.org/wiki/Demographics_of_India", "table", 4)` to import the 4th table from the specified Wikipedia page, and the URL must include the protocol (e.g., http://). Alternatively, you can reference cells containing the URL, query, and index, such as `IMPORTHTML(A2, B2, C2)`. Students often forget to enclose the URL in quotation marks when directly inputting it into the formula.ou can use the `IMPORTHTML` function. The basic syntax is `IMPORTHTML(url, query, index)`, where `url` is the URL of the webpage, `query` specifies either "list" or "table" depending on the desired data structure, and `index` is the numerical index of the table or list you want to import (starting from 1). For example, `IMPORTHTML("http://en.wikipedia.org/wiki/Demographics_of_India", "table", 4)` imports the 4th table from the specified Wikipedia page. The `url` can be directly entered as a string or referenced from a cell containing the URL.)](https://youtu.be/eYQEk7XJM7s)

You'll learn how to [import tables on the web using Google Sheets's `=IMPORTHTML()` formula](https://support.google.com/docs/answer/3093339?hl=en), covering:
