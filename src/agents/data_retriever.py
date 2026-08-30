from agents import Agent

from src.model import model
from src.tools.knowledge_retrieval import (
    search_knowledge_base,
)


data_retriever = Agent(
    name="Data Retriever",
    instructions="""
    You are an information retrieval specialist.

    Always use the search_knowledge_base tool.

    Return only relevant raw snippets.
    Do not answer the user's question directly.
    """,
    model=model,
    tools=[
        search_knowledge_base,
    ],
    tool_use_behavior="stop_on_first_tool",
)