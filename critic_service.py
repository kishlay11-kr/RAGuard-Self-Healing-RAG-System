from langchain_groq import ChatGroq

from app.core.config import settings


class CriticService:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=settings.GROQ_API_KEY
        )

    def evaluate_answer(
        self,
        query,
        answer,
        retrieved_chunks
    ):

        context = "\n".join(
            retrieved_chunks
        )

        prompt = f"""
You are a strict AI evaluator for a self-healing RAG system.

Evaluate the answer based on these rules:

1. Groundedness
- The answer must be supported by the provided context.
- If information is invented or unsupported, return FAIL.

2. Hallucination Check
- Do not allow fabricated facts.
- If the answer contains unsupported claims, return FAIL.

3. Completeness
- The answer must fully address the question.
- If the answer is vague, too short, partially correct,
  or missing important details, return FAIL.

Evaluation Rules:
- PASS only if the answer is correct, grounded,
  and sufficiently complete.
- FAIL if the answer is incomplete,
  even if partially correct.
- Be strict.

Return ONLY in this exact format:

VERDICT: PASS or FAIL
REASON: short reason

Context:
{context}

Question:
{query}

Answer:
{answer}
"""

        response = self.llm.invoke(
            prompt
        )

        return response.content