from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class RetrieverService:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            VectorStore()
        )

    def retrieve(self, query: str):

        query_embedding = (
            self.embedding_service.model.encode(
                query
            )
        )

        results = self.vector_store.search(
            query_embedding
        )

        return results