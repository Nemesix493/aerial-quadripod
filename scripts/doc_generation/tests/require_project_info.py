"""Unit test setup for components requiring validated project info.

This module provides a base test case that prepares a temporary
YAML project info file and cleans it up after tests.
"""

from unittest import TestCase
from pathlib import Path
from os import remove

import pyaml

from doc_generation.project_info import ProjectInfo
import settings


class RequireProjectInfoTestCase(TestCase):
    """Base test case to initialize and clean up a temporary project info file for tests."""

    info_file_content = {
        "materials": [
            {
                "id": "material_test",
                "dim": [6000],
                "url": "https://test.material.com/",
                "ref": "ref_test",
            }
        ],
        "construct-info": {
            "cut_line_thickness": 3,
            "cut_line_tolerance": 7
        },
        "parts": [
            {
                "name": "test_name",
                "quantity": 10,
                "material_id": "material_test",
                "max_length": 200
            }
        ]
    }

    @classmethod
    def setUpClass(cls):
        """Prepare test file path and assign it to the class before tests run."""
        cls.info_file_test = Path(__file__).resolve().parent / "test_info_file.yml"
        ProjectInfo.INFO_FILE_PATH = cls.info_file_test
        cls.write_info_file(cls.info_file_content)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test file after all tests have run."""
        remove(cls.info_file_test)
        ProjectInfo.INFO_FILE_PATH = settings.INFO_FILE
        return super().tearDownClass()

    @classmethod
    def write_info_file(cls, obj):
        """Write YAML object to the temporary test info file."""
        with open(cls.info_file_test, "w", encoding="utf-8") as info_file_test:
            pyaml.dump(obj, info_file_test)
