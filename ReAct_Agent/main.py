from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, START, END
from langchain.agents import create_agent
from langchain_core.messages import BaseMessage
from langchain.messages import ToolMessage, SystemMessage
from langchain.tools import tool
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tool_node
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    # So using BaseMessage to indicate we can have any type
    # of message (like HumanMessage, SystemMessage, etc)
    # Then we use Sequence as the type annotation so that
    # we don't have to worry about updates. Lastly, we
    # use annotation to add "add_messages" as the metadata,
    # which is our reducer function


@tool
def add(a: int, b: int):
    """This is an addition function that adds two numbers together"""
    return a + b


tools = [add]
agent = create_agent(model="google_genai:gemini-3.1-flash-lite", tools=tools)


def model_call(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(
        content="You are my AI assistant, please answer my query to the best of your ability."
    )
    response = agent.invoke([system_prompt] + state["messages"])
    # You could do this:
    # state["messages"] = response
    # return state

    # But this is faster
    return {"messages": [response]}


def should_continue(state: AgentState) -> AgentState:
    messages = state["messages"]
    last_message = messages[-1]

    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"


graph = StateGraph(AgentState)
graph.add_node("agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("tools")

graph.add_conditional_edges("agent", should_continue, {
    "end": "f
})
