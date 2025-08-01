---
chunk_id: course_live_session_2025_01_30_006
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 492
---

A33:** Not exactly, but we can make API calls and get embeddings for words. For example, let's say we have the word "Anand".

**Q34: Sorry for interrupting, but is Hugging Face part of the TDS course?**

**A34:** I think it's been removed, probably because it's too heavy for the course.

---

**Q35: My next question is why are these vectors (embeddings) so long? It's just a word. For a paragraph, it must be thousands of variables.**

**A35:** It won't be. We're getting embeddings from OpenAI. We'll always get embeddings of the same length. It uses 1,536 numbers to represent a word. These are different features of the word. It might involve the shape of a bicycle. Does it involve SVD? It must be doing SVD.

**Q36: Can we use wrongly spelled words and get embeddings for them?**

**A36:** You can try. It should work. Anything similar to "bicycle" should work.

**Q37: My last question is how can we pass multiple words at the same time and get their embeddings separately?**

**A37:** I think this is the way you can pass multiple words. This should get us two different vectors. It's a list. The first embedding is for bicycle, and the second is for cycle.

**Q38: Can we get the names of the words and their embeddings separately in the JSON?**

**A38:** No, it won't get you the name of the embedding. It will store embeddings for each word. You can pass three different values. You can calculate three embeddings. Then you can compute the cosine similarity between them. The first index would get the embedding for bicycle, the second for cycle, and the third for `biycle`.

**Q39: Can we have a session on Hugging Face?**

**A39:** We can have a session during the last week of the course. The last week should be a bit lighter. Hugging Face is totally open source, so it would be very helpful during the NLP part of the course. But Hugging Face won't be of much context when it comes to TDS. It would be for learning only.

**Q40: My first doubt is, can we use `httpie` instead of `requests`?**
