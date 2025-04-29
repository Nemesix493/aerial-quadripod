"""Entry point script to discover and run all unittests in the current directory."""

import unittest
from pathlib import Path


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(Path(__file__).resolve().parent)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
