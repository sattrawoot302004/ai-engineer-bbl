from openai import AsyncOpenAI

from agents import OpenAIResponsesModel, set_tracing_disabled

from src.config import (
    BBL_LLM_API_KEY,
    BBL_LLM_BASE_URL,
    BBL_LLM_MODEL,
)


client = AsyncOpenAI(
    api_key=BBL_LLM_API_KEY,
    base_url=BBL_LLM_BASE_URL,
    default_headers={
        "api-key": BBL_LLM_API_KEY,
    },
)


model = OpenAIResponsesModel(
    model=BBL_LLM_MODEL,
    openai_client=client,
)


set_tracing_disabled(True)