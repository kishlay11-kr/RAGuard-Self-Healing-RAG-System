from langchain_groq import ChatGroq

from app.core.config import settings


class ReformulationService:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=settings.GROQ_API_KEY
        )

    def reformulate_query(
        self,
        query
    ):

        prompt = f"""
        Rewrite the query only if needed.

        Rules:
        - Fix spelling mistakes
        - Make query clearer
        - Keep it short
        - Do NOT over-explain
        - Preserve user intent
        - Return ONLY the improved query

        Examples:
        "waht is joins" → "what are SQL joins"
        "lef join" → "left join in SQL"

        Query:
        {query}
        """

        response = self.llm.invoke(
            prompt
        )

        return response.content.strip()