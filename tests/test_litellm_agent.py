# Quick test: load the tutor agent (no tools).
# Run from repo root: python test_litellm_agent.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from google.adk.models.lite_llm import LiteLlm

from development_tutor.agent import root_agent


def test_litellm_agent():
    assert root_agent is not None
    assert root_agent.name == "dev_assistant"
    assert root_agent.description == "Tutor agent for Q&A and explaining topics."
    # match part of the instruction
    assert "patient, clear tutor" in root_agent.instruction
    assert "explain topics" in root_agent.instruction
    assert "learner understands" in root_agent.instruction
    assert root_agent.tools == []
    # this return a LlmAgent object
    assert isinstance(root_agent.model, LiteLlm)
    assert root_agent.model.model == "ollama/llama3.1"
