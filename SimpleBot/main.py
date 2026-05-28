from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[HumanMessage]


# Create the agent here or use init chat bot, I'll figure it out as I get thru the
# the tutorial (since he uses openai and I want to use something free)
# Since he uses invoke I'll need to use create agent

agent = create_agent(
    model="google_genai:gemini-3.5-flash",
)


def process(state: AgentState) -> AgentState:
    response = agent.invoke({"messages": state["messages"]})
    print(f"\nAI response: {response['messages'][-1].content[0]['text']}")
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

app = graph.compile()

user_input = input("Enter a prompt: ")
while user_input != "exit":
    app.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter a prompt: ")
