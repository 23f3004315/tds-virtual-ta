---
chunk_id: discourse_topic_169029_post_126_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/126
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 296
username: lakshaygarg654
post_number: 126
topic_id: 169029
---

## Post #126 by lakshaygarg654

**Direct Link**: [Post #126](https://discourse.onlinedegree.iitm.ac.in/t/169029/126)

@carlton , @Jivraj @Saransh_Saini

**GA2 - Question 3: Publish a Page Using GitHub Pages**

As part of the requirement, I successfully published a webpage using GitHub Pages that includes my email address `21f3001076@ds.study.iitm.ac.in` in the HTML content. The page functions correctly and becomes accessible on my local system.

To automate the publishing process, I implemented a delay function that checks for the page’s availability after 5 seconds. Based on testing, GitHub Pages typically take around 10–20 seconds to go live after repository creation and HTML deployment. As a result, the complete process—from initiating the API call to verifying that the page is live—takes approximately 30 seconds locally. This setup works reliably on my local machine.

However, when deploying the same process on Azure, I encountered an issue. Without the delay, the API responds too quickly—before the GitHub Pages site is actually live—resulting in a broken or non-functional link on the assignment portal. On the other hand, including the delay function causes Azure to throw a **502 Bad Gateway** error, likely due to Azure’s request timeout limitations. The additional wait time slightly exceeds the platform’s allowed response duration.
