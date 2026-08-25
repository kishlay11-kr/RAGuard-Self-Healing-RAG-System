# RAGuard — Self-Healing Agentic RAG System

RAGuard is a **self-healing Retrieval-Augmented Generation (RAG) system** designed to provide more reliable answers from uploaded documents.

It combines **semantic retrieval, LLM generation, automated answer criticism, query reformulation, and LangGraph-based workflow orchestration**. If the generated answer fails the critic's evaluation, RAGuard automatically reformulates the query and retries the retrieval-and-generation process.

## Features

* 📄 PDF document ingestion and text extraction
* ✂️ Intelligent text chunking
* 🧠 Sentence Transformer embeddings
* 🔎 Semantic vector retrieval
* 🗄️ ChromaDB vector storage
* 🤖 LLM-based answer generation
* 🔍 Automated critic agent for answer evaluation
* 🔄 Self-healing query reformulation
* 🕸️ LangGraph workflow orchestration
* ⚡ FastAPI backend
* 🔐 Environment-based configuration

## Architecture

```text
User Query
    │
    ▼
Retriever
    │
    ▼
Relevant Document Chunks
    │
    ▼
LLM Generation
    │
    ▼
Generated Answer
    │
    ▼
Critic Agent
    │
    ├── PASS ──────────────► Final Answer
    │
    └── FAIL
          │
          ▼
   Query Reformulation
          │
          ▼
      Re-Retrieve
          │
          ▼
     LLM Generation
```

## Project Structure

```text
RAGuard/
│
├── main.py
├── rag_graph.py
│
├── chunk_service.py
├── pdf_service.py
├── embedding_service.py
├── vector_store.py
├── retriever_service.py
├── llm_service.py
├── critic_service.py
├── reformulation_service.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Core Components

| Component                  | Purpose                                                   |
| -------------------------- | --------------------------------------------------------- |
| `main.py`                  | FastAPI application and API endpoints                     |
| `rag_graph.py`             | LangGraph-based RAG workflow                              |
| `pdf_service.py`           | PDF document processing                                   |
| `chunk_service.py`         | Splits documents into retrieval chunks                    |
| `embedding_service.py`     | Generates semantic embeddings                             |
| `vector_store.py`          | Manages ChromaDB vector storage                           |
| `retriever_service.py`     | Retrieves relevant document chunks                        |
| `llm_service.py`           | Generates answers using the configured LLM                |
| `critic_service.py`        | Evaluates generated answers                               |
| `reformulation_service.py` | Reformulates failed queries for another retrieval attempt |

## Tech Stack

* **Python**
* **FastAPI**
* **LangGraph**
* **ChromaDB**
* **Sentence Transformers**
* **LangChain Text Splitters**
* **LLM APIs**
* **Pydantic**

## How the Self-Healing RAG Works

1. A user uploads a document.
2. The document is extracted and divided into chunks.
3. Each chunk is converted into an embedding.
4. Embeddings are stored in ChromaDB.
5. The user submits a query.
6. Relevant chunks are retrieved using semantic similarity.
7. The LLM generates an answer using the retrieved context.
8. The critic agent evaluates the answer.
9. If the answer passes, it is returned to the user.
10. If it fails, the query is reformulated and the system performs another retrieval and generation cycle.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kishlay11-kr/RAGuard-Self-Healing-RAG-System.git
cd RAGuard-Self-Healing-RAG-System
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:

```bash
copy .env.example .env
```

Add the required LLM/API configuration to `.env`.

**Never commit the actual `.env` file or API keys to GitHub.**

### 5. Start the Backend

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API

### Health Check

```http
GET /api/v1/health
```

### Upload Document

```http
POST /api/v1/upload
```

Uploads and processes a document for retrieval.

### Query

```http
POST /api/v1/query
```

Sends a query through the RAG and self-healing workflow.

## Evaluation

RAGuard can be evaluated using metrics such as:

* Critic Pass Rate
* Self-Healing Rate
* Answer Correctness
* Answer Relevancy
* Response Time

## Limitations

The current document-processing pipeline primarily works with text-based PDF content. Scanned documents, complex tables, and graphical information may require additional OCR and document-understanding capabilities.

## Future Improvements

* OCR support for scanned documents
* Improved table and chart understanding
* More advanced retrieval strategies
* Hybrid keyword + semantic search
* Retrieval reranking
* Better evaluation datasets
* Streaming responses
* Production deployment and monitoring

## License

This project is intended for educational and portfolio purposes.

```
```
