import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain.agents import create_agent

async def main():
    client = MultiServerMCPClient(
        {
            "livescore": {
                "transport": "http",  
                "url": "https://learn.microsoft.com/api/mcp",
            },

        }
    )

    tools = await client.get_tools()

    agent = create_agent(
        "claude-sonnet-4-6",
        tools  
    )

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is MCP?"}]}
    )

    print(response)

if __name__ == "__main__":
    asyncio.run(main())
