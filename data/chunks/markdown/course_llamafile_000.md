---
chunk_id: course_llamafile_000
source_url: https://tds.s-anand.net/#/llamafile
source_title: llamafile
content_type: course
tokens: 496
---

## Local LLMs: Llamafile

You would have heard of Large Language Models (LLMs) like GPT-4, Claude, and Llama. Some of these models are available for free, but most of them are not.

An easy way to run LLMs locally is Mozilla's [Llamafile](https://github.com/Mozilla-Ocho/llamafile). It's a single executable file that works on Windows, Mac, and Linux. No installation or configuration needed - just download and run.

Watch this Llamafile Tutorial (6 min):

[**[Course Image: Llamafile: Local LLMs Made Easy]** Llamafile simplifies the process of running local Large Language Models (LLMs). The core idea is to package the LLM and its runtime into a single executable file. This eliminates the need for complex installations or configurations; you simply download and run the file. This approach makes LLMs more accessible and easier to use on various operating systems, streamlining the deployment and execution of these models for local inference. The stated goal of Llamafile is to make local LLMs easy to use.amafile," a tool designed to make running local Large Language Models (LLMs) easier. Llamafile simplifies the deployment and execution of LLMs directly on your machine. It packages the model and the necessary runtime into a single executable file. This allows you to run powerful AI models without relying on cloud services. The tutorial will guide you through the process of downloading and running Llamafile for your projects.)](https://youtu.be/d1Fnfvat6nM)

Here's how to get started

1. [Download `Llama-3.2-1B-Instruct.Q6_K.llamafile` (1.11 GB)](https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile/blob/main/Llama-3.2-1B-Instruct.Q6_K.llamafile?download=true).
2. From the command prompt or terminal, run `Llama-3.2-1B-Instruct.Q6_K.llamafile`.
3. Optional: For GPU acceleration, use `Llama-3.2-1B-Instruct.Q6_K.llamafile --n-gpu-layers 35`. (Increase or decrease the number of layers based on your GPU VRAM.)
