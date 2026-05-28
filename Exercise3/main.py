from typing import TypedDict, List
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    age: int
    skills: List[str]
    final: str


def node_one(state: AgentState) -> AgentState:
    state["final"] = f"{state['name']}, welcome to the system!"
    return state


def node_two(state: AgentState) -> AgentState:
    state["final"] += f" You are {state['age']} years old!"
    return state


def node_three(state: AgentState) -> AgentState:
    state["final"] += (
        " You have skills in: "
        + ", ".join(state["skills"][:-1])
        + ", and "
        + state["skills"][-1]
    )
    return state


graph = StateGraph(AgentState)
graph.add_node("one", node_one)
graph.add_node("two", node_two)
graph.add_node("three", node_three)

graph.set_entry_point("one")
graph.add_edge("one", "two")
graph.add_edge("two", "three")
graph.set_finish_point("three")

app = graph.compile()
response = app.invoke(
    {"name": "Bob", "age": 31, "skills": ["Python", "LangGraph", "Machine Learning"]}
)

print(response["final"])

