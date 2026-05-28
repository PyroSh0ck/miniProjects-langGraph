import random
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    name: str
    counter: int
    number: List[int]


def greeting_node(state: AgentState) -> AgentState:
    """Simple function that says hi to the user"""
    state["name"] = f"Hey {state['name']}, its good to see you!"
    state["number"] = []
    state["counter"] = 0
    return state


def random_node(state: AgentState) -> AgentState:
    """Function that returns a random number 1-10"""
    state["number"].append(random.randint(1, 10))
    state["counter"] += 1
    return state


def should_continue(state: AgentState) -> AgentState:
    if state["counter"] < 5:
        return "loop"
    else:
        return "exit"


graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.add_node("random", random_node)

graph.add_edge(START, "greeter")
graph.add_edge("greeter", "random")
graph.add_conditional_edges("random", should_continue, {"loop": "random", "exit": END})

app = graph.compile()
response = app.invoke({"name": "bob"})
print(response)
