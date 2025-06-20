---
chunk_id: course_embeddings_000
source_url: https://tds.s-anand.net/#/embeddings
source_title: embeddings
content_type: course
tokens: 416
---

## Embeddings: OpenAI and Local Models

Embedding models convert text into a list of numbers. These are like a map of text in numerical form. Each number represents a feature, and similar texts will have numbers close to each other. So, if the numbers are similar, the text they represent mean something similar.

This is useful because text similarity is important in many common problems:

1. **Search**. Find similar documents to a query.
2. **Classification**. Classify text into categories.
3. **Clustering**. Group similar items into clusters.
4. **Anomaly Detection**. Find an unusual piece of text.

You can run embedding models locally or using an API. Local models are better for privacy and cost. APIs are better for scale and quality.

| Feature | Local Models | API |
| ----------- | -------------------------- | ------------------------- |
| **Privacy** | High | Dependent on provider |
| **Cost** | High setup, low after that | Pay-as-you-go |
| **Scale** | Limited by local resources | Easily scales with demand |
| **Quality** | Varies by model | Typically high |

The [Massive Text Embedding Benchmark (MTEB)](https://huggingface.co/spaces/mteb/leaderboard) provides comprehensive comparisons of embedding models. These models are compared on several parameters, but here are some key ones to look at:

1. **Rank**. Higher ranked models have higher quality.
2. **Memory Usage**. Lower is better (for similar ranks). It costs less and is faster to run.
3. **Embedding Dimensions**. Lower is better. This is the number of numbers in the array. Smaller dimensions are cheaper to store.
4. **Max Tokens**. Higher is better. This is the number of input tokens (words) the model can take in a _single_ input.
5. Look for higher scores in the columns for Classification, Clustering, Summarization, etc. based on your needs.

### Local Embeddings
