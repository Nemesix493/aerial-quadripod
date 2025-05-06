"""Unit tests for the base material optimizer class."""

from doc_generation.material_optimizer import LengthOptimizer
from ..require_project_info import RequireProjectInfoTestCase


class BaseMaterialOptimizerTests(RequireProjectInfoTestCase):
    """Test case for validating the material optimizer base behavior."""

    def test_get_all(self):
        """Test that all materials are correctly loaded and associated with optimizers."""
        length_optimizers = LengthOptimizer.get_all()
        self.assertEqual(
            len(length_optimizers),
            len(self.info_file_content['materials'])
        )
