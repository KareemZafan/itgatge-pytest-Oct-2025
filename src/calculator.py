import math

def add(a,b):
    return a + b 

def sub(a,b):
    return a - b 

def mul(a,b):
    return a * b 

def div(a,b):
    if b == 0: 
        return None   
    return a / b 

def mod(a,b):
    return a % b

def abs(a):
    if a > 0: 
        return a
    return -a 

def get_square_root(a):
    return  math.sqrt(a)






