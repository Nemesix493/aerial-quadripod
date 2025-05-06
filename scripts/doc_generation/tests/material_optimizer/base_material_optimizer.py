"""Unit tests for the base material optimizer class."""

from doc_generation.material_optimizer import MaterialOptimizer
from ..require_project_info import RequireProjectInfoTestCase


class BaseMaterialOptimizerTests(RequireProjectInfoTestCase):
    """Test case for validating the material optimizer base behavior."""

    def test_get_all(self):
        """Test that all materials are correctly loaded and associated with optimizers."""
        material_optimizers = MaterialOptimizer.get_all()
        self.assertEqual(
            len(material_optimizers),
            len(self.info_file_content['materials'])
        )
        for material_optimizer in material_optimizers:
            self.assertIsInstance(
                material_optimizer,
                MaterialOptimizer
            )
