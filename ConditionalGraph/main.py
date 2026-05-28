from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    final: int


def add_operation(state: AgentState) -> AgentState:
    state["final"] = state["number1"] + state["number2"]
    return state


def subtract_operation(state: AgentState) -> AgentState:
    state["final"] = state["number1"] - state["number2"]
    return state


def choose_operation(state: AgentState) -> AgentState:
    if state["operation"] == "+":
        return "addition_operation"
    elif state["operation"] == "-":
        return "subtraction_operation"
    else:
        return state


graph = StateGraph(AgentState)
graph.add_node("add_node", add_operation)
graph.add_node("sub_node", subtract_operation)
graph.add_node("router", lambda state: state)

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    choose_operation,
    {"addition_operation": "add_node", "subtraction_operation": "sub_node"},
)
graph.add_edge("add_node", END)
graph.add_edge("sub_node", END)

app = graph.compile()
response = app.invoke({"number1": 20, "number2": 30, "operation": "+"})

print(response["final"])
