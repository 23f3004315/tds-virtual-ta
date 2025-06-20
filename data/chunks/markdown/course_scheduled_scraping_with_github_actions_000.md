---
chunk_id: course_scheduled_scraping_with_github_actions_000
source_url: https://tds.s-anand.net/#/scheduled-scraping-with-github-actions
source_title: scheduled-scraping-with-github-actions
content_type: course
tokens: 494
---

## Scheduled Scraping with GitHub Actions

GitHub Actions provides an excellent platform for running web scrapers on a schedule. This tutorial shows how to automate data collection from websites using GitHub Actions workflows.

### Key Concepts

- **Scheduling**: Use [cron syntax](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) to run scrapers at specific times
- **Dependencies**: Install required packages like `httpx`, `lxml`
- **Data Storage**: Save scraped data to files and commit back to the repository
- **Error Handling**: Implement robust error handling for network issues and HTML parsing
- **Rate Limiting**: Respect website terms of service and implement delays between requests

Here's a sample `scrape.py` that scrapes the IMDb Top 250 movies using httpx and lxml:

```python
import json
import httpx
from datetime import datetime, UTC
from lxml import html
from typing import List, Dict

def scrape_imdb() -> List[Dict[str, str]]:
 """Scrape IMDb Top 250 movies using httpx and lxml.

Returns:
 List of dictionaries containing movie title, year, and rating.
 """
 headers = {"User-Agent": "Mozilla/5.0 (compatible; IMDbBot/1.0)"}
 response = httpx.get("https://www.imdb.com/chart/top/", headers=headers)
 response.raise_for_status()

tree = html.fromstring(response.text)
 movies = []

for item in tree.cssselect(".ipc-metadata-list-summary-item"):
 title = (
 item.cssselect(".ipc-title__text")[0].text_content()
 if item.cssselect(".ipc-title__text")
 else None
 )
 year = (
 item.cssselect(".cli-title-metadata span")[0].text_content()
 if item.cssselect(".cli-title-metadata span")
 else None
 )
 rating = (
 item.cssselect(".ipc-rating-star")[0].text_content()
 if item.cssselect(".ipc-rating-star")
 else None
 )

if title and year and rating:
 movies.append({"title": title, "year": year, "rating": rating})

return movies

# Scrape data and save with timestamp
now = datetime.now(UTC)
with open(f'imdb-top250-{now.strftime("%Y-%m-%d")}.json', "a") as f:
 f.write(json.dumps({"timestamp": now.isoformat(), "movies": scrape_imdb()}) + "\n")
```
