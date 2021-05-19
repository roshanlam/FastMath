import math

def sin(num1):
    total = 0
    total = math.sin(num1)
    return total

def cos(num1):
    total = 0
    total = math.cos(num1)
    return total

def tan(num1):
    total = 0
    total = math.tan(num1)
    return total

def cot(num1):
    total = 0
    total = math.atan(num1)
    return total

def csc(num1):
    if(num1 == 0):
        return 'Undefined'
    total = 0
    total = math.acos(num1)
    return total

def sec(num1):
    total = 0
    total = math.asin(num1)
    return total

