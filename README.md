# Build Agentic Tools with Google ADK

**Learn by doing: a small, runnable tutor agent to get you from zero to “I built an AI agent” with the Google Agent Development Kit (ADK).**

---

## What We’re Doing Here

This repo is a **hands-on learning project** for developers who want to:

- **Build agentic tools** — agents that can reason, use tools, and talk to users.
- **Use Google ADK** — the Agent Development Kit for designing and running agents.
- **Start simple** — one tutor agent, one flow, no fluff. Then extend from there.

**Objective:** Get you comfortable with ADK basics (agents, models, prompts, CLI, web UI) so you can add tools, sub-agents, and custom logic with confidence.

---

## The Basics

- **Agent** — A program that uses an LLM to have a conversation, optionally call tools, and (in ADK) can delegate to other agents.
- **Google ADK** — A framework to define agents (model + instruction + tools/sub-agents), run them in the terminal or via a web app, and plug in different LLM backends (e.g. via LiteLLM).
- **This project** — One **tutor agent** wired to LiteLLM (e.g. Ollama). You chat with it in the CLI or in the browser; it explains topics in a clear, step-by-step way. No tools in this minimal version — pure Q&A to keep the “first agent” experience simple.

---

## Tech Stack & Minimum Requirements

| What | Choice in this repo |
|------|----------------------|
| **Framework** | [Google ADK](https://google.github.io/adk-docs/) (Python) |
| **LLM gateway** | [LiteLLM](https://docs.litellm.ai/) (via `google-adk[extensions]`) |
| **Default model** | [Ollama](https://ollama.com/) (e.g. `llama3.1`) — run models locally |
| **Language** | Python 3.12+ |
| **Package manager** | Poetry |

**You need:**

- **Python 3.12+**
- **Poetry** (or use the project’s `pyproject.toml` with `pip` if you prefer)
- **Ollama** (optional but recommended) — install from [ollama.com](https://ollama.com), then e.g. `ollama pull llama3.1`
- A **terminal** and a **browser** for CLI and `adk web`

---

## How to Get Started

### 1. Clone and enter the repo

```bash
git clone https://github.com/austinnoronha/agentic_learning_with_google_adk.git
cd agentic_learning_with_google_adk
```

### 2. Install dependencies

```bash
poetry install
```

### 3. Environment (optional)

Create a `.env` in the project root if you want to override the default model or API base:

```env
# Optional: default is ollama/llama3.1
LITELLM_MODEL=ollama/llama3.1
OLLAMA_API_BASE=http://localhost:11434

# To use this this start ollama eith CMD : ollama serve
```

### 4. Run the agent

**Terminal (CLI):**

```bash
poetry run adk run development_tutor
```

**Web UI:**

```bash
poetry run adk web
```

Then open **http://localhost:8000**, select the `development_tutor` agent, and chat in the browser.

---

## Sample: The Tutor Agent

This repo ships one agent: **`development_tutor`** (named `dev_assistant` in the app). It’s a minimal “tutor” that explains topics step by step — no tools, no sub-agents, just the LLM and a clear system prompt.

**Layout:**

```
development_tutor/
├── agent.py          # Defines the agent (LiteLLM + instruction, no tools)
├── prompt.py         # System instruction: “you are a patient tutor…”
└── shared_libraries/
    └── constants.py  # Agent name, model string, API base (from env)
```

**What it does:**

- **agent.py** — Builds a `LlmAgent` with a LiteLLM model (from `constants`) and a single instruction from `prompt.py`. No `tools=` in this starter.
- **prompt.py** — Tells the model to act as a tutor: explain step by step, use simple language, give examples, and stay on topic.
- **constants.py** — Reads `LITELLM_MODEL` and `OLLAMA_API_BASE` from the environment so you can point at different models or backends without changing code.

This is the “sample tool” in the sense of **one runnable agent** you can extend (e.g. add a `web_search` tool, or a sub-agent) once you’re comfortable with the basics.

---

## Using the CLI and ADK Web

### CLI: `adk run`

From the **project root**:

```bash
poetry run adk run development_tutor
```

- Starts an interactive chat in the terminal.
- Type your message and press Enter; the tutor replies. Type `exit` to quit.
- All traffic goes through ADK → LiteLLM → your configured model (e.g. Ollama).

### Web UI: `adk web`

From the **project root**:

```bash
poetry run adk web
```

- Starts a local server (default **http://localhost:8000**).
- Open that URL, pick the **development_tutor** agent, and chat in the browser.
- Same agent as the CLI, different interface.

Use both to get a feel for how ADK runs your agent in different environments.

---

## Vision

- **Short term:** Keep this repo as a minimal, well-documented “first agent” with ADK: one tutor, one flow, easy to read and run. Add a first tool (e.g. web search) or a first sub-agent as a next step.
- **Medium term:** Use it as a playground for agentic patterns: tools, sub-agents, routing, and better prompts — always with ADK + LiteLLM so you can swap models and providers easily.
- **Long term:** Reuse the patterns (and optionally the code) in real products: support bots, internal assistants, or learning tools — all built on the same “agent + instruction + optional tools” idea you learn here.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for the full text. You’re free to use, modify, and distribute it for learning and building.

---

**Have fun building agents.**
