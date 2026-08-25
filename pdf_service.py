import fitz


class PDFService:

    @staticmethod
    def extract_text(pdf_path: str):
        document = fitz.open(pdf_path)

        extracted_text = ""

        for page in document:
            extracted_text += page.get_text()

        total_pages = len(document)

        document.close()

        return {
            "pages": total_pages,
            "text": extracted_text,
            "characters": len(extracted_text)
        }

    def search(self, query_embedding, top_k=3):

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k)

        return results

