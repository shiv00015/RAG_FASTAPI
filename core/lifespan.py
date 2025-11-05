from contextlib import asynccontextmanager
from utils.embeddings import VectorStore
import aiofiles
from fastapi import FastAPI
from utils.gemini_rag_pipeline import GeminiService

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await load_file(app)
    try:
        yield
    finally:
        if hasattr(app.state.sent, "close"):
            app.state.sent.close()
            
        
async def load_file(app: FastAPI):
    async with aiofiles.open('knowledge.txt', 'r') as f:
        content = await f.read()
        docs = [line.strip() for line in content.splitlines() if line.strip()]
      
    app.state.gemini = GeminiService()
    app.state.sent = VectorStore(docs)
    print('state', app.state)
