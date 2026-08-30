from agents import Agent, RunHooks

from src.agents.data_retriever import data_retriever
from src.model import model

class DebugHooks(RunHooks):
    async def on_agent_start(self, context, agent):
        print(f"\n[AGENT START] {agent.name}")

    async def on_agent_end(self, context, agent, output):
        print(f"[AGENT END] {agent.name}")
        print(f"[OUTPUT] {output}")

    async def on_tool_start(self, context, agent, tool):
        print(f"\n[TOOL START] {tool.name}")

        if hasattr(context, "tool_arguments"):
            print(f"[TOOL INPUT] {context.tool_arguments}")

    async def on_tool_end(self, context, agent, tool, result):
        print(f"[TOOL END] {tool.name}")
        print(f"[TOOL OUTPUT] {result}")


debug_hooks = DebugHooks()

report_generator = Agent(
    name="Report Generator",
    instructions="""
You are an expert report writer.

Always use the Data Retriever before answering.

Answer only using facts explicitly stated in the retrieved snippets.

Do not infer relationships between separate policies unless the
retrieved information explicitly states that relationship.

Ignore retrieved snippets that are not relevant to the user's question.

Do not add recommendations, assumptions, or follow-up offers.

Produce a clear, accurate, concise, and non-redundant answer.
    """,
    model=model,
    tools=[
        data_retriever.as_tool(
            tool_name="retrieve_knowledge",
            tool_description=(
                "Retrieve relevant raw snippets "
                "from the local knowledge base."
            ),
             hooks=debug_hooks,
        )
    ],
)

