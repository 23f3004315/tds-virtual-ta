---
chunk_id: course_wikipedia_data_with_python_000
source_url: https://tds.s-anand.net/#/wikipedia-data-with-python
source_title: wikipedia-data-with-python
content_type: course
tokens: 492
---

## Wikipedia Data with Python

[**[Course Image: Wikipedia data with Wikimedia Python library]** This image serves as an introductory slide from the "Wikipedia Data with Python" module within the "TOOLS IN DATA SCIENCE" course, focusing on how to acquire data specifically from Wikimedia. It sets the stage for learning how to extract information from Wikipedia using Python, likely through libraries and APIs designed for this purpose. The slide credits Instructor Anand S and Tutorial Instructor Dibu Philip for the course material, presented under the IIT Madras Online Degree program. Students will learn to programmatically access and utilize Wikipedia's vast data resources for data science projects. After this module, one can expect to be able to gather, process, and analyze Wikipedia content using Python.a with Python" course, titled "Get the data: Wikimedia," focuses on obtaining data from Wikimedia projects using Python. It is part of the "Tools in Data Science" course, instructed by Anand S and Diby Philip. This module likely introduces methods for accessing and scraping Wikipedia data for analysis. Students will learn how to interact with the Wikimedia API and extract relevant information using Python libraries. Mastering this section is crucial for projects that involve analyzing Wikipedia content, identifying trends, or building knowledge graphs.)](https://youtu.be/b6puvm-QEY0)

You'll learn how to scrape data from Wikipedia using the `wikipedia` Python library, covering:

- **Installing and Importing**: Use pip install to get the Wikipedia library and import it with import wikipedia as wk.
- **Keyword Search**: Use the search function to find Wikipedia pages containing a specific keyword, limiting results with the results argument.
- **Fetching Summaries**: Use the summary function to get a concise summary of a Wikipedia page, limiting sentences with the sentences argument.
- **Retrieving Full Pages**: Use the page function to obtain the full content of a Wikipedia page, including sections and references.
- **Accessing URLs**: Retrieve the URL of a Wikipedia page using the url attribute of the page object.
- **Extracting References**: Use the references attribute to get all reference links from a Wikipedia page.
- **Fetching Images**: Access all images on a Wikipedia page via the images attribute, which returns a list of image URLs.
- **Extracting Tables**: Use the pandas.read_html function to extract tables from the HTML content of a Wikipedia page, being mindful of table indices.

Here are links and references:
