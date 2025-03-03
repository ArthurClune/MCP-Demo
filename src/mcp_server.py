#!/usr/bin/env python3
# Copyright 2025 Arthur Clune arthur@clune.org
#
# Licensed under the MIT License

import subprocess
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Code Directory Lister")

@mcp.tool()
def ls(path: str) -> str:
    """List files in the specified directory"""
    result = subprocess.run(
        ["ls", path],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()
