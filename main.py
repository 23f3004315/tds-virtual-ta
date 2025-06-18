#!/usr/bin/env python3
"""
TDS Virtual TA - Updated FastAPI Implementation
Updated to match actual directory structure from successful chunking/embedding scripts
"""

import os
import json
import base64
import numpy as np
import faiss
from pathlib import Path
from typing import List, Dict, Optional, Any, Tuple
from datetime import datetime
import logging
import time
import traceback

# FastAPI and related imports
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel, Field
import uvicorn

# ML and embedding imports
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from PIL import Image
import io
import torch

# Configure comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'tds_api_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("tds_virtual_ta")

# Pydantic models matching exact project specification
class QueryRequest(BaseModel):
    """Request model matching exact project specification for evaluation"""
    question: str = Field(..., description="Student question", min_length=1)
    image: Optional[str] = Field(None, description="Base64 encoded image")

class LinkResponse(BaseModel):
    """Individual source link response model for evaluation compliance"""
    url: str = Field(..., description="Direct source URL")
    text: str = Field(..., description="Human-readable link description")

class QueryResponse(BaseModel):
    """Response model matching exact project specification"""
    answer: str = Field(..., description="AI-generated response")
    links: List[LinkResponse] = Field(..., description="Source attribution links")

class HealthResponse(BaseModel):
    """Health check response model"""
    status: str
    total_chunks: int
    course_chunks: int
    discourse_chunks: int
    embedding_model: str
    gemini_available: bool
    timestamp: str

