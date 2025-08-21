# Gitrules
<p align="center">
  <img width="672" height="602" alt="image" src="https://github.com/user-attachments/assets/7ed8b1c3-b602-4dfd-aba3-01cc9c3b799b" />
</p>

**Pastable superpowers for your codebases.**  
Build context files (agents, rules, MCP configs, etc.) for AI coding tools. Compose them in a browser workspace, then generate a single _install-in-one-click_ script that recreates the files inside any repo.

---

## ✨ What it does

We’re basically your **context manager** 🗂️ — helping you **create, modify, and improve your coding context** for AI coding agents through simple files. Drop in rules, agents, or MCP configs and watch your agents level up ⚡.

- 🖥️ **Visual workspace**: File tree + Monaco editor + quick actions, persisted in `localStorage`.
- 🔄 **Instant sharing**: Every change turns into a fresh one-click install script (short hash included).
- 🤖 **Plug-and-play add-ons**:
  - **Agents** from `app/actions/agents/*.md`
  - **Rules** from `app/actions/rules/*.md`
  - **MCPs** from `app/actions/mcps.json` → toggled into `.mcp.json`
- 🎨 **Zero-setup UI**: Jinja + Tailwind + Vanilla JS; no fragile build step.

---

## 🧰 Tech Stack

- **Backend**: FastAPI, Jinja2
- **Frontend**: Tailwind, Vanilla JS, Monaco editor (CDN)
- **Runtime**: Uvicorn (dev)
- **Config**: `.env` via `python-dotenv`
- **Analytics (optional)**: `api-analytics` middleware

---

## 🚀 Quick Start (Local)

> This project uses **uv** for package management.

1) **Install**
~~~bash
uv pip install -r requirements.txt
~~~


2) **Run the dev server**
~~~bash
uvicorn app.main:app --reload
~~~
Open http://localhost:8000

---

## 🧪 Using the App

1) **Open the site** → Use **Quick start** buttons to add Agents / Rules / MCPs.  
2) **Workspace** → Files appear in the left tree; edit in the center editor.  
3) **One-click install** → Top-right shows a shell command, for example:
~~~bash
sh -c "$(curl -fsSL http://localhost:8000/api/install/<HASH>.sh)"
~~~
It creates folders, writes files, and lists any required **environment variables** it detected.

> 🔐 **Security tip**: As with any `curl | sh`, inspect the script first:
> `curl -fsSL http://localhost:8000/api/install/<HASH>.sh`

---

## ➕ Add Your Own

- **Agent**: drop `my-agent.md` into `app/actions/agents/`  
  The UI label is derived from the filename (kebab → Title Case).

- **Rule**: drop `my-rule.md` into `app/actions/rules/`

- **MCP preset**: edit `app/actions/mcps.json`  
  The installer toggles entries into `.mcp.json` and surfaces any `${ENV_VAR}` strings it finds.


---

## 🙏 Credits

Using prompts from:  
https://github.com/centminmod/my-claude-code-setup

---
