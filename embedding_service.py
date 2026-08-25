from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, chunks):

        # Prevent empty input
        if not chunks:
            print("No chunks found")
            return []

        print(f"Generating embeddings for {len(chunks)} chunks")

        embeddings = self.model.encode(
            chunks,
            show_progress_bar=True
        )

        print(f"Generated {len(embeddings)} embeddings")

        return embeddings