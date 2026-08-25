# RAGuard Backend

FastAPI backend for **RAGuard: A Self-Healing RAG Pipeline for Reliable Career & Placement Intelligence**.

This phase only initializes the backend architecture. RAG, ingestion, embeddings, vector storage, and LangGraph workflows will be added in later phases.

## Run Locally

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/api/v1/health
```
