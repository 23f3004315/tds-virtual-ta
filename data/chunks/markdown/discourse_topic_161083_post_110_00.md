---
chunk_id: discourse_topic_161083_post_110_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/110
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 167
username: sarvan108
post_number: 110
topic_id: 161083
---

## Post #110 by sarvan108

**Direct Link**: [Post #110](https://discourse.onlinedegree.iitm.ac.in/t/161083/110)

I ran this directly in the console and got the correct answer.

// Select all

and elements with the ‘foo’ class

const fooElements = document.querySelectorAll(“div.foo, span.foo”);

// Initialize a variable to store the sum

let sum = 0;

// Iterate through the selected elements

fooElements.forEach(element =&gt; {

// Get the ‘data-value’ attribute and convert it to a number

const value = parseFloat(element.getAttribute(“data-value”));

// Add the value to the sum

if (!isNaN(value)) {

sum += value;

}

});

console.log(“Sum of data-value attributes:”, sum);
