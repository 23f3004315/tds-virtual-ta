---
chunk_id: discourse_topic_169029_post_227_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/227
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 295
username: 22f3000819
post_number: 227
topic_id: 169029
---

## Post #227 by 22f3000819

**Direct Link**: [Post #227](https://discourse.onlinedegree.iitm.ac.in/t/169029/227)

@Saransh_Saini @Jivraj @carlton

What is the request timeout for each question, especially for the question on YouTube video transcription? I request the timeout to be at least 40-60 seconds as yt-dlp and faster-whisper take take to download the audio, load the model and run it on cpu and get the transcription.

For 259.7 to 351.8 seconds, it is taking around 1.5 mins, but it is giving the correct answer.

So I request you to shorten the length of the audio or increase the request timeout or both in moderation.

Question —&gt; the “question” sent to the api will have the youtube video link, right? Or since the video is same for everyone, can I just have the audio file ready in the project? Will the api be tested against any YouTube video other than the Mystery Story Audiobook link given in the GA question?

Edit: Even with a preprocessed audio file (mp3, speech optimized, 32K), what’s taking the longest time is joining the transcribed sentences into a single string. That alone is taking &gt;50 seconds. Please suggest a way to make it faster.

Regards,

Shivaditya
