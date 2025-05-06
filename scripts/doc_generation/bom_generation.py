"""Module for generating a Bill of Materials (BOM) document."""

from datetime import date

from .material_optimizer import MaterialOptimizer
from .document import Document


class BOMDocument(Document):
    """Class responsible for generating the BOM document using material optimizers."""

    template = "BOM.html.j2"
    export_name = "BOM"

    def __init__(self, material_optimizers: list[MaterialOptimizer]):
        """Initialize the BOMDocument with a list of material optimizers.

        Args:
            material_optimizers (list[MaterialOptimizer]): List of optimizers for each material.
        """
        self.material_optimizers = material_optimizers

    def get_context(self):
        """Build the context data used to render the BOM template.

        Returns:
            dict: Context including materials information and current date.
        """
        return {
            'materials': [
                {
                    'quantity': len(material_optimizer.optimized_cutting_plans),
                    'unit': "x".join(
                        [
                            str(dim)
                            for dim in material_optimizer.material["dim"]
                        ]
                    ) + " mm",
                    'parts': ", ".join(
                        [
                            f"{part['name']} x {part['quantity']}"
                            for part in material_optimizer.parts
                        ]
                    ),
                    **material_optimizer.material
                }
                for material_optimizer in self.material_optimizers
            ],
            'date': date.today().strftime("%m/%d/%Y")
        }


def run(material_optimizers) -> BOMDocument:
    """Run the BOM generation process and save it as a PDF.

    Args:
        material_optimizers (list[MaterialOptimizer]): List of material optimizers to process.

    Returns:
        BOMDocument: The generated and saved BOM document.
    """
    bom_document = BOMDocument(material_optimizers)
    bom_document.save_as_pdf()
    return bom_document
