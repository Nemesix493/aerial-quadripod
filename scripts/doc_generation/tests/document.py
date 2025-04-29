"""Unit tests for the abstract Document class and its concrete implementations."""

from unittest import TestCase
from pathlib import Path
from os import remove

from jinja2 import Template

from doc_generation.document import Document


class DocumentTests(TestCase):
    """Test suite for the Document abstract base class."""

    @classmethod
    def get_document_subclass(cls):
        """Return a simple concrete implementation of Document for testing purposes."""

        class DocumentTestClass(Document):
            """Concrete subclass of Document for testing rendering and saving."""

            export_path = Path(__file__).resolve().parent
            export_name = "test_document"

            def get_context(self):
                """Provide context data for template rendering."""
                return {"title": "title_test"}

            def get_template(self):
                """Return an inline Jinja2 template for rendering."""
                return Template(
                    '<!DOCTYPE html>\n<html lang="en">\n'
                    '<head>\n    '
                    '<meta charset="UTF-8">\n    <title>{{ title }}</title>\n'
                    '</head>\n<body>\n'
                    '    <h1 style="color: navy;">{{ title }}</h1>\n'
                    '</body>\n</html>'
                )

        return DocumentTestClass

    @classmethod
    def setUpClass(cls):
        """Setup the test document instance."""
        cls.document_subclass = cls.get_document_subclass()
        cls.document_instance = cls.document_subclass()
        return super().setUpClass()

    def test_template_render(self):
        """Test if the template renders correctly with the provided context."""
        self.assertEqual(
            self.document_instance.html,
            '<!DOCTYPE html>\n<html lang="en">\n'
            '<head>\n    '
            '<meta charset="UTF-8">\n    <title>title_test</title>\n'
            '</head>\n<body>\n'
            '    <h1 style="color: navy;">title_test</h1>\n'
            '</body>\n</html>'
        )

    def test_save_as_html(self):
        """Test if the HTML file is generated and saved correctly."""
        self.document_instance.save_as_html()
        self.assertTrue(
            self.document_instance.html_path.exists()
        )
        remove(self.document_instance.html_path)

    def test_save_as_pdf(self):
        """Test if the PDF file is generated and saved correctly."""
        self.document_instance.save_as_pdf()
        self.assertTrue(
            self.document_instance.pdf_path.exists()
        )
        remove(self.document_instance.pdf_path)

    def test_paths_errors(self):
        """Test error cases when export path or name are invalid."""

        # Invalid export_path
        document_subclass_error = self.get_document_subclass()
        document_subclass_error.export_path = "invalid_path"
        self.assertRaises(
            TypeError,
            lambda: document_subclass_error().html_path
        )
        self.assertRaises(
            TypeError,
            lambda: document_subclass_error().pdf_path
        )

        # Invalid export_name
        document_subclass_error = self.get_document_subclass()
        document_subclass_error.export_name = None
        self.assertRaises(
            TypeError,
            lambda: document_subclass_error().html_path
        )
        self.assertRaises(
            TypeError,
            lambda: document_subclass_error().pdf_path
        )
