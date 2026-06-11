# RAGuard 🚀

A self-healing RAG pipeline for intelligent document question answering using LangGraph, FastAPI, and ChromaDB.

## Problem
Traditional RAG systems often fail when user queries are vague, ambiguous, or retrieval quality is poor.

## Solution
RAGuard introduces a self-healing retrieval pipeline with:
- Critic-based answer evaluation
- Automatic query reformulation
- Multi-step retrieval retry
- Context-aware response generation

## Features
✅ PDF Upload & Processing  
✅ ChromaDB Vector Store  
✅ LangGraph Workflow  
✅ Critic Agent  
✅ Query Reformulation  
✅ Self-Healing Retrieval  
✅ FastAPI Backend  
✅ Swagger API Testing

## Architecture
[Add architecture image]

## Tech Stack
- LangChain
- LangGraph
- FastAPI
- ChromaDB
- Sentence Transformers
- Python

## API Demo

### Upload PDF
POST `/api/v1/upload`

### Query Document
POST `/api/v1/query`

Example:

```json
{
  "question": "Summarize SQL joins"
}
```

## Future Improvements
- Frontend dashboard
- Confidence scoring
- Multi-document retrieval
- Evaluation metrics

## Author
Kishlay Kumar
