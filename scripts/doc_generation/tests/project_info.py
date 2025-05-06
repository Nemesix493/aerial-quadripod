"""Unit tests for the ProjectInfo class used in project metadata validation and loading."""

from doc_generation.project_info import ProjectInfo
from .require_project_info import RequireProjectInfoTestCase


class ProjectInfoTests(RequireProjectInfoTestCase):
    """Test suite for validating the behavior of the ProjectInfo class."""

    def test_load(self):
        """Test successful loading and parsing of the info file."""
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
        self.write_info_file(self.info_file_content)
