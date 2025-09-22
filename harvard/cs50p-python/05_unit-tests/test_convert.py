import pytest
from convert import convert

def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_error():
    with pytest.raises(TypeError):
        convert("1")

def test_float_conversion():
    # We use pytest.approx to allow for some float rounding
    # error
    # We can set abs=n such that we will accept any value
    # close to the expected value + or - n
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)