"""Unit tests for the LengthOptimizer class from the material optimizer module."""

from cerberus import Validator

from doc_generation.material_optimizer import LengthOptimizer
from ..require_project_info import RequireProjectInfoTestCase


class LengthOptimizerTests(RequireProjectInfoTestCase):
    """Test case for validating the behavior of LengthOptimizer."""

    stocks_schema = {
        'stocks': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'parts': {'type': 'list', 'required': True},
                    'remaining': {'type': 'integer', 'required': True}
                }
            }
        }
    }

    stocks_validator = Validator(stocks_schema)

    def test_length_optimizer(self):
        """Test that optimized cutting plans are generated and match the expected schema."""
        length_optimizers = LengthOptimizer.get_all()
        self.assertEqual(
            len(length_optimizers),
            1
        )
        for length_optimizer in length_optimizers:
            self.assertTrue(
                self.stocks_validator.validate(
                    {'stocks': length_optimizer.optimized_cutting_plans}
                )
            )
