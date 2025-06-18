---
chunk_id: course_live_sessions_000
source_url: https://tds.s-anand.net/#/live-sessions
source_title: live-sessions
content_type: course
tokens: 441
---

# Live Sessions

Live sessions by the instructors and TAs are recorded and uploaded to YouTube.

[**[Course Image: TDS Live Sessions: Jan 2025]** The live sessions in the TDS course often cover a variety of essential tools used in data science. These tools can range from data manipulation and visualization libraries to machine learning frameworks and cloud computing platforms. Understanding these tools is critical for success in data science projects and assignments within the TDS curriculum. The sessions aim to equip students with the practical knowledge to effectively apply these tools in real-world scenarios. Mastering these data science tools during the live sessions will help students tackle a wide range of data-related tasks.r essential tools used in the field of data science. These sessions aim to familiarize students with the diverse range of tools available, which span data visualization techniques, statistical analysis methods, and machine learning algorithms. The instructors may demonstrate how to use these tools to solve real-world problems and may include interactive Q&A sessions to address student queries and clarify concepts. Key concepts may be presented with code examples using languages like Python or R. By attending these live sessions, students should gain practical insights into the application of these tools and feel more confident in tackling data science projects.)](https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C)

These were downloaded using [yt-dlp](https://github.com/yt-dlp/yt-dlp). The options compress the audio optimized for speech.

```bash
yt-dlp --extract-audio --audio-format opus --embed-thumbnail --postprocessor-args \
 "-c:a libopus -b:a 12k -ac 1 -application voip -vbr off -ar 8000 -cutoff 4000 -frame_duration 60 -compression_level 10" \
 $YOUTUBE_URL
```

They were then transcribed by Gemini 1.5 Flash 002 (currently the best model from a price-quality perspective for audio transcription).

System prompt:

```
You are an expert transcriber of data science audio tutorials
```

User prompt:
