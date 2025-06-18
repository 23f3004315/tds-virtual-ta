---
chunk_id: course_extracting_audio_and_transcripts_002
source_url: https://tds.s-anand.net/#/extracting-audio-and-transcripts
source_title: extracting-audio-and-transcripts
content_type: course
tokens: 522
---

:

```bash
# Get media file information
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Display frame metadata
ffprobe -v quiet -print_format json -show_frames input.mp4

# Generate video thumbnails
ffmpeg -i input.mp4 -vf "thumbnail" -frames:v 1 thumb.jpg
```

---

Watch this introduction to FFmpeg (12 min):

[**[Course Image: FFmpeg in 12 Minutes]** This material introduces FFmpeg, a powerful command-line tool, for audio and video manipulation. Specifically, within the context of "extracting-audio-and-transcripts," it is critical for tasks like extracting audio streams from video files, converting audio formats for transcription, and generating thumbnails for video content. Mastery of FFmpeg will enable efficient audio extraction and processing, an essential step for accurate transcript generation. Understanding FFmpeg basics lays the groundwork for more advanced audio/video tasks in TDS projects. The image shows a screenshot of the command line tool FFmpeg.erful command-line tool used for various multimedia tasks, especially relevant in the context of extracting audio and transcripts. It highlights the importance of learning how to use FFmpeg effectively. Understanding FFmpeg's capabilities is crucial for manipulating audio and video files, which is a key skill in data science projects involving multimedia data. This includes extracting audio from video files, converting audio formats, and preparing audio for transcription. The image serves as an introductory visual to get users acquainted with FFmpeg's role in the workflow.)](https://youtu.be/MPV7JXTWPWI)

Tools:

- [ffmpeg.lav.io](https://ffmpeg.lav.io/): Interactive command builder
- [FFmpeg Explorer](https://ffmpeg.guide/): Visual FFmpeg command generator
- [FFmpeg Buddy](https://evanhahn.github.io/ffmpeg-buddy/): Simple command generator

Tips:

1. Use `-c copy` when possible to avoid re-encoding
2. Monitor progress with `-progress pipe:1`
3. Use `-hide_banner` to reduce output verbosity
4. Test commands with small clips first
5. Use hardware acceleration when available (-hwaccel auto)

Error Handling:

```bash
# Validate file before processing
ffprobe input.mp4 2>&1 | grep "Invalid"

# Continue on errors in batch processing
ffmpeg -i input.mp4 output.mp4 -xerror

# Get detailed error information
ffmpeg -v error -i input.mp4 2>&1 | grep -A2 "Error"
```
