import pytest

from shapes_area import Triangle


class TestTriangle:
    ACCEPTABLE_ERROR = 0.0000001

    @pytest.mark.parametrize(
        'sides_sizes, expected_area',
        (
            ((5, 3, 4), 6),
            ((8, 4, 6), 11.62),
            ((10, 2, 11), 9.05),
        )
    )
    def test_area_calculating(self, sides_sizes, expected_area):
        triangle_area = Triangle(*sides_sizes).area
        assert round(triangle_area, 2) == expected_area

    def test_check_for_right_triangle_with_right_triangle_sides_sizes(self, right_triangle_sides_sizes):
        assert Triangle(*right_triangle_sides_sizes).is_right(self.ACCEPTABLE_ERROR)

    def test_check_for_right_triangle_non_right_triangle_sides_sizes(self, non_right_triangle_sides_sizes):
        assert not Triangle(*non_right_triangle_sides_sizes).is_right(self.ACCEPTABLE_ERROR)

    def test_impossible_triangles_sides_sizes(self, impossible_triangle_sides_sizes):
        try:
            Triangle(*impossible_triangle_sides_sizes)
        except Exception as exc:
            assert isinstance(exc, ValueError)
            assert str(exc) == 'impossible triangle sides sizes'
        else:
            pytest.fail('exception did not raised')
