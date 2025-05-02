"""
Module entry point for doc_generation package test suite.

Exposes test case classes for import and discovery by test runners.
"""

from .document import DocumentTests
from .project_info import ProjectInfoTests

__all__ = [
    'DocumentTests',
    'ProjectInfoTests'
]
