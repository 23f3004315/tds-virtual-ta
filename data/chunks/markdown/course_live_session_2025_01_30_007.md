---
chunk_id: course_live_session_2025_01_30_007
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 533
---

 be a bit lighter. Hugging Face is totally open source, so it would be very helpful during the NLP part of the course. But Hugging Face won't be of much context when it comes to TDS. It would be for learning only.

**Q40: My first doubt is, can we use `httpie` instead of `requests`?**

---

**A40:** Yes, you can change it to `httpx`. I'm not sure about `httpie`. It's a command-line tool. I've never used it. I think even if it does, it shouldn't matter much because it's just a different library that allows you to make requests. I wanted to shift to another question. I don't know how to use this particular thing. Maybe it's possible to use it in Python, but I don't know. `requests` is better. If it's complicated, it's not a good tool. At the end, it's also using the `requests` module.

**Q41: My next question is why are the vectors (embeddings) so long?**

**A41:** That's the dimension it uses to represent a word. A higher dimension means better representation, but it requires more storage. You can think of them as a vector space, like a 3D space. Instead of representing a word in 3D, we're representing it in 1,536 dimensions. These are different features of the word. One might represent shape.

**Q42: Does it involve SVD?**

**A42:** I don't know the exact algorithm OpenAI uses to calculate embeddings. You can search on Google or ask ChatGPT. You can also ask ChatGPT for code completion.

**Q43: Question 9: Three different documents. For example, these are three different documents. You can think of them as paragraphs or words. The purpose is to figure out which word is related to the query word. One could be cat, one could be dog, and the other could be elephant. The query word could be kitten. You have to figure out which word relates more to it. The way to do it is using embeddings.**

**A43:** You would have to figure out the embedding for each one of them. The way to compare two words is to compute the dot product. Cosine similarity is the dot product divided by the norm of each vector. OpenAI returns normalized vectors. The cosine similarity between "bicycle" and "cycle" would be higher than between "bicycle" and "apple". That's how computers store this information.
