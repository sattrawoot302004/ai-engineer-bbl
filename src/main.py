import asyncio

from agents import Runner

from src.agents.report_generator import (
    report_generator,
)


async def main():
    query = input("Question: ")

    result = await Runner.run(
        report_generator,
        query,
    )

    print("\nAnswer:")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())