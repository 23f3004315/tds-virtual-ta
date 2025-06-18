---
chunk_id: course_live_sessions_001
source_url: https://tds.s-anand.net/#/live-sessions
source_title: live-sessions
content_type: course
tokens: 176
---

utoff 4000 -frame_duration 60 -compression_level 10" \
 $YOUTUBE_URL
```

They were then transcribed by Gemini 1.5 Flash 002 (currently the best model from a price-quality perspective for audio transcription).

System prompt:

```
You are an expert transcriber of data science audio tutorials
```

User prompt:

---

```
Transcribe this audio tutorial about Tools in Data Science (TDS) as an FAQ.
Summarize the student questions faithfully.
Summarize the answers succinctly, without missing information, in a conversational style.
Avoid repeating questions, consolidating similar ones.
Prefer "You" and "I" instead of "student" and "instructor".
For example:

**Q1: [Concisely framed question]**

**A1:** [Succinct answer]
```
