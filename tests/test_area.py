from src.area import calculate_area_square
import pytest

def test_area_valid_student_id_output():
    # last two digits of 100959264 => 64 ; 8 x 8 = 64
    assert calculate_area_square(8) == 64

import pytest
@pytest.mark.parametrize("x,expected", [(1,1),(2.5,6.25),(10,100)])
def test_parametric(x, expected):
    assert calculate_area_square(x) == expected

@pytest.mark.parametrize("bad", [0, -1, "a", None])
def test_invalid(bad):
    with pytest.raises(TypeError):
        calculate_area_square(bad)
