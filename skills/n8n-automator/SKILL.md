---
name: n8n-automator
description: A hybrid skill for managing n8n workflows using both MCP (for inspection) and REST API (for creation/editing).
---

# n8n Automator Skill

This skill enables "Unicorn-Tier" automation of your n8n instance.

## Architecture

- **Right Brain (MCP):** Connects via `supergateway` to "read" your n8n instance, discover tools, and understand available nodes.
- **Left Brain (REST API):** Connects via standard HTTP requests to create, update, and delete workflows, covering the gap in the current MCP implementation.

## Setup

1. **MCP**: Ensure the `n8n-mcp` server is configured in your IDE settings.
2. **API**: Store your `N8N_API_KEY` in the `.env` file of this skill or securely in your environment.

## Capabilities

- `audit_workflow`: Inspect a workflow and add documentation/sticky notes.
- `generate_workflow`: Create a new workflow from a text description and push it to the server.
- `trigger_workflow`: Execute a workflow via Webhook or ID.

## Usage

Refer to `scripts/n8n_manager.py` (to be created) for the execution logic.
