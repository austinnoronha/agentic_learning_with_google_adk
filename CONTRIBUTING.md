# Contributing to Google ADK Learning

Thanks for your interest in contributing. This project is a **learning repo** for building agentic tools with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/). We especially welcome contributions that help others learn: **submit your tools, small agents, or examples** so the community can run them and extend them.

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Submitting Tools for Learning](#submitting-tools-for-learning)
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Tool and Agent Guidelines](#tool-and-agent-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)

---

## Ways to Contribute

- **Submit a tool** — Add a new ADK tool (e.g. a `FunctionTool`, or a small agent that uses a tool) so others can learn from it.
- **Submit a sample agent** — Add a minimal agent (under `development_tutor/` or a new folder) that showcases one pattern (e.g. one tool, one sub-agent).
- **Improve docs** — Fix or expand the README, CONTRIBUTING, or inline comments.
- **Fix bugs** — Report or fix issues in existing tools or the tutor agent.
- **Share ideas** — Open an issue to suggest a tool idea or a learning path.

We’d love **user-submitted tools for learning**: small, runnable examples that demonstrate how to build agentic behavior with Google ADK.

---

## Submitting Tools for Learning

If you want to contribute a **tool** or a **small agent** for others to learn from:

### 1. Decide where it lives

- **New tool only**  
  Add it under `development_tutor/tools/` (e.g. `development_tutor/tools/your_tool.py`). Use ADK’s `FunctionTool` (or another ADK tool type) and keep the tool self-contained and documented.

- **New agent that uses your tool**  
  You can either:
  - Add a new agent folder next to `development_tutor/` (e.g. `your_agent/agent.py` + `your_agent/tools/...`) and document how to run it with `adk run your_agent`, or  
  - Add your tool under `development_tutor/tools/` and optionally wire it into the existing tutor agent (or a new sub-agent) and document the change.

### 2. What to include

- **Code** — One or more files (tool, and optionally agent) that run with this repo’s setup (Python 3.12+, Poetry, ADK, LiteLLM as in `pyproject.toml`).
- **Docstring** — For your tool (and agent if applicable): what it does, parameters, and a one-line “learning intent” (e.g. “Example of a read-only API tool”).
- **README or comment** — Short “How to run” and “What this demonstrates” (e.g. in README or in a top-of-file comment). If you add a new agent folder, a short README there is ideal.

### 3. Keep it learnable

- Prefer **small, focused** tools and agents over large, multi-step flows.
- Use **clear names** (e.g. `weather_tool`, `fetch_docs_tool`) and simple function signatures.
- Avoid secrets or production credentials; use env vars or placeholders and document them.

Example of a minimal tool submission:

```python
# development_tutor/tools/example_tool.py
"""Example tool: fetch a greeting. For learning ADK FunctionTool."""
from google.adk.tools.function_tool import FunctionTool

def greeting(name: str) -> str:
    """Return a short greeting. (Learning: simple FunctionTool with one argument.)"""
    return f"Hello, {name}!"

greeting_tool = FunctionTool(greeting)
```

---

## Code of Conduct

- Be respectful and inclusive.
- Give constructive feedback.
- Keep examples and docs suitable for a learning audience.
- Communicate clearly.

---

## Getting Started

1. **Fork and clone** the repo (or clone directly if you have push access).
2. **Create a branch**: `git checkout -b feature/my-tool` or `tool/short-name`.
3. **Set up the project**:
   ```bash
   poetry install
   poetry run pre-commit install
   ```
4. **Run the existing agent** to confirm the repo works:
   ```bash
   poetry run adk run development_tutor
   ```
5. Add your tool (and optionally agent), then run tests and open a PR.

---

## Tool and Agent Guidelines

- **Use ADK APIs** — Build tools with `google.adk.tools.FunctionTool` (or other ADK tool types) and agents with `google.adk.agents.LlmAgent` so they work with `adk run` and `adk web`.
- **Prefer type hints** — Use type annotations on tool functions and important helpers.
- **No hardcoded secrets** — Use environment variables or clearly documented placeholders.
- **Optional tests** — Add a small test under `tests/` if your tool or agent is easy to unit test (e.g. loading the agent or calling the tool function). Not required for every submission but appreciated.

---

## Pull Request Process

1. **Branch** — Use a branch like `feature/my-tool` or `tool/description`.
2. **Scope** — One tool or one small agent (or one doc change) per PR when possible.
3. **Description** — In the PR, state:
   - What you added (e.g. “New tool: X” or “New sample agent: Y”).
   - How to run it (`adk run ...` or which script).
   - What learners will see (one or two sentences).
4. **Checks** — Ensure `poetry run pytest` passes and `poetry run pre-commit run --all-files` (or equivalent) is clean if the project uses pre-commit.

Maintainers will review for clarity, safety, and fit with the learning focus.

---

## Testing

- Run tests: `poetry run pytest`
- Run with coverage: `poetry run pytest --cov=development_tutor --cov-report=term-missing`
- If you add a new agent folder, you can add a test that imports its `root_agent` (similar to `tests/test_litellm_agent.py`) so we keep “agent loads” as a baseline.

---

Thank you for contributing. Your tools and examples help others learn how to build agentic tools with Google ADK.
