import asyncio

from agents import Runner

from src.agents.data_retriever import data_retriever


async def main():
    query = "Can employees go abroad for work?"

    result = await Runner.run(
        data_retriever,
        query,
    )

    print("\n--- Data Retriever Output ---")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())