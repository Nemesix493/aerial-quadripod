"""Module implementing a material length optimizer using best-fit strategy."""

from .base_material_optimizer import MaterialOptimizer
from ..project_info import ProjectInfo


class LengthOptimizer(MaterialOptimizer):
    """Optimizer for cutting parts from stock material with limited usable length."""

    @classmethod
    def get_all(cls):
        """Return a list of LengthOptimizer instances for all 1D materials in the project."""
        construct_info = ProjectInfo.get_construct_info()
        return [
            cls(
                material=material,
                cut_line_thickness=construct_info['cut_line_thickness'],
                cut_line_tolerance=construct_info['cut_line_tolerance'],
                parts=[
                    part
                    for part in ProjectInfo.get_parts()
                    if part['material_id'] == material['id']
                ]
            )
            for material in ProjectInfo.get_materials()
            if len(material['dim']) == 1
        ]

    @property
    def optimized_cutting_plans(self):
        """Compute and return an optimized cutting plan using a best-fit algorithm.

        Returns:
            list: A list of stocks used, each with remaining length and assigned parts.
        """
        if not hasattr(self, "_optimized_cutting_plans"):
            parts = sorted(
                self.parts, reverse=True, key=lambda part: part['max_length']
            )
            stocks = []
            for part in parts:
                for _ in range(part['quantity']):
                    fits = [
                        (i, stocks[i]['remaining'] - part['max_length'] - self.cut_margin)
                        for i in range(len(stocks))
                        if stocks[i]['remaining'] - part['max_length'] - self.cut_margin >= 0
                    ]
                    if fits:
                        index, remaining = min(fits, key=lambda item: item[1])
                        stocks[index]['remaining'] = remaining
                        stocks[index]['parts'].append(part)
                    else:
                        new_stock = {
                            'remaining':
                                self.material['dim'][0] - part['max_length'] - self.cut_margin,
                            'parts': [part]
                        }
                        stocks.append(new_stock)
            setattr(self, "_optimized_cutting_plans", stocks)
        return getattr(self, "_optimized_cutting_plans")
