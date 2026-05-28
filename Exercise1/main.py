from typing import TypedDict
from langgraph.graph import StateGraph


class SharedState(TypedDict):
    name: str


# Node:
def node_complimentor(state: SharedState) -> SharedState:
    """Simple function for a node to add a compliment to the state"""
    state["name"] += ", you're doing an amazing job learning LangGraph!"
    return state


graph = StateGraph(SharedState)  # state schema

# creating Node
graph.add_node("complimentor", node_complimentor)

graph.set_entry_point("complimentor")
graph.set_finish_point("complimentor")

app = graph.compile()

response = app.invoke({"name": "Bob"})
print(response["name"])
