"""
Script to run the documentation generation process.

This script initializes the export directory (if needed) and executes
the Bill of Materials (BOM) generation using material optimizers
from the `doc_generation` package.
"""

from os import makedirs

import settings
import doc_generation


def init_run():
    """Create the export directory if it does not already exist."""
    if not settings.EXPORT_DIR.exists():
        makedirs(settings.EXPORT_DIR)


if __name__ == "__main__":
    init_run()
    material_optimizers = doc_generation.MaterialOptimizer.get_all()
    bom_document = doc_generation.run_bom_generation(material_optimizers)
