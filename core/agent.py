from langchain.agents import create_agent
from llm import model
from tools import get_azure_docs_tools, get_gmail_tools

tools = get_gmail_tools() + get_azure_docs_tools()

agent = create_agent(
    model,
    tools
)

events = agent.stream({"messages": [{"role": "user", "content": "What is Model Context Protocol?"}]}, stream_mode="values")
for event in events:
    event["messages"][-1].pretty_print()