from math import pi
from typing import override, Any

from shapes_area import Shape


class Circle(Shape):
    def __init__(self, radius: int | float):
        if not self._is_valid_radius_type(radius):
            raise TypeError('radius type must be int or float')

        self._radius = radius

        self._area = None

    @property
    @override
    def area(self) -> float:
        if self._area is None:
            self._area = pi * self._radius**2
        
        return self._area

    @staticmethod
    def _is_valid_radius_type(radius: Any) -> bool:
        return isinstance(radius, (int, float))
