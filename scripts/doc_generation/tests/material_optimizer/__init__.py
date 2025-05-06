"""
Module entry point for doc_generation.material_optimizer test suite.

Exposes test case classes for import and discovery by test runners.
"""

from .length_optimizer import LengthOptimizerTests
from .base_material_optimizer import BaseMaterialOptimizerTests

__all__ = [
    'LengthOptimizerTests',
    'BaseMaterialOptimizerTests'
]
