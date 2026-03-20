import os
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = AzureChatOpenAI(
    model="gpt-5.2-chat",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)
