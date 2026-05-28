from typing import TypedDict, List
import math
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    values: List[int]
    operator: str
    result: str


def apply_operator(state: AgentState) -> AgentState:
    if state["operator"] == "+":
        state["result"] = f"Hey {state['name']}, your answer is: {sum(state['values'])}"
    elif state["operator"] == "*":
        state["result"] = (
            f"Hey {state['name']}, your answer is: {math.prod(state['values'])}"
        )
    else:
        state["result"] = f"Hey {state['name']} I don't recognize that operator"
    return state


graph = StateGraph(AgentState)
graph.add_node("operator", apply_operator)
graph.set_entry_point("operator")
graph.set_finish_point("operator")

app = graph.compile()
response = app.invoke({"name": "Bob", "values": [1, 2, 3, 4], "operator": "*"})

print(response["result"])
