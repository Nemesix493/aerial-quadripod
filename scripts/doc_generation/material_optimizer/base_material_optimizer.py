"""Base module defining the interface for material optimization strategies."""

from abc import ABC, abstractmethod
from itertools import chain


class MaterialOptimizer(ABC):
    """Abstract base class for material optimization.

    Defines the structure and required interface for any subclass that performs
    material cutting plan optimization.
    """

    @classmethod
    def get_all(cls) -> list:
        """Return a chain of all available cutting plans from subclasses.

        This method calls `get_all()` on each subclass of MaterialOptimizer.
        Returns:
            list: A list of all cutting plans.
        """
        return list(chain(
            *(
                sub_class.get_all()
                for sub_class in cls.__subclasses__()
            )
        ))

    @property
    def cut_margin(self):
        """Calculate and return the total margin needed for cutting.

        The cut margin is defined as twice the cut line thickness plus the tolerance.
        Returns:
            int: The computed cut margin.
        """
        return self.cut_line_thickness * 2 + self.cut_line_tolerance

    @property
    @abstractmethod
    def optimized_cutting_plans(self):
        """Abstract property to be implemented by subclasses.

        Should return the optimized cutting plans based on the implementation logic.
        """

    def __init__(self, material: dict, cut_line_thickness: int,
                 cut_line_tolerance: int, parts: list):
        """Initialize the material optimizer with configuration and parts data.

        Args:
            material (dict): The material specification.
            cut_line_thickness (int): Thickness of the cut line.
            cut_line_tolerance (int): Tolerance around the cut line.
            parts (list): List of part specifications to optimize.
        """
        self.material = material
        self.cut_line_thickness = cut_line_thickness
        self.cut_line_tolerance = cut_line_tolerance
        self.parts = parts
