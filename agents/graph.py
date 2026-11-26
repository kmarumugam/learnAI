from langgraph.graph import (
    StateGraph,
    END
)

from agents.state import AgentState

from agents.nodes import (
    retrieve_node,
    answer_node,
    review_node
)

builder = StateGraph(
    AgentState
)

builder.add_node(
    "retrieve",
    retrieve_node
)

builder.add_node(
    "answer",
    answer_node
)

builder.add_node(
    "review",
    review_node
)

builder.set_entry_point(
    "retrieve"
)

builder.add_edge(
    "retrieve",
    "answer"
)

builder.add_edge(
    "answer",
    "review"
)

builder.add_edge(
    "review",
    END
)

graph = builder.compile()