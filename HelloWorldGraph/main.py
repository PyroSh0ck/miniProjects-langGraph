from typing import Dict, TypedDict
from langgraph.graph import StateGraph

# Creating an AgentState - Remember its a shared data element/structure thing that all nodes will udpate


# This is also known as the state schema
class AgentState(TypedDict):
    message: str


# Defining a node (input and output must both be the state because a node just updates a state)


def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""

    state["message"] = "Hey " + state["message"] + ", how is your day going?"

    return state


# Creating the StateGraph:

graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)

# Adding the start and end nodes
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"message": "Bob"})

print(result["message"])
