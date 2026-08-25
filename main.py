from fastapi import FastAPI
from app.api.v1.upload import router as upload_router
from app.api.v1.query import router as query_router

app = FastAPI(
    title="RAGuard AI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "RAGuard API Running 🚀",
        "status": "active"
    }


app.include_router(
    upload_router,
    prefix="/api/v1/upload",
    tags=["Upload"]
)

app.include_router(
    query_router,
    prefix="/api/v1/query",
    tags=["Query"]
)