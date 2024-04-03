from math import sqrt
from typing import override, Any

from shapes_area import Shape


class Triangle(Shape):
    def __init__(self, a: int | float, b: int | float, c: int | float):
        if not self._is_valid_sides_types(a, b, c):
            raise TypeError('a, b, c types must be int or float')

        if not self._is_possible_triangle(a, b, c):
            raise ValueError('impossible triangle sides sizes')

        self._a = a
        self._b = b
        self._c = c

        self._area = None

    @property
    @override
    def area(self) -> float:
        if self._area is None:
            half_perimeter = (self._a + self._b + self._c) / 2
            self._area = sqrt(
                half_perimeter
                * (half_perimeter - self._a)
                * (half_perimeter - self._b)
                * (half_perimeter - self._c)
            )

        return self._area

    def is_right(self, acceptable_error: float = 0) -> bool:
        """
        :param acceptable_error: When sides of triangle is floats with large fractional part, error may occur.
                                 In this parameter, you can specify acceptable error.
        """
        if not self._is_valid_acceptable_error_type(acceptable_error):
            raise TypeError('acceptable_error type must be float')

        a, b, c = sorted((self._a, self._b, self._c))
        return abs((a ** 2 + b ** 2) - c ** 2) <= acceptable_error

    @staticmethod
    def _is_possible_triangle(a: int | float, b: int | float, c: int | float):
        return a + b > c and a + c > b and b + c > a

    @staticmethod
    def _is_valid_sides_types(a: Any, b: Any, c: Any) -> bool:
        return all(map(
            lambda side: isinstance(side, (int, float)),
            (a, b, c)
        ))

    @staticmethod
    def _is_valid_acceptable_error_type(acceptable_error: Any) -> bool:
        return isinstance(acceptable_error, float)
