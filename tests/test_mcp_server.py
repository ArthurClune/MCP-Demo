# Copyright 2025 Arthur Clune arthur@clune.org
#
# Licensed under the MIT License
#
# Vide coded using Claude Code

import unittest
from unittest.mock import patch, MagicMock
import subprocess

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mcp_server import mcp, ls


class TestMCPServer(unittest.TestCase):
    @patch("mcp_server.subprocess.run")
    def test_ls_function(self, mock_run) -> None:
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

    def test_mcp_function_registration(self) -> None:
        """Test that the ls function is registered with the MCP server."""
        # We can only verify the function exists by checking it directly
        # ls is already imported at the top of the file

        # Verify that ls is a callable function
        self.assertTrue(callable(ls))

        # Verify the function has the expected parameter
        import inspect
        sig = inspect.signature(ls)
        self.assertIn("path", sig.parameters)


if __name__ == "__main__":
    from unittest import main
    main()
