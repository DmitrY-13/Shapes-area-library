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
        with pytest.raises(ValueError) as excinfo:
            Triangle(*impossible_triangle_sides_sizes)

        assert str(excinfo.value) == 'impossible triangle sides sizes'

    def test_invalid_sides_types(self, non_right_triangle_sides_sizes):
        def check_exception_with_invalid_sides_types(side_sizes):
            with pytest.raises(TypeError) as excinfo:
                Triangle(*side_sizes)

            assert str(excinfo.value) == 'a, b, c types must be int or float'

        for i in range(3):
            sides_sizes = list(non_right_triangle_sides_sizes)
            sides_sizes[i] = ''
            check_exception_with_invalid_sides_types(sides_sizes)

        for i, j in zip(range(3), range(-1, 2)):
            sides_sizes = list(non_right_triangle_sides_sizes)
            sides_sizes[i] = ''
            sides_sizes[j] = ''
            check_exception_with_invalid_sides_types(sides_sizes)

        check_exception_with_invalid_sides_types(('', '', ''))

    def test_invalid_acceptable_error_type(self, non_right_triangle_sides_sizes):
        with pytest.raises(TypeError) as excinfo:
            Triangle(*non_right_triangle_sides_sizes).is_right('')

        assert str(excinfo.value) == 'acceptable_error type must be float'
