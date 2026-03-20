import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient  
from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_google_credentials,
)


def get_azure_docs_tools():
    async def _fetch():
        client = MultiServerMCPClient(
            {
                "livescore": {
                    "transport": "http",  
                    "url": "https://learn.microsoft.com/api/mcp",
                },

            }
        )

        tools = await client.get_tools()
        return tools
    return asyncio.run(_fetch())


def get_gmail_tools():
    toolkit = GmailToolkit()

    # credentials = get_google_credentials(
    # token_file="token.json",
    # scopes=["https://mail.google.com/"],
    # client_secrets_file="credentials.json",
    # )

    # api_resource = build_resource_service(credentials=credentials)
    # toolkit = GmailToolkit(api_resource=api_resource)

    tools = toolkit.get_tools()
    return tools


if __name__ == "__main__":
    print(get_gmail_tools())
