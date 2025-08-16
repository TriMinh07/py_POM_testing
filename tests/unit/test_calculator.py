import pytest
from src.calculator import add, div

def test_add_basic():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a,b,expected", [(1,2,3), (-1,1,0), (2.5,0.5,3.0)])
def test_add_param(a,b,expected):
    assert add(a, b) == expected

def test_div_ok():
    assert div(6, 2) == 3

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
