# RAG API with FastAPI

A FastAPI-based API that implements Retrieval-Augmented Generation (RAG) for question answering. This project combines FAISS for efficient similarity search with OpenAI's language models to provide accurate answers based on a custom knowledge base.

## Project Overview

This project implements a RAG (Retrieval-Augmented Generation) system that:
1. Stores text documents as vector embeddings using FAISS
2. Retrieves relevant context based on user questions
3. Generates accurate answers using OpenAI's language models or Gemini's language models

## Features

- FastAPI endpoints for querying the knowledge base
- Vector similarity search using FAISS
- Integration with OpenAI or Gemini for answer generation
- Asynchronous file operations with aiofiles
- Automatic API documentation with FastAPI
- Hot reload support for development

## Project Structure

```
├── main.py              # FastAPI application and routes
├── knowledge.txt        # Knowledge base content
├── requirements.txt     # Project dependencies
├── core/
│   └── lifespan.py     # Application lifecycle management
└── utils/
    ├── embeddings.py   # Vector store implementation
    |── rag_pipeline.py # OpenAI RAG pipeline implementation
    └── gemini_rag_pipeline.py # Gemini RAG pipeline implementation
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd RAG
```

2. Create and activate a virtual environment:
```bash
python -m venv rag_env
# Windows
.\rag_env\Scripts\activate
# Unix/MacOS
source rag_env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Add your knowledge base content to `knowledge.txt` (one statement per line)

2. Start the FastAPI server:
```bash
python main.py
```
Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoints

### GET /
- Purpose: Check the status of embeddings initialization
- Response: Confirms if embeddings are loaded

### GET /ask
- Purpose: Query the RAG system with a question
- Parameters:
  - `question` (string): The question to ask about the knowledge base
- Returns: JSON with question, retrieved context, and generated answer

Example query:
```
GET /ask?question=What is FastAPI?
```

## Dependencies

Key dependencies include:
- FastAPI
- FAISS-CPU
- OpenAI
- Gemini
- Sentence-Transformers
- Python-dotenv
- Uvicorn

For a complete list of dependencies, see `requirements.txt`.

## Development

The project uses FastAPI's hot reload feature for development. Any changes to the code will automatically restart the server.