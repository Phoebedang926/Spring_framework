# tests/test_calculator.py
import pytest
from src.calculator import *




def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 0) == 0
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(6, 2) == 3
    assert divide(9, 3) == 3
    assert pytest.approx(divide(1, 3), 0.33)  # Approximate check for floating point numbers
    with pytest.raises(ValueError):
        divide(5, 0)
