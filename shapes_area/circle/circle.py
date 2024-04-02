from math import pi
from typing import override

from shapes_area import Shape


class Circle(Shape):
    def __init__(self, radius: int | float):
        self._radius = radius

        self._area = None

    @property
    @override
    def area(self) -> float:
        if self._area is None:
            self._area = pi * self._radius**2
        
        return self._area
