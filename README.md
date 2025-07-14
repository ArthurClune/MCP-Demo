# Model-Context-Protocol (MCP) Server

The simplest and dumbest possible MCP server, written to understand this stuff

This repo only exists to support the blog post https://clune.org/posts/explaining-model-context-protocol/

## Features

- Provides a single function `ls` that runs the shell command `ls <path>` and returns the result as a string

## Installation in Claude Desktop
```
mcp install src/mcp_server.py
```

This will add condig to `~/Library/Application Support/Claude/claude_desktop_config.json` like
```
{
  "mcpServers": {
    "Code Directory Lister": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/arthur/code/MCP/test_example/src/mcp_server.py"
      ]
    }
  }
}
```

Once installed, test in Claude desktop by e.g. "Show me the files in /Users"

## Tests

The tests are  pretty made up
```
uv run python -m unittest discover -s tests
```

## Type Checking

This project uses pyrefly for type checking. To run type checks:

```
uv run pyrefly check
```

The codebase follows PEP 8 typing standards and should show 0 errors when properly typed.
