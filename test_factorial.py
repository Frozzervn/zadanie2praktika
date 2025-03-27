# test_factorial.py

import pytest
from factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_two():
    assert factorial(2) == 2

def test_factorial_three():
    assert factorial(3) == 6

def test_factorial_four():
    assert factorial(4) == 24

def test_factorial_five():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError, match="Факториал не определён для отрицательных чисел."):
        factorial(-1)

def test_factorial_large_number():
    assert factorial(10) == 3628800
