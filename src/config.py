import os

from dotenv import load_dotenv


load_dotenv()


BBL_LLM_BASE_URL = os.environ["BBL_LLM_BASE_URL"]
BBL_LLM_API_KEY = os.environ["BBL_LLM_API_KEY"]
BBL_LLM_MODEL = os.environ["BBL_LLM_MODEL"]