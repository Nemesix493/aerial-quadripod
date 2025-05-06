"""Unit tests for the BOM generation module."""

from os import remove

from cerberus import Validator

from doc_generation.bom_generation import BOMDocument, run
from doc_generation import MaterialOptimizer, ProjectInfo
from .require_project_info import RequireProjectInfoTestCase


class BOMDocumentTest(RequireProjectInfoTestCase):
    """Test case for the BOMDocument class and its context generation."""

    context_schema = {
        'materials': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'quantity': {'type': 'integer', 'required': True},
                    'unit': {'type': 'string', 'required': True},
                    'parts': {'type': 'string', 'required': True},
                    **ProjectInfo.material_schema
                }
            }
        },
        'date': {
            'type': 'string',
            'required': True
        }
    }

    context_validator = Validator(context_schema)

    def test_get_context(self):
        """Test that BOMDocument returns a context matching the defined schema."""
        bom_document = BOMDocument(MaterialOptimizer.get_all())
        self.assertTrue(
            self.context_validator.validate(
                bom_document.get_context()
            ),
            self.context_validator.errors
        )


class RunBOMGenerationTest(RequireProjectInfoTestCase):
    """Test case for the `run` function in the BOM generation module."""

    def test_run(self):
        """Test that running the BOM generation returns a BOMDocument instance."""
        bom_document = run(MaterialOptimizer.get_all())
        self.assertIsInstance(
            bom_document,
            BOMDocument
        )
        remove(bom_document.pdf_path)
