from src import calculator as calc
import pytest

test_data = [(90,0,90),(0,3,3),(-3,-9,-12),(3,9,12),(44,-4,40),(9,-80,-71)]
@pytest.mark.parametrize("a,b,result",test_data)
def test_add_function(a,b,result):
    assert calc.add(a,b) == result
    

def test_subtract_function():
    assert calc.sub(2,0) == 2
    assert calc.sub(0,3) == -3
    assert calc.sub(-3,-9) == 6
    assert calc.sub(3,9) == -6    

test_data_mul = [(2,0,0),(0,3,0),(-3,-9,27),(3,9,27),(3,-9,-27),(1,9,9)]    
@pytest.mark.parametrize("num1,num2,res",test_data_mul)
def test_multiply_function(num1,num2,res):
    assert calc.mul(num1,num2) == res
    

#@pytest.mark.skip(reason="It has bugs")
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

day = 31 # day of month is 15
@pytest.mark.skipif(day < 28, reason="Checking the bill payment starting from day 28")
def test_square_root_function():
    assert calc.get_square_root(100) == 10
    assert calc.get_square_root(0) == 0
    assert calc.get_square_root(169) == 13
    