---
chunk_id: course_extracting_audio_and_transcripts_001
source_url: https://tds.s-anand.net/#/extracting-audio-and-transcripts
source_title: extracting-audio-and-transcripts
content_type: course
tokens: 507
---

## Media Processing: FFmpeg

[FFmpeg](https://ffmpeg.org/) is the standard command-line tool for processing video and audio files. It's essential for data scientists working with media files for:

- Extracting audio/video for machine learning
- Converting formats for web deployment
- Creating visualizations and presentations
- Processing large media datasets

Basic Operations:

```bash
# Basic conversion
ffmpeg -i input.mp4 output.avi

# Extract audio
ffmpeg -i input.mp4 -vn output.mp3

# Convert format without re-encoding
ffmpeg -i input.mkv -c copy output.mp4

# High quality encoding (crf: 0-51, lower is better)
ffmpeg -i input.mp4 -preset slower -crf 18 output.mp4
```

Common Data Science Tasks:

```bash
# Extract frames for computer vision
ffmpeg -i input.mp4 -vf "fps=1" frames_%04d.png # 1 frame per second
ffmpeg -i input.mp4 -vf "select='eq(n,0)'" -vframes 1 first_frame.jpg

# Create video from image sequence
ffmpeg -r 1/5 -i img%03d.png -c:v libx264 -vf fps=25 output.mp4

# Extract audio for speech recognition
ffmpeg -i input.mp4 -ar 16000 -ac 1 audio.wav # 16kHz mono

# Trim video/audio for training data
ffmpeg -ss 00:01:00 -i input.mp4 -t 00:00:30 -c copy clip.mp4
```

Processing Multiple Files:

```bash
# Concatenate videos (first create files.txt with list of files)
echo "file 'input1.mp4'
file 'input2.mp4'" > files.txt
ffmpeg -f concat -i files.txt -c copy output.mp4

# Batch process with shell loop
for f in *.mp4; do
 ffmpeg -i "$f" -vn "audio/${f%.mp4}.wav"
done
```

Data Analysis Features:

```bash
# Get media file information
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Display frame metadata
ffprobe -v quiet -print_format json -show_frames input.mp4

# Generate video thumbnails
ffmpeg -i input.mp4 -vf "thumbnail" -frames:v 1 thumb.jpg
```
