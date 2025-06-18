---
chunk_id: course_extracting_audio_and_transcripts_003
source_url: https://tds.s-anand.net/#/extracting-audio-and-transcripts
source_title: extracting-audio-and-transcripts
content_type: course
tokens: 452
---

Error Handling:

```bash
# Validate file before processing
ffprobe input.mp4 2>&1 | grep "Invalid"

# Continue on errors in batch processing
ffmpeg -i input.mp4 output.mp4 -xerror

# Get detailed error information
ffmpeg -v error -i input.mp4 2>&1 | grep -A2 "Error"
```

---

## Media tools: yt-dlp

[yt-dlp](https://github.com/yt-dlp/yt-dlp) is a feature-rich command-line tool for downloading audio/video from thousands of sites. It's particularly useful for extracting audio and transcripts from videos.

Install using your package manager:

```bash
# macOS
brew install yt-dlp

# Linux
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o ~/.local/bin/yt-dlp
chmod a+rx ~/.local/bin/yt-dlp

# Windows
winget install yt-dlp
```

Common operations for extracting audio and transcripts:

```bash
# Download audio only at lowest quality suitable for speech
yt-dlp -f "ba[abr=3.9"
# dependencies = ["yt-dlp"]
# ///

import yt_dlp

def download_audio(url: str) -> None:
 """Download audio at speech-optimized quality."""
 ydl_opts = {
 'format': 'ba[abr<50]/worstaudio',
 'postprocessors': [{
 'key': 'FFmpegExtractAudio',
 'preferredcodec': 'mp3',
 'preferredquality': '32'
 }]
 }

 with yt_dlp.YoutubeDL(ydl_opts) as ydl:
 ydl.download([url])

# Example usage
download_audio('https://www.youtube.com/watch?v=VIDEO_ID')
```

Tools:

- [ffmpeg](https://ffmpeg.org/): Required for audio extraction and conversion
- [whisper](https://github.com/openai/whisper): Can be used with yt-dlp for speech-to-text
- [gallery-dl](https://github.com/mikf/gallery-dl): Alternative for image-focused sites

Note: Always respect copyright and terms of service when downloading content.
