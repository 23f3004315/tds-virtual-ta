---
chunk_id: discourse_topic_165959_post_376_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/376
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 277
username: Lokkiii
post_number: 376
topic_id: 165959
---

## Post #376 by Lokkiii

**Direct Link**: [Post #376](https://discourse.onlinedegree.iitm.ac.in/t/165959/376)

const movies = ;

document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) =&gt; {

if (index &gt;= 25) return; // Stop after collecting 25 movies

`const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement &amp;&amp; yearElement) {
 const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
 const id = idMatch ? `tt${idMatch[1]}` : null;
 const title = titleElement.innerText.trim();
 //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
 const yearText = yearElement.innerText.trim();
 const year = yearText ? yearText : null; // Keep year as a string
 const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string
