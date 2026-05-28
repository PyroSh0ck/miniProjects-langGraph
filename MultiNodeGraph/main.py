from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    age: int
    final: str


def name_node(state: AgentState) -> AgentState:
    """Basic node function for greeting someone by their name"""

    state["final"] = f"Hey {state['name']}, it's great to meet you!"
    return state


def age_node(state: AgentState) -> AgentState:
    state["final"] += f" Your age is {state['age']}!"
    return state


graph = StateGraph(AgentState)
graph.add_node("namer", name_node)
graph.add_node("ager", age_node)
graph.set_entry_point("namer")
graph.add_edge("namer", "ager")
graph.set_finish_point("ager")

app = graph.compile()
response = app.invoke({"name": "Bob", "age": 20})

print(response["final"])
