---
name: google-stitch
description: Remote MCP server for Google Stitch (AI-driven UI design).
---

# Stitch via MCP

**Connect IDEs and CLIs to Stitch using the Model Context Protocol.**

The Stitch Model Context Protocol (MCP) server allows your favorite AI tools like Cursor, Antigravity, or the Gemini CLI to directly interact with your Stitch projects.

## Understanding Remote MCP

Most MCP servers you use are Local. They read files on your hard drive or run scripts on your machine. Stitch is a Remote MCP server. It lives in the cloud.

Because it is remote, it requires a secure “handshake” to ensure that the AI agent acting on your behalf actually has permission to modify your designs.

## API Keys vs OAuth

The Stitch MCP server supports two authentication methods:

1. **API Keys**: Persistent keys generated in the Stitch Settings page.
2. **OAuth**: A browser-based authentication flow required by specific AI clients that do not support manual key entry, or for environments where storing persistent secrets on disk is restricted.

### When to use which

In most cases, **API Keys are the easiest approach**. They are the fastest way to get your tool connected. However, OAuth is worth the extra minute of setup in specific situations.

| Scenario           | Use API Keys if…                                                                                                              | Use OAuth if…                                                                                                                              |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **Client Support** | Your tool (e.g., Cursor, Antigravity, or the Gemini CLI) accepts an API key in a config file or environment variable.         | Your tool (e.g., web-based tools) requires a “Sign In” flow and doesn’t provide a way to manually input a key.                             |
| **Storage Policy** | You are on a private machine where saving a secret key in a local `.json` or `.env` file is standard practice.                | You are in a “Zero-Trust” or ephemeral environment where saving persistent secrets to the hard drive is blocked or risky.                  |
| **Revocation**     | You are comfortable manually deleting a key from the Stitch Settings page and then finding/removing it from your local files. | You want the ability to “Log Out” and instantly invalidate the tool’s access via the Stitch Settings page without hunting for local files. |
| **Session Logic**  | You want a connection that stays active indefinitely until you manually change it.                                            | You prefer a session-based connection that can be set to expire or require a re-approval after a period of inactivity.                     |

## 1. API Key Setup

1. Go to your **Stitch Settings** page.
2. Scroll to the **API Keys** section.
3. Click on **“Create API Key”** to generate a new API key.
4. Copy the API key and save it in a secure location.

> **Warning**: Never store your API key in a place where it can be exposed to the public. Never commit your API key to a public repository.

## 2. MCP Client Setup

### Antigravity / Gemini Code Assist

In the Agent Panel, click the three dots in the top right and select **MCP Servers**. Click **Manage MCP Servers**. Select **“View raw config”** and add the following entry:

```json
{
  "mcpServers": {
    "stitch": {
      "serverUrl": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "YOUR-API-KEY"
      }
    }
  }
}
```

### Gemini CLI

Install the Stitch extension for the Gemini CLI.

```bash
gemini extensions install https://github.com/gemini-cli-extensions/stitch
```

### Cursor

Create a `.cursor/mcp.json` file with the following entry:

```json
{
  "mcpServers": {
    "stitch": {
      "url": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "YOUR-API-KEY"
      }
    }
  }
}
```

### VSCode

1. Open the Command Palette (`Cmd+Shift+P`) and type “MCP: Add Server”.
2. Select “Add MCP Server”. Select HTTP to add a remote MCP server.
3. Enter the Stich MCP URL: `https://stitch.googleapis.com/mcp`.
4. Set the name to “stitch” and confirm.
5. Build the `mcp.json` file to add the API key:

```json
{
  "servers": {
    "stitch": {
      "url": "https://stitch.googleapis.com/mcp",
      "type": "http",
      "headers": {
        "Accept": "application/json",
        "X-Goog-Api-Key": "YOUR-API-KEY"
      }
    }
  }
}
```

### Claude Code

Use the `claude mcp` command to authenticate and add the following entry:

```bash
claude mcp add stitch --transport http https://stitch.googleapis.com/mcp --header "X-Goog-Api-Key: api-key" -s user
```

## 3. OAuth Setup (Alternative)

We need to generate two secrets to allow your MCP Client to talk to Stitch:

- **Project ID**: The container for your work.
- **Access Token**: The short lived key for to verify authentication for the project.

### Step 1: Install the Google Cloud SDK

Stitch relies on the `gcloud` CLI for secure authentication.

```bash
# MacOS via Homebrew
brew install --cask google-cloud-sdk
```

### Step 2: Double-Layer Authentication

You need to log in twice. Once as You (the user), and once as the Application (your local code/MCP client).

```bash
# 1. User Login (Opens Browser)
gcloud auth login

# 2. Application Default Credentials (ADC) Login
# This allows the MCP server to "impersonate" you securely.
gcloud auth application-default login
```

### Step 3: Configure the Project & Permissions

Select your working project and enable the Stitch API. You must also grant your user permission to consume services.

```bash
# Replace [YOUR_PROJECT_ID] with your actual Google Cloud Project ID
PROJECT_ID="[YOUR_PROJECT_ID]"

gcloud config set project "$PROJECT_ID"

# Enable the Stitch API
gcloud beta services mcp enable stitch.googleapis.com --project="$PROJECT_ID"

# Grant Service Usage Consumer role
USER_EMAIL=$(gcloud config get-value account)
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="user:$USER_EMAIL" \
    --role="roles/serviceusage.serviceUsageConsumer" \
    --condition=None
```

### Step 4: Generate the Secrets (.env)

Finally, we generate the Access Token and save it to a `.env` file.

```bash
# Print the token
TOKEN=$(gcloud auth application-default print-access-token)

# Note: This overwrites any existing .env file
echo "GOOGLE_CLOUD_PROJECT=$PROJECT_ID" > .env
echo "STITCH_ACCESS_TOKEN=$TOKEN" >> .env

echo "Secrets generated in .env"
```

> **Note**: Access Tokens are temporary (usually lasting 1 hour). When your MCP client stops responding or says “Unauthenticated,” you need to refresh the token.

## Available Tools

Once authenticated, your AI assistant will have access to the following tools to manage your Stitch workflow.

### Project Management

- **create_project**: Creates a new container for your UI work.
- **list_projects**: Retrieves a list of all your active designs.

### Screen Management

- **list_screens**: Fetches all screens within a specific project.
- **get_project**: Retrieves specific details for a single project.
- **get_screen**: Retrieves specific details for a single screen.

### Make new design

- **generate_screen_from_text**: Creates a new design from text prompt.
