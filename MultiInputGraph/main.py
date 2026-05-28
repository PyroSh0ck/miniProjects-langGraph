from typing import TypedDict, List
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str


def handle_multiple_values(state: AgentState) -> AgentState:
    """This is a simple function for handling multiple values"""
    state["result"] = f"Hey there {state['name']}, your sum is {sum(state['values'])}!"
    return state


graph = StateGraph(AgentState)
graph.add_node("processor", handle_multiple_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")
app = graph.compile()
response = app.invoke({"values": [1, 2, 3, 4], "name": "Steven"})
print(response["result"])
