---
chunk_id: course_scraping_imdb_with_javascript_000
source_url: https://tds.s-anand.net/#/scraping-imdb-with-javascript
source_title: scraping-imdb-with-javascript
content_type: course
tokens: 380
---

## Scraping IMDb with JavaScript

[**[Course Image: Scraping the IMDb with Browser JavaScript]** When scraping IMDb with JavaScript, you might encounter issues retrieving text using `item.querySelectorAll(".cli-title-metadata-item:nth-child(1)").text`. Common problems include the query selector not finding matching elements due to incorrect class names or dynamically loaded content; ensure the class name and structure are correct and present when the code runs. Also, the `:nth-child(1)` pseudo-class may be inappropriate if the target element isn't the first child. Remember that `querySelectorAll` returns a NodeList, so you'll need to access the element (e.g., using `[0]`) before getting the text, and verify that you're using the correct property, like `.textContent` or `.innerText`, to extract the element's content. Double-check your class names for typos such as `.cli-title-metadata-item`. and encountering issues with `item.querySelectorAll(".cli-title-metadata-item:nth-child(1)").text`, consider these common reasons for errors. First, ensure the selector `.cli-title-metadata-item:nth-child(1)` correctly matches elements within the specified `item`, verifying there are no typos and that the elements are present in the DOM when the code runs. Second, confirm that `:nth-child(1)` is appropriate for the element's position and remember that `querySelectorAll` returns a NodeList, so access the first element using `[0]` before extracting the text. Lastly, verify you're using the correct text property, which should be either `.textContent` or `.innerText` to retrieve the text content of the element.)](https://youtu.be/YVIKZqZIcCo)

You'll learn how to scrape the [IMDb Top 250 movies](https://www.imdb.com/chart/top) directly in the browser using JavaScript on the Chrome DevTools, covering:
