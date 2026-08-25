from langchain_groq import ChatGroq

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=settings.GROQ_API_KEY
        )

    def generate_answer(
        self,
        query,
        retrieved_chunks
    ):

        context = "\n".join(
            retrieved_chunks
        )

        prompt = f"""
        You are a helpful RAG assistant.

        Answer ONLY using the relevant information from the context.

        Do NOT include unrelated topics.
        Do NOT continue into other concepts.
        Keep the answer concise and focused.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        response = self.llm.invoke(
            prompt
        )

        return response.content