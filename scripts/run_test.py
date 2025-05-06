"""Entry point script to discover and run all unittests in the current directory."""

import unittest
from pathlib import Path
import sys
from os import rmdir


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import settings
    settings.EXPORT_DIR = Path(__file__).resolve().parent / "export_test/"
    import run

    run.init_run()

    loader = unittest.TestLoader()
    suite = loader.discover(Path(__file__).resolve().parent)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    rmdir(settings.EXPORT_DIR)
