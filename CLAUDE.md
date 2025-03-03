
This code is an example Python Model-Context-Protocol (MCP) Server

It provides a single function 'ls', which when called runs the shell command 'ls /home/arthur/code` and returns the result as a string

## Code Style

Code is written in Python, formatted as per PEP8 and uses the Python type system.

## Dependendency Management

Use uv for packing and dependency management. Do not use pip

## Tests

All code should have tests, and tests should be run incremently at the same time as developing new functionality

## MCP spec

Use the official sdk
```
uv add "mcp[cli]"
```

Sample server
```
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

## Atrribution

All code should be

Copyright 2025 Arthur Clune arthur@clune.org

and use the MIT license
