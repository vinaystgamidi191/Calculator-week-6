from app.calculator import add, subtract

def test_addition():
    '''Test that addition function works'''    
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works'''    
    assert subtract(2, 2) == 0


import pytest
from decimal import Decimal
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (Decimal('2.5'), Decimal('3.5'), Decimal('6')),
])
def test_addition(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (Decimal('5.5'), Decimal('3.5'), Decimal('2')),
])
def test_subtraction(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 0, 0),
    (Decimal('2.5'), Decimal('3.5'), Decimal('8.75')),
])
def test_multiplication(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (0, 5, 0),
    (Decimal('10'), Decimal('2'), Decimal('5')),
])
def test_division(calculator, a, b, expected):
    if b == 0:
        with pytest.raises(ValueError):
            calculator.divide(a, b)
    else:
        assert calculator.divide(a, b) == expected

def test_clear_history(calculator):
    calculator.add(2, 3)
    calculator.subtract(5, 3)
    calculator.clear_history()
    assert calculator.get_history() == []

def test_history(calculator):
    calculator.add(2, 3)
    calculator.subtract(5, 3)
    assert calculator.get_history() == [(2, 3, '+', 5), (5, 3, '-', 2)]
