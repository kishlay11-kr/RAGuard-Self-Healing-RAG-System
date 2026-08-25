import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="raguard_documents"
        )

    def store_chunks(self, chunks, embeddings):

        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        embedding_data = (
            embeddings.tolist()
            if hasattr(embeddings, "tolist")
            else embeddings
        )

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embedding_data
        )

    def search(self, query_embedding, top_k=3):

        embedding_data = (
            query_embedding.tolist()
            if hasattr(query_embedding, "tolist")
            else query_embedding
        )

        results = self.collection.query(
            query_embeddings=[embedding_data],
            n_results=top_k
        )

        return results

    def count_documents(self):
        return self.collection.count()