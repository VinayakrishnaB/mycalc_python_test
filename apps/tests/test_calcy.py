import pytest
from calcy import calcy

cal = calcy()

def test_add():
    assert cal.add(2, 3) == 5

def test_sub():
    assert cal.sub(5, 3) == 2

def test_multiply():
    assert cal.multiply(4, 3) == 12

def test_divide():
    assert cal.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        cal.divide(10, 0)
