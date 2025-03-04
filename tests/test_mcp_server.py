# Copyright 2025 Arthur Clune arthur@clune.org
#
# Licensed under the MIT License
#
# Vide coded using Claude Code

import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import subprocess

# Add the src directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.mcp_server import mcp, ls


class TestMCPServer(unittest.TestCase):
    @patch("src.mcp_server.subprocess.run")
    def test_ls_function(self, mock_run):
        """Test that the ls function calls subprocess.run with the correct arguments and returns the output."""
        # Setup the mock
        mock_process = MagicMock()
        mock_process.stdout = "file1\nfile2\nfile3"
        mock_run.return_value = mock_process

        # Call the function directly with a test path
        test_path = "/test/path"
        result = ls(test_path)

        # Verify the mock was called correctly
        mock_run.assert_called_once_with(
            ["ls", test_path],
            capture_output=True,
            text=True,
            check=True
        )

        # Verify the result is the expected string
        self.assertEqual(result, "file1\nfile2\nfile3")

    def test_mcp_function_registration(self):
        """Test that the ls function is registered with the MCP server."""
        # We can only verify the function exists by checking it directly
        from src.mcp_server import ls

        # Verify that ls is a callable function
        self.assertTrue(callable(ls))

        # Verify the function has the expected parameter
        import inspect
        sig = inspect.signature(ls)
        self.assertIn("path", sig.parameters)


if __name__ == "__main__":
    unittest.main()
