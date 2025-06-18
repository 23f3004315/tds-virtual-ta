---
title: "🤖 TDS Virtual Teaching Assistant"
emoji: "👩‍🏫"
colorFrom: "blue"
colorTo: "green"
sdk: docker
app_port: 7860
pinned: false
license: mit
tags:
  - fastapi
  - rag
  - ai
  - education
  - gemini
  - teaching-assistant
short_description: "TDS Virtual TA"
---
TDS Virtual Teaching Assistant
Project Overview
The TDS Virtual Teaching Assistant is an AI-powered question-answering system developed as a student project for the Tools in Data Science course. This application leverages Retrieval-Augmented Generation (RAG) technology to provide intelligent responses to course-related queries with comprehensive source attribution.

Key Features

RAG-based Architecture: Combines semantic search with AI generation for accurate, contextual responses

BGE-Large-EN-v1.5 Embeddings: Open source embedding model 

FAISS Vector Search: Efficient similarity search across course materials and forum discussions

Gemini AI Integration: State-of-the-art language model for natural response generation

Comprehensive Course Integration
Multi-source Knowledge Base: Includes official course materials, assignments, and forum discussions

Real-time Source Attribution: Provides working links to relevant course resources and discourse forum posts

Multi-modal Support: Handles both text queries and image-based questions

Production-Ready Deployment
FastAPI Web Framework: Modern, high-performance API with automatic documentation

Docker Containerization: Consistent deployment across environments

HuggingFace Spaces Hosting: Free cloud deployment 

Git LFS Integration: Efficient handling of large embedding files

Technology Stack
Backend Framework
FastAPI: Async web framework with automatic API documentation

Uvicorn: Lightning-fast ASGI server

Pydantic: Data validation and serialization

AI/ML Components
BGE-Large-EN-v1.5: Quality embeddings

FAISS: Vector similarity search engine

Sentence Transformers: Semantic text processing

Google Gemini: Large language model integration

DevOps & Deployment
Docker: Application containerization

uv: Modern Python dependency management

Git LFS: Large file version control

HuggingFace Spaces: Cloud deployment platform


API Endpoints
Main Endpoints
POST /api/ - Primary Q&A endpoint with optional image support

GET /health - System health check with metrics

GET /docs - Interactive Swagger API documentation

GET / - Application information and status

Accuracy: High-quality responses with source attribution

Availability: 24/7 deployment on HuggingFace Spaces
