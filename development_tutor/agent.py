"""Tutor agent: LiteLLM only, Q&A with no tools."""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AGENT_DIR = Path(__file__).resolve().parent
for p in (PROJECT_ROOT, AGENT_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from prompt import INSTRUCTION
from shared_libraries.constants import AGENT_NAME, API_BASE, DESCRIPTION, MODEL

model = LiteLlm(model=MODEL, api_base=API_BASE)
root_agent = LlmAgent(
    model=model,
    name=AGENT_NAME,
    description=DESCRIPTION,
    instruction=INSTRUCTION,
)
