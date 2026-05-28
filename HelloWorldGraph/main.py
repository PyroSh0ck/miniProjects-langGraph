from typing import Dict, TypedDict
from langgraph.graph import StateGraph

# Creating an AgentState - Remember its a shared data element/structure thing that all nodes will udpate


class AgentState(TypedDict):
    message: str


# Defining a node (input and output must both be the state because a node just updates a state)


def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""

    state["message"] = "Hey" + state["message"] + ", how is your day going?"

    return state
