from typing import TypedDict, List
from langchain_core.documents import Document


class AgentState(TypedDict):

    question: str

    documents: List[Document]

    answer: str

    review_status: str