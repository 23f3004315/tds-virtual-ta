---
chunk_id: course_scheduled_scraping_with_github_actions_001
source_url: https://tds.s-anand.net/#/scheduled-scraping-with-github-actions
source_title: scheduled-scraping-with-github-actions
content_type: course
tokens: 432
---

, "rating": rating})

return movies

# Scrape data and save with timestamp
now = datetime.now(UTC)
with open(f'imdb-top250-{now.strftime("%Y-%m-%d")}.json', "a") as f:
 f.write(json.dumps({"timestamp": now.isoformat(), "movies": scrape_imdb()}) + "\n")
```

---

Here's a sample `.github/workflows/imdb-top250.yml` that runs the scraper daily and saves the data:

```yaml
name: Scrape IMDb Top 250

on:
 schedule:
 # Runs at 00:00 UTC every day
 - cron: "0 0 * * *"
 workflow_dispatch: # Allow manual triggers

jobs:
 scrape-imdb:
 runs-on: ubuntu-latest
 permissions:
 contents: write

steps:
 - name: Checkout repository
 uses: actions/checkout@v4

- name: Install uv
 uses: astral-sh/setup-uv@v5

- name: Run scraper
 run: | # python
 uv run --with httpx,lxml,cssselect python scrape.py

- name: Commit and push changes
 run: |
 git config --local user.email "github-actions[bot]@users.noreply.github.com"
 git config --local user.name "github-actions[bot]"
 git add *.json
 git commit -m "Update IMDb Top 250 data [skip ci]" || exit 0
 git push
```

### Best Practices

1. **Cache Dependencies**: Use GitHub's caching to speed up package installation
2. **Handle Errors**: Implement retries and error logging
3. **Rate Limiting**: Add delays between requests to avoid overwhelming servers
4. **Data Validation**: Verify scraped data structure before saving
5. **Monitoring**: Set up notifications for workflow failures

### Tools and Resources

- [httpx](https://www.python-httpx.org/): Async HTTP client
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Video Tutorials
