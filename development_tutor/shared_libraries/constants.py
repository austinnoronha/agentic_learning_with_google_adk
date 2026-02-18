import os

from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "dev_assistant"
DESCRIPTION = "Tutor agent for Q&A and explaining topics."

# LiteLLM model string (e.g. ollama/llama3.1, ollama_chat/llama3.1). Must support tools.
MODEL = os.getenv("LITELLM_MODEL", "ollama/llama3.1")
API_BASE = os.getenv("OLLAMA_API_BASE", "http://localhost:11434")
