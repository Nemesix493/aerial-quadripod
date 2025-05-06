"""
Module entry point for the doc_generation package.

Provides access to project information handling, material optimization,
and Bill of Materials (BOM) generation utilities.
"""

from .project_info import ProjectInfo
from .material_optimizer import MaterialOptimizer
from .bom_generation import run as run_bom_generation

__all__ = [
    'ProjectInfo',
    'run_bom_generation',
    'MaterialOptimizer'
]
