from math import sqrt, radians, sin
from random import randint

import pytest


def random_side_size() -> int:
    return randint(1, 100)


def random_angle() -> float:
    return radians(randint(46, 89))


@pytest.fixture
def right_triangle_sides_sizes() -> tuple[int, int, float]:
    a = random_side_size()
    b = random_side_size()
    c = sqrt(a**2 + b**2)

    return a, b, c


@pytest.fixture
def non_right_triangle_sides_sizes() -> tuple[int, float, float]:
    angle_a = random_angle()
    angle_b = random_angle()
    angle_c = radians(180) - angle_a - angle_b

    sin_a = sin(angle_a)

    side_a = random_side_size()
    side_b = side_a * sin(angle_b) / sin_a
    side_c = side_a * sin(angle_c) / sin_a

    return side_a, side_b, side_c


@pytest.fixture
def impossible_triangle_sides_sizes() -> tuple[int, int, int]:
    a = random_side_size()
    b = random_side_size()
    c = a + b + 1

    return a, b, c
