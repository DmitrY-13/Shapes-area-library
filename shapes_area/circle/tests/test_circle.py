import pytest

from shapes_area import Circle


class TestCircle:
    @pytest.mark.parametrize(
        'radius, expected_area',
        (
            (3, 28.27),
            (13, 530.93),
            (25, 1963.5),
        )
    )
    def test_area_calculating(self, radius, expected_area):
        circle_area = Circle(radius).area
        assert round(circle_area, 2) == expected_area