class TDSVirtualTACore:
    """
    Core TDS Virtual Teaching Assistant implementation
    Updated for actual directory structure from successful scripts
    """
    
    def __init__(self):
        """Initialize the Virtual TA with actual directory structure"""
        logger.info("🤖 Initializing TDS Virtual Teaching Assistant")
        
        # **CORRECTED PATHS** - Based on your actual successful scripts
        self.base_path = Path(".")
        
        # Actual embedding directory structure from your scripts
        self.embeddings_dir = self.base_path / "data" / "embeddings"
        self.chunks_dir = self.base_path / "data" / "chunks" / "markdown"
        self.metadata_index_dir = self.base_path / "data" / "chunks" / "metadata_index"
        
        # **ACTUAL FILE NAMES** from your successful embedding script
        self.embeddings_file = self.embeddings_dir / "embeddings_complete.npz"  # Your actual file
        self.faiss_index_file = self.embeddings_dir / "faiss_index.bin"        # Your actual file
        self.metadata_file = self.embeddings_dir / "embeddings_metadata.json"  # Your actual file
        
        # Validation flags
        self.initialization_complete = False
        self.embeddings_loaded = False
        self.model_loaded = False
        self.gemini_configured = False
        
        # Performance monitoring
        self.query_count = 0
        self.total_response_time = 0.0
        self.error_count = 0
        
        # Initialize components
        try:
            self._validate_actual_file_structure()
            self._load_actual_embeddings_and_metadata()
            self._load_faiss_index()
            self._load_bge_model()
            self._setup_gemini()
            self.initialization_complete = True
            logger.info("✅ TDS Virtual TA initialization completed successfully")
        except Exception as e:
            logger.error(f"❌ Critical initialization failure: {e}")
            logger.error(traceback.format_exc())
            raise RuntimeError(f"TDS Virtual TA initialization failed: {e}")
    
    def _validate_actual_file_structure(self) -> None:
        """Validate actual files created by your successful scripts"""
        logger.info("🔍 Validating actual file structure from successful scripts")
        
        # Check files actually created by your embedding script
        required_files = [
            self.embeddings_file,           # embeddings_complete.npz
            self.faiss_index_file,          # faiss_index.bin
            self.metadata_file,             # embeddings_metadata.json
        ]
        
        # Check if chunks directory exists
        if not self.chunks_dir.exists():
            raise FileNotFoundError(f"Chunks directory not found: {self.chunks_dir}")
        
        # Check for chunk files
        chunk_files = list(self.chunks_dir.glob("*.md"))
        if len(chunk_files) == 0:
            raise FileNotFoundError(f"No chunk files found in: {self.chunks_dir}")
        
        # Check required embedding files
        missing_files = [f for f in required_files if not f.exists()]
        if missing_files:
            raise FileNotFoundError(f"Critical files missing: {missing_files}")
        
        logger.info(f"✅ All required files validated")
        logger.info(f"📄 Found {len(chunk_files)} chunk files")
        logger.info(f"📦 Embeddings file: {self.embeddings_file}")
        logger.info(f"🔍 FAISS index: {self.faiss_index_file}")
        logger.info(f"📊 Metadata file: {self.metadata_file}")
    
    def _load_actual_embeddings_and_metadata(self) -> None:
        """Load embeddings from your actual .npz format"""
        logger.info("📂 Loading embeddings from actual .npz format")
        
        try:
            # Load your actual .npz embeddings file
            logger.info(f"Loading embeddings from: {self.embeddings_file}")
            
            with np.load(self.embeddings_file) as data:
                # Load arrays based on your actual script output
                self.embeddings = data['embeddings']
                self.chunk_ids_array = data['chunk_ids']
                self.source_urls_array = data['source_urls']
                self.source_titles_array = data['source_titles']
                self.content_types_array = data['content_types']
                
                # Optional arrays from your enhanced script
                if 'usernames' in data.files:
                    self.usernames_array = data['usernames']
                else:
                    self.usernames_array = np.array([''] * len(self.chunk_ids_array))
                
                if 'topic_ids' in data.files:
                    self.topic_ids_array = data['topic_ids']
                else:
                    self.topic_ids_array = np.array([''] * len(self.chunk_ids_array))
                
                if 'post_numbers' in data.files:
                    self.post_numbers_array = data['post_numbers']
                else:
                    self.post_numbers_array = np.array([0] * len(self.chunk_ids_array))
            
            # Convert arrays to lists for easier handling
            self.chunk_ids = self.chunk_ids_array.tolist()
            self.source_urls = self.source_urls_array.tolist()
            self.source_titles = self.source_titles_array.tolist()
            self.content_types = self.content_types_array.tolist()
            self.usernames = self.usernames_array.tolist()
            self.topic_ids = self.topic_ids_array.tolist()
            self.post_numbers = self.post_numbers_array.tolist()
            
            # Load metadata from your actual metadata file
            logger.info(f"Loading metadata from: {self.metadata_file}")
            
            if self.metadata_file.exists():
                with open(self.metadata_file, 'r', encoding='utf-8') as f:
                    self.embedding_metadata_summary = json.load(f)
            else:
                self.embedding_metadata_summary = {}
            
            # Create metadata index for chunk lookup
            self.metadata_index = {}
            for i, chunk_id in enumerate(self.chunk_ids):
                self.metadata_index[chunk_id] = {
                    'chunk_id': chunk_id,
                    'source_url': self.source_urls[i],
                    'source_title': self.source_titles[i],
                    'content_type': self.content_types[i],
                    'username': self.usernames[i] if i < len(self.usernames) else '',
                    'topic_id': self.topic_ids[i] if i < len(self.topic_ids) else '',
                    'post_number': self.post_numbers[i] if i < len(self.post_numbers) else 0,
                    'embedding_index': i
                }
            
            # Calculate statistics
            self.total_chunks = len(self.chunk_ids)
            self.course_chunks = len([ct for ct in self.content_types if ct == 'course'])
            self.discourse_chunks = len([ct for ct in self.content_types if ct == 'discourse'])
            
            self.embeddings_loaded = True
            logger.info(f"✅ Loaded embeddings successfully")
            logger.info(f"📊 Total chunks: {self.total_chunks}")
            logger.info(f"📚 Course chunks: {self.course_chunks}")
            logger.info(f"💬 Discourse chunks: {self.discourse_chunks}")
            logger.info(f"🔢 Embedding shape: {self.embeddings.shape}")
            
        except Exception as e:
            logger.error(f"❌ Failed to load embeddings: {e}")
            raise
    
    def _load_faiss_index(self) -> None:
        """Load FAISS index from your actual file"""
        logger.info(f"🔍 Loading FAISS index from: {self.faiss_index_file}")
        
        try:
            self.faiss_index = faiss.read_index(str(self.faiss_index_file))
            logger.info(f"✅ FAISS index loaded with {self.faiss_index.ntotal} vectors")
        except Exception as e:
            logger.error(f"❌ Failed to load FAISS index: {e}")
            raise
    
    def _load_bge_model(self) -> None:
        """Load BGE model (same as used in your embedding generation)"""
        logger.info("📥 Loading BGE-large-en-v1.5 for CPU inference")
        
        try:
            # Load the same model used in your embedding script
            self.embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
            self.embedding_model.eval()
            
            # CPU optimizations
            torch.set_num_threads(4)
            
            # Disable gradients for inference
            for param in self.embedding_model.parameters():
                param.requires_grad = False
            
            # Test embedding
            test_query = "TDS Student Question: What is data science?"
            _ = self.embedding_model.encode([test_query], normalize_embeddings=True)
            
            self.model_loaded = True
            logger.info("✅ BGE model loaded and optimized for CPU inference")
            
        except Exception as e:
            logger.error(f"❌ Failed to load BGE model: {e}")
            raise
    
    def _setup_gemini(self) -> None:
        """Configure Gemini API for response generation"""
        logger.info("🔧 Configuring Gemini API")
        
        # Try multiple environment variable names
        api_key = (os.getenv('GEMINI_API_KEY') or 
                  os.getenv('GEMINI_PROJECT1_KEY') or 
                  os.getenv('GOOGLE_API_KEY'))
        
        if not api_key:
            logger.warning("⚠️ No Gemini API key found - response generation will be limited")
            self.gemini_configured = False
            return
        
        try:
            genai.configure(api_key=api_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            # Test connection
            test_response = self.gemini_model.generate_content("Test connection")
            if test_response and test_response.text:
                self.gemini_configured = True
                logger.info("✅ Gemini API configured and tested successfully")
            else:
                raise ValueError("Gemini test failed")
                
        except Exception as e:
            logger.error(f"❌ Failed to configure Gemini: {e}")
            self.gemini_configured = False
    
    def _embed_query_optimized(self, query_text: str) -> np.ndarray:
        """Generate optimized embedding for user query"""
        try:
            # Use same context as your embedding generation
            contextualized_query = f"Question: {query_text}"
            
            # Generate embedding with same settings as your script
            with torch.no_grad():
                embedding = self.embedding_model.encode(
                    [contextualized_query],
                    normalize_embeddings=True,
                    convert_to_numpy=True,
                    show_progress_bar=False,
                    device='cpu'
                )
            
            return embedding[0]
            
        except Exception as e:
            logger.error(f"Query embedding error: {e}")
            raise
    
    def _retrieve_relevant_chunks_with_faiss(self, question: str, top_k: int = 5) -> List[Dict]:
        """Retrieve relevant chunks using your FAISS index"""
        logger.info(f"🔍 Retrieving relevant chunks using FAISS")
        
        try:
            # Generate query embedding
            query_embedding = self._embed_query_optimized(question)
            
            # Use your FAISS index for similarity search
            similarity_scores, chunk_indices = self.faiss_index.search(
                query_embedding.reshape(1, -1).astype(np.float32), 
                top_k
            )
            
            relevant_chunks = []
            
            for i, (score, idx) in enumerate(zip(similarity_scores[0], chunk_indices[0])):
                if idx == -1:  # FAISS returns -1 for no match
                    continue
                
                chunk_id = self.chunk_ids[idx]
                chunk_metadata = self.metadata_index.get(chunk_id, {})
                
                relevant_chunks.append({
                    'chunk_id': chunk_id,
                    'metadata': chunk_metadata,
                    'similarity': float(score),
                    'rank': i + 1,
                    'embedding_index': idx
                })
            
            logger.info(f"✅ Retrieved {len(relevant_chunks)} relevant chunks")
            if relevant_chunks:
                logger.info(f"📊 Similarity range: {relevant_chunks[0]['similarity']:.3f} - {relevant_chunks[-1]['similarity']:.3f}")
            
            return relevant_chunks
            
        except Exception as e:
            logger.error(f"Chunk retrieval error: {e}")
            raise
    
    def _load_chunk_content(self, chunk_id: str) -> str:
        """Load actual chunk content from your markdown files"""
        try:
            # Use your actual chunks directory
            markdown_file = self.chunks_dir / f"{chunk_id}.md"
            
            if markdown_file.exists():
                with open(markdown_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract content after YAML frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        return parts[2].strip()
                
                return content
            else:
                logger.warning(f"Chunk file not found: {markdown_file}")
                return "Content not available"
                
        except Exception as e:
            logger.error(f"Error loading chunk content for {chunk_id}: {e}")
            return "Error loading content"
    
    def _process_image_with_gemini(self, base64_image: str, question: str) -> str:
        """Process uploaded image using Gemini"""
        if not self.gemini_configured:
            return "Image uploaded but processing unavailable (Gemini API not configured)"
        
        try:
            # Decode base64 image
            image_data = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(image_data))
            
            # Educational context prompt
            prompt = f"""
            You are a teaching assistant for the TDS (Tools in Data Science) course.
            
            Student question: {question}
            
            Analyze this image in the context of data science tools and techniques.
            Focus on code errors, visualizations, configurations, or tool usage.
            Provide specific technical insights related to the student's question.
            """
            
            result = self.gemini_model.generate_content([prompt, image])
            
            if result and result.text:
                return result.text.strip()
            else:
                return "Unable to analyze image content"
                
        except Exception as e:
            logger.error(f"Image processing error: {e}")
            return f"Image processing failed: {str(e)}"
    
    def _generate_response_with_context(self, question: str, relevant_chunks: List[Dict], 
                                      image_description: str = None) -> str:
        """Generate response using Gemini with retrieved context"""
        if not self.gemini_configured:
            return "I apologize, but response generation is currently unavailable due to API configuration issues."
        
        try:
            # Build context from retrieved chunks
            context_parts = []
            
            for chunk in relevant_chunks:
                metadata = chunk['metadata']
                chunk_content = self._load_chunk_content(chunk['chunk_id'])
                
                # Format context based on content type
                if metadata.get('content_type') == 'course':
                    source_info = f"TDS Course Material - {metadata.get('source_title', 'Unknown Topic')}"
                elif metadata.get('content_type') == 'discourse':
                    username = metadata.get('username', 'Community Member')
                    source_info = f"TDS Discussion by {username}"
                else:
                    source_info = "TDS Educational Content"
                
                context_parts.append(f"{source_info}:\n{chunk_content}\n")
            
            context = "\n" + "="*50 + "\n".join(context_parts)
            
            # Construct prompt
            prompt = f"""
You are a knowledgeable Teaching Assistant for the TDS (Tools in Data Science) course.

Student Question: {question}

{f"Image Context: {image_description}" if image_description else ""}

Relevant Course Materials:
{context}

Instructions:
1. Answer comprehensively using the provided materials
2. Include practical examples, code, or step-by-step instructions
3. Reference specific tools and techniques from the course
4. Maintain an encouraging, educational tone
5. If materials don't fully answer the question, acknowledge this

Generate a helpful response:
"""
            
            # Generate response
            try:
                result = self.gemini_model.generate_content(
                    prompt,
                    generation_config={
                        'temperature': 0.7,
                        'top_p': 0.8,
                        'top_k': 40,
                        'max_output_tokens': 1024,
                    }
                )
                
                if result and result.text:
                    return result.text.strip()
                else:
                    return "I apologize, but I'm unable to generate a response at this time."
                    
            except Exception as gen_error:
                logger.error(f"Gemini generation error: {gen_error}")
                return "I encountered an error while generating the response. Please try again."
                
        except Exception as e:
            logger.error(f"Response generation error: {e}")
            return "I apologize, but I encountered an error while processing your question."
    
    def _extract_source_links_validated(self, relevant_chunks: List[Dict]) -> List[LinkResponse]:
        """Extract validated source links from your actual data"""
        logger.info("🔗 Extracting source links from actual metadata")
        
        links = []
        seen_urls = set()
        
        try:
            for chunk in relevant_chunks:
                metadata = chunk['metadata']
                
                # Get source URL from your actual data structure
                source_url = metadata.get('source_url', '').strip()
                if not source_url or source_url in seen_urls:
                    continue
                
                if not source_url.startswith('http'):
                    continue
                
                # Create link based on content type
                if metadata.get('content_type') == 'course':
                    title = metadata.get('source_title', 'TDS Course Material')
                    link_text = f"Course: {title}"
                    
                elif metadata.get('content_type') == 'discourse':
                    username = metadata.get('username', 'Community')
                    post_number = metadata.get('post_number', '')
                    
                    link_text = f"Discussion by {username}"
                    if post_number:
                        link_text += f" (Post #{post_number})"
                
                else:
                    link_text = metadata.get('source_title', 'TDS Content')
                
                links.append(LinkResponse(url=source_url, text=link_text))
                seen_urls.add(source_url)
                
                # Limit to 5 links
                if len(links) >= 5:
                    break
            
            logger.info(f"✅ Generated {len(links)} source links")
            return links
            
        except Exception as e:
            logger.error(f"Source link extraction error: {e}")
            return []
    
    async def process_query_complete(self, request: QueryRequest) -> QueryResponse:
        """Complete query processing pipeline"""
        start_time = time.time()
        self.query_count += 1
        
        logger.info(f"🤖 Processing query #{self.query_count}")
        
        try:
            # Process image if provided
            image_description = None
            if request.image:
                logger.info("🖼️ Processing uploaded image")
                image_description = self._process_image_with_gemini(request.image, request.question)
            
            # Retrieve relevant chunks using your FAISS index
            relevant_chunks = self._retrieve_relevant_chunks_with_faiss(request.question)
            
            if not relevant_chunks:
                return QueryResponse(
                    answer="I couldn't find relevant information in the TDS course materials to answer your question. Please try rephrasing your question.",
                    links=[]
                )
            
            # Generate response
            answer = self._generate_response_with_context(
                request.question, 
                relevant_chunks, 
                image_description
            )
            
            # Extract source links
            source_links = self._extract_source_links_validated(relevant_chunks)
            
            # Performance tracking
            response_time = time.time() - start_time
            self.total_response_time += response_time
            
            logger.info(f"✅ Query processed in {response_time:.2f}s")
            
            return QueryResponse(answer=answer, links=source_links)
            
        except Exception as e:
            self.error_count += 1
            logger.error(f"❌ Query processing error: {e}")
            
            return QueryResponse(
                answer="I apologize, but I encountered an error while processing your question. Please try again.",
                links=[]
            )
    
    def get_system_health(self) -> Dict:
        """Get system health information"""
        avg_response_time = (self.total_response_time / self.query_count 
                           if self.query_count > 0 else 0.0)
        
        return {
            "status": "healthy" if self.initialization_complete else "initializing",
            "total_chunks": self.total_chunks if self.embeddings_loaded else 0,
            "course_chunks": self.course_chunks if self.embeddings_loaded else 0,
            "discourse_chunks": self.discourse_chunks if self.embeddings_loaded else 0,
            "embedding_model": "BGE-large-en-v1.5" if self.model_loaded else "not_loaded",
            "gemini_available": self.gemini_configured,
            "performance": {
                "queries_processed": self.query_count,
                "average_response_time": round(avg_response_time, 2),
                "error_count": self.error_count,
                "error_rate": round(self.error_count / max(self.query_count, 1) * 100, 2)
            },
            "timestamp": datetime.now().isoformat()
        }

# Initialize FastAPI application
app = FastAPI(
    title="TDS Virtual Teaching Assistant",
    description="AI-powered teaching assistant for Tools in Data Science course with comprehensive source attribution",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Security and CORS middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Virtual TA instance
virtual_ta: Optional[TDSVirtualTACore] = None

@app.on_event("startup")
async def startup_event():
    """Initialize the Virtual TA on application startup"""
    global virtual_ta
    
    logger.info("🚀 Starting TDS Virtual TA API")
    
    try:
        virtual_ta = TDSVirtualTACore()
        logger.info("✅ TDS Virtual TA startup completed successfully")
    except Exception as e:
        logger.error(f"❌ Critical startup failure: {e}")
        virtual_ta = None

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on application shutdown"""
    logger.info("🔄 TDS Virtual TA API shutting down")
    global virtual_ta
    virtual_ta = None

@app.post("/api/", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    """Main API endpoint for TDS Virtual Teaching Assistant"""
    if virtual_ta is None or not virtual_ta.initialization_complete:
        raise HTTPException(
            status_code=503, 
            detail="TDS Virtual TA service not initialized or unavailable"
        )
    
    logger.info(f"📝 Received question from client")
    
    try:
        response = await virtual_ta.process_query_complete(request)
        logger.info(f"✅ Successfully generated response with {len(response.links)} source links")
        return response
        
    except Exception as e:
        logger.error(f"❌ API endpoint error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during query processing")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Comprehensive health check endpoint"""
    if virtual_ta is None:
        raise HTTPException(status_code=503, detail="Service not initialized")
    
    health_data = virtual_ta.get_system_health()
    
    return HealthResponse(
        status=health_data["status"],
        total_chunks=health_data["total_chunks"],
        course_chunks=health_data["course_chunks"],
        discourse_chunks=health_data["discourse_chunks"],
        embedding_model=health_data["embedding_model"],
        gemini_available=health_data["gemini_available"],
        timestamp=health_data["timestamp"]
    )

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "TDS Virtual Teaching Assistant API",
        "description": "AI-powered TA for Tools in Data Science course",
        "version": "1.0.0",
        "evaluation_ready": True,
        "endpoints": {
            "ask": "POST /api/ - Ask questions with optional image upload",
            "health": "GET /health - System health and performance metrics",
            "docs": "GET /docs - Interactive API documentation"
        },
        "features": [
            "BGE-large-en-v1.5 embeddings for semantic search",
            "FAISS index for fast similarity search",
            "Gemini-powered response generation",
            "Comprehensive source attribution",
            "Image analysis support",
            "Course and discourse content integration"
        ]
    }

# Production server configuration
if __name__ == "__main__":
    logger.info("🚀 Starting TDS Virtual TA API server")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 7860)),  # HuggingFace Spaces compatibility
        log_level="info",
        access_log=True
    )
