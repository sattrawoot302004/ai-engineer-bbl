import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ["BBL_LLM_API_KEY"]
base_url = os.environ["BBL_LLM_BASE_URL"]
model = os.environ["BBL_LLM_MODEL"]

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
    default_headers={
        "api-key": api_key,
    },
)

response = client.responses.create(
    model=model,
    input="Write a one-sentence bedtime story about a unicorn.",
)

print(response.output_text)