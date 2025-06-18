---
chunk_id: discourse_topic_165959_post_376_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/376
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 171
username: Lokkiii
post_number: 376
topic_id: 165959
---

D/g, "").trim(); // Remove non-numeric characters
 const yearText = yearElement.innerText.trim();
 const year = yearText ? yearText : null; // Keep year as a string
 const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

---

if (id &amp;&amp; title &amp;&amp; year &amp;&amp; rating &amp;&amp; parseFloat(rating) &gt;= 3 &amp;&amp; parseFloat(rating) &lt;= 5) {
 movies.push({ id, title, year, rating });
 }
}
`
});

// Output JSON data with no spaces after colon

console.log(JSON.stringify(movies, (key, value) =&gt; typeof value === ‘string’ ? value.trim() : value, 0));
