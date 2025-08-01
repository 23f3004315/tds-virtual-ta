---
chunk_id: course_extracting_audio_and_transcripts_005
source_url: https://tds.s-anand.net/#/extracting-audio-and-transcripts
source_title: extracting-audio-and-transcripts
content_type: course
tokens: 515
---

 `source` indicates the source directory, i.e. where the input `$FILE` is
- `--language`: The language of the input file. If you don't specify it, it analyzes the first 30 seconds to auto-detect. You can speed it up by specifying it.

Run `faster-whisper-xxl --help` for more options.

---

## Gemini transcription

The [Gemini](https://gemini.google.com/) models from Google are notable in two ways:

1. They have a _huge_ input context window. Gemini 2.0 Flash can accept 1M tokens, for example.
2. They can handle audio input.

This allows us to use Gemini to transcribe audio files.

LLMs are not good at transcribing audio _faithfully_. They tend to correct errors and meander from what was said. But they are intelligent. That enables a few powerful workflows. Here are some examples:

1. **Transcribe into other languages**. Gemini will handle the transcription and translation in a single step.
2. **Summarize audio transcripts**. For example, convert a podcast into a tutorial, or a meeting recording into actions.
3. **Legal Proceeding Analysis**. Extract case citations, dates, and other details from a legal debate.
4. **Medical Consultation Summary**. Extract treatments, medications, details of next visit, etc. from a medical consultation.

Here's how to use Gemini to transcribe audio files.

1. Get a [Gemini API key](https://aistudio.google.com/app/apikey) from Google AI Studio.
2. Set the `GEMINI_API_KEY` environment variable to the API key.
3. Set the `MP3_FILE` environment variable to the path of the MP3 file you want to transcribe.
4. Run this code:
 ```bash
 curl -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-002:streamGenerateContent?alt=sse \
 -H "X-Goog-API-Key: $GEMINI_API_KEY" \
 -H "Content-Type: application/json" \
 -d "$(cat << EOF
 {
 "contents": [
 {
 "role": "user",
 "parts": [
 {
 "inline_data": {
 "mime_type": "audio/mp3",
 "data": "$(base64 --wrap=0 $MP3_FILE)"
 }
 },
 {"text": "Transcribe this"}
 ]
 }
 ]
 }
 EOF
 )"
 ```
