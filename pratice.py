from langchain_openai import ChatOpenAI
from browser_use import Agent  # Assuming this is a custom module you’ve defined
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Ensure your OpenRouter API key is in the .env file as OPENROUTER_API_KEY
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def main():
    agent = Agent(
        task="Extract customer reviews from the current Chrome tab",
        llm=ChatOpenAI(
            model="openai/gpt-4o",
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        ),
        browser_connection="http://localhost:9222",  # Hypothetical parameter
    )
    reviews = await agent.run()
    print("Extracted Reviews:")
    print(reviews)

if __name__ == "__main__":
    asyncio.run(main())