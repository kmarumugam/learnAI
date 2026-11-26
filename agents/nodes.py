from services.vector_store import get_store

from services.anthropic_service import (
    invoke_claude
)


def retrieve_node(state):

    db = get_store()

    docs = db.similarity_search(
        state["question"],
        k=5
    )

    return {
        "documents": docs
    }


def answer_node(state):

    context = "\n\n".join(
        [
            d.page_content
            for d in state["documents"]
        ]
    )

    prompt = f"""
Answer the user question using
ONLY the provided context.

Context:
{context}

Question:
{state["question"]}

Provide concise answer.
"""

    answer = invoke_claude(prompt)

    return {
        "answer": answer
    }


def review_node(state):

    context = "\n\n".join(
        [
            d.page_content
            for d in state["documents"]
        ]
    )

    prompt = f"""
Question:
{state['question']}

Answer:
{state['answer']}

Context:
{context}

Determine whether answer is
supported by context.

Return only:

PASS

or

FAIL
"""

    result = invoke_claude(prompt)

    return {
        "review_status": result
    }