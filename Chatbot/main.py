import os
from typing import TypedDict, List, Union
from langchain.messages import HumanMessage, AIMessage
from langchain.agents import create_agent
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


agent = create_agent(model="google_genai:gemini-3.1-flash-lite")


def process(state: AgentState) -> AgentState:
    """This node will send the request the user inputs to a model"""
    response = agent.invoke({"messages": state["messages"]})
    print(response["messages"][-1].content[0]["text"])
    state["messages"].append(response["messages"][-1])

    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
app = graph.compile()

conversation_history = []

with open("logging.txt", "r") as file:
    for line in file:
        result = line.split(":", 1)
        if result[0] == "You":
            conversation_history.append(HumanMessage(content=result[1]))
        elif result[0] == "AI":
            conversation_history.append(AIMessage(content=result[1]))
    print("Finished reading convo history")


user_input = input("Enter prompt: ")

while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    response = app.invoke({"messages": conversation_history})
    conversation_history = response["messages"]
    user_input = input("Enter prompt: ")

with open("logging.txt", "w") as file:
    file.write("Conversaton History:\n")

    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    file.write("End of conversation")

print("Conversation saved to logging.txt")
