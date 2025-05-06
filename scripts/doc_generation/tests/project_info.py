"""Unit tests for the ProjectInfo class used in project metadata validation and loading."""

from unittest import TestCase
from pathlib import Path
from os import remove

import pyaml

from doc_generation.project_info import ProjectInfo


class ProjectInfoTests(TestCase):
    """Test suite for validating the behavior of the ProjectInfo class."""

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
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test file after all tests have run."""
        remove(cls.info_file_test)
        return super().tearDownClass()

    def write_info_file(self, obj):
        """Write YAML object to the temporary test info file."""
        with open(self.info_file_test, "w", encoding="utf-8") as info_file_test:
            pyaml.dump(obj, info_file_test)

    def test_load(self):
        """Test successful loading and parsing of the info file."""
        self.write_info_file(self.info_file_content)
        ProjectInfo.load()
        self.assertEqual(
            self.info_file_content,
            getattr(ProjectInfo, "_info")
        )
        delattr(ProjectInfo, "_info")

    def test_load_error(self):
        """Test that missing top-level keys cause validation to fail."""
        for key in self.info_file_content:
            invalid_info_file = self.info_file_content.copy()
            invalid_info_file.pop(key)
            self.write_info_file(invalid_info_file)
            self.assertRaises(
                ProjectInfo.ValidationError,
                ProjectInfo.load
            )
