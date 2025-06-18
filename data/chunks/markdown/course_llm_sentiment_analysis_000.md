---
chunk_id: course_llm_sentiment_analysis_000
source_url: https://tds.s-anand.net/#/llm-sentiment-analysis
source_title: llm-sentiment-analysis
content_type: course
tokens: 497
---

## LLM Sentiment Analysis

[OpenAI's API](https://platform.openai.com/) provides access to language models like GPT 4o, GPT 4o mini, etc.

For more details, read OpenAI's guide for:

- [Text Generation](https://platform.openai.com/docs/guides/text-generation)
- [Vision](https://platform.openai.com/docs/guides/vision)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Start with this quick tutorial:

[**[Course Image: OpenAI API Quickstart: Send your First API Request]** This image shows how to set up your OpenAI API key within the `.zshrc` configuration file, typically used for shell environments like Zsh. To properly configure your environment for LLM sentiment analysis, you should add the line `export OPENAI_API_KEY='your_api_key'` (replacing `'your_api_key'` with your actual key) to your `.zshrc` file. This command sets the OpenAI API key as an environment variable, which allows your Python scripts or other applications to access the OpenAI service for tasks like analyzing text sentiment; remember to source your `.zshrc` file or restart your terminal session for the changes to take effect. Failing to set the API key correctly will prevent you from authenticating with the OpenAI API, causing your sentiment analysis tasks to fail. This step ensures that your applications can securely access OpenAI's LLMs for sentiment analysis and other NLP tasks.t analysis within your LLM project, you need to configure your API key. This involves editing your `.zshrc` file to include the line `export OPENAI_API_KEY='your_actual_api_key'`, replacing 'your_actual_api_key' with the key you obtained from OpenAI. Adding `export OPENAI_API_KEY='sk-proj-qZIGbilFyPY` to the .zshrc file ensures that the OpenAI API key is set as an environment variable, allowing your Python scripts to securely access the OpenAI API for sentiment analysis tasks. Once the key is in place, remember to source your `.zshrc` file with `source ~/.zshrc` or restart your terminal to apply the changes, enabling you to then call the API in your sentiment analysis code.)](https://youtu.be/Xz4ORA0cOwQ)
