---
chunk_id: course_devtools_000
source_url: https://tds.s-anand.net/#/devtools
source_title: devtools
content_type: course
tokens: 301
---

## Browser: DevTools

[Chrome DevTools](https://developer.chrome.com/docs/devtools/overview/) is the de facto standard for web development and data analysis in the browser.
You'll use this a lot when debugging and inspecting web pages.

Here are the key features you'll use most:

1. **Elements Panel**

- Inspect and modify HTML/CSS in real-time
 - Copy CSS selectors for web scraping
 - Debug layout issues with the Box Model

```javascript
 // Copy selector in Console
 copy($0); // Copies selector of selected element
 ```

2. **Console Panel**

- JavaScript REPL environment
 - Log and debug data
 - Common console methods:

```javascript
 console.table(data); // Display data in table format
 console.group("Name"); // Group related logs
 console.time("Label"); // Measure execution time
 ```

3. **Network Panel**
 - Monitor API requests and responses
 - Simulate slow connections
 - Right-click on a request and select "Copy as fetch" to get the request.
4. **Essential Keyboard Shortcuts**
 - `Ctrl+Shift+I` (Windows) / `Cmd+Opt+I` (Mac): Open DevTools
 - `Ctrl+Shift+C`: Select element to inspect
 - `Ctrl+L`: Clear console
 - `$0`: Reference currently selected element
 - `$$('selector')`: Query selector all (returns array)

Videos from Chrome Developers (37 min total):
