import asyncio

from agents import Agent, Runner

from  src.model import model


agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant. Answer briefly.",
    model=model,
)


async def main():
    result = await Runner.run(
        agent,
        "What is Retrieval-Augmented Generation?",
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())