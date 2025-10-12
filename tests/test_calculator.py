from src import calculator as calc
import pytest


def test_add_function():
    assert calc.add(2,0) == 2
    assert calc.add(0,3) == 3
    assert calc.add(-3,-9) == -12
    assert calc.add(3,9) == 12

def test_subtract_function():
    assert calc.sub(2,0) == 2
    assert calc.sub(0,3) == -3
    assert calc.sub(-3,-9) == 6
    assert calc.sub(3,9) == -6    
    
def test_multiply_function():
    assert calc.mul(2,0) == 0
    assert calc.mul(0,3) == 0
    assert calc.mul(-3,-9) == 27
    assert calc.mul(3,9) == 27
    assert calc.mul(1,9) == 9

def test_divide_function():
    assert calc.div(2,0) == None
    assert calc.div(0,3) == 0
    assert calc.div(-36,-9) == 4
    assert calc.div(-36,9) == -4
    assert calc.div(9,9) == 1
    assert calc.div(9,1) == 9

def test_mod_function():
    assert calc.mod(12,5) == 2
    assert calc.mod(100,12) == 4
    assert calc.mod(2,30) == 2  

@pytest.mark.JAN_RELEASE
def test_abs_function():
    assert calc.abs(12) == 12
    assert calc.abs(-12) == 12
    assert calc.abs(0) == 0
    
def test_square_root_function():
    assert calc.get_square_root(100) == 10
    assert calc.get_square_root(0) == 0
    assert calc.get_square_root(169) == 13
    