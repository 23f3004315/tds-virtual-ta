---
chunk_id: course_llm_video_screen_scraping_001
source_url: https://tds.s-anand.net/#/llm-video-screen-scraping
source_title: llm-video-screen-scraping
content_type: course
tokens: 505
---

 - Select specific screen area containing target data
 - Record scrolling/clicking through content
 - Keep recordings short (30-60 seconds)
2. **Process with Gemini**
 - Upload to [Google AI Studio](https://makersuite.google.com/app/prompts)
 - Select Gemini 1.5 Flash (cost-effective)
 - Prompt for structured output (JSON/CSV)

---

Example prompt for extracting tabular data:

```text
Turn this video into a JSON array where each item has:
{
 "date": "yyyy-mm-dd",
 "amount": float
}
```

### Cost Calculation

Gemini 1.5 Flash pricing (as of January 2025):

- $0.075 per million tokens
- Cost per frame ~ 250 tokens
- Cost for 24 hours of video at 1 frame per second ~ $1.62!

### Best Practices

1. **Recording Quality**
 - Frame only relevant content
 - Pause briefly on important data
 - Maintain consistent scroll speed
 - Use high contrast display settings
2. **Data Validation**
 - Always verify critical data manually
 - Use spot-checking for large datasets
 - Consider running multiple passes
 - Log and review any anomalies
3. **Error Handling**
 - Request data in simple formats (CSV/JSON)
 - Include validation in prompts
 - Split long videos into segments
 - Handle missing/partial data gracefully

### Use Cases

1. **Data Extraction**
 - Email content aggregation
 - Dashboard metrics collection
 - Protected web content
 - Legacy system data
2. **Data Journalism**
 - Public records analysis
 - Time-series data collection
 - Interactive visualization data
 - Government website scraping
3. **Business Intelligence**
 - Competitor pricing analysis
 - Market research data
 - Internal system migration
 - Legacy report conversion

Tools:

- [Google AI Studio](https://aistudio.google.com/app/prompts): Process videos with Gemini
- [QuickTime Player](https://support.apple.com/guide/quicktime-player/welcome/mac): Screen recording (Mac)
- [Screen2Gif](https://www.screentogif.com/): Screen recording (Windows)
- [OBS Studio](https://obsproject.com/): Advanced screen recording (cross-platform)

References:

- [Simon Willison's Video Scraping Tutorial](https://simonwillison.net/2024/Oct/17/video-scraping/)
- [Gemini API Documentation](https://ai.google.dev/docs)
