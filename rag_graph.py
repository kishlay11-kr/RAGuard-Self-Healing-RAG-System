from typing import TypedDict, Optional

from langgraph.graph import (
    StateGraph,
    END
)

from app.services.retriever_service import (
    RetrieverService
)

from app.services.llm_service import (
    LLMService
)

from app.services.critic_service import (
    CriticService
)

from app.services.reformulation_service import (
    ReformulationService
)


# -----------------------------------
# Graph State
# -----------------------------------
class GraphState(TypedDict):

    query: str

    reformulated_query: Optional[str]

    retrieved_chunks: list

    context: str

    answer: str

    evaluation: str

    self_healed: bool


# -----------------------------------
# Reformulation Node
# -----------------------------------
def reformulate_node(state):

    reformulator = (
        ReformulationService()
    )

    improved_query = (
        reformulator
        .reformulate_query(
            state["query"]
        )
    )

    improved_query = (
        " ".join(
            improved_query.split()
        )
        .replace('"', '')
        .strip()
    )

    # Save only if changed
    if (
        improved_query.lower().strip()
        != state["query"]
        .lower()
        .strip()
    ):
        reformulated_query = (
            improved_query
        )
    else:
        reformulated_query = ""

    final_query = (
        reformulated_query
        if reformulated_query
        else state["query"]
    )

    return {
        "reformulated_query":
        reformulated_query,

        "query":
        state["query"],

        "final_query":
        final_query
    }


# -----------------------------------
# Retrieve Node
# -----------------------------------
def retrieve_node(state):

    retriever = (
        RetrieverService()
    )

    final_query = (
        state.get(
            "reformulated_query"
        )
        or state["query"]
    )

    results = (
        retriever.retrieve(
            final_query
        )
    )

    retrieved_chunks = (
        results.get(
            "documents",
            [[]]
        )[0]
    )

    context = "\n\n".join(
        retrieved_chunks
    )

    return {
        "retrieved_chunks":
        retrieved_chunks,

        "context":
        context
    }


# -----------------------------------
# Answer Node
# -----------------------------------
def answer_node(state):

    llm_service = (
        LLMService()
    )

    final_query = (
        state.get(
            "reformulated_query"
        )
        or state["query"]
    )

    answer = (
        llm_service
        .generate_answer(
            final_query,
            state["context"]
        )
    )

    answer = (
        " ".join(
            answer.split()
        )
        if answer
        else ""
    )

    return {
        "answer":
        answer
    }


# -----------------------------------
# Critic Node
# -----------------------------------
def critic_node(state):

    critic = (
        CriticService()
    )

    evaluation = (
        critic.evaluate_answer(
            state["query"],
            state["answer"],
            state[
                "retrieved_chunks"
            ]
        )
    )

    evaluation = (
        " ".join(
            evaluation.split()
        )
        if evaluation
        else ""
    )

    return {
        "evaluation":
        evaluation
    }


# -----------------------------------
# Retry Decision
# -----------------------------------
def should_heal(state):

    if (
        "FAIL"
        in state["evaluation"]
        .upper()

        and not state.get(
            "self_healed",
            False
        )
    ):
        return "heal"

    return "pass"


# -----------------------------------
# Self Healing Node
# -----------------------------------
def healing_node(state):

    llm_service = (
        LLMService()
    )

    healing_prompt = f"""
    The previous answer was not good enough.

    Critic feedback:
    {state["evaluation"]}

    Rewrite the answer using ONLY the provided context.

    Rules:
    - Stay grounded in context
    - Fix missing information
      if present
    - Do NOT invent facts
    - If context lacks
      information, say so
    - Improve completeness
      and clarity

    Question:
    {state.get(
        "reformulated_query"
    ) or state["query"]}

    Context:
    {state["context"]}
    """

    answer = (
        llm_service
        .llm
        .invoke(
            healing_prompt
        )
        .content
    )

    answer = (
        " ".join(
            answer.split()
        )
        if answer
        else ""
    )

    return {
        "answer":
        answer,

        "self_healed":
        True
    }


# -----------------------------------
# Graph Build
# -----------------------------------
workflow = StateGraph(
    GraphState
)

workflow.add_node(
    "reformulate",
    reformulate_node
)

workflow.add_node(
    "retrieve",
    retrieve_node
)

workflow.add_node(
    "answer",
    answer_node
)

workflow.add_node(
    "critic",
    critic_node
)

workflow.add_node(
    "heal",
    healing_node
)


# Entry point
workflow.set_entry_point(
    "reformulate"
)


# Main flow
workflow.add_edge(
    "reformulate",
    "retrieve"
)

workflow.add_edge(
    "retrieve",
    "answer"
)

workflow.add_edge(
    "answer",
    "critic"
)


# Retry logic
workflow.add_conditional_edges(
    "critic",
    should_heal,
    {
        "heal":
        "heal",

        "pass":
        END
    }
)


# Re-evaluate after healing
workflow.add_edge(
    "heal",
    "critic"
)


graph = workflow.compile()