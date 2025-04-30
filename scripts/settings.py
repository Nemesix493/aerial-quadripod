
"""
This module define the globals settings for the scripts
"""

from pathlib import Path

# project directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# cad files directory path
CAD_FILES_DIR = BASE_DIR / "cad"

TEMPLATES_DIR = BASE_DIR / "scripts" / "templates"

EXPORT_DIR = BASE_DIR / "exports"
