<<<<<<< HEAD
from .lib import *
from .trig import *
=======
<<<<<<< HEAD
from lib import *
from trig import *
=======
# importing complex math formulas
# basic formulas will be in the main.py file
import math

from .lib import *

>>>>>>> 0cd6b73977149b6af5be7ae2b25b7ff57248cd75
>>>>>>> MartinKondor-feature/better_usage

def add(num1, num2):
    return num1 + num2 


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2

<<<<<<< HEAD
def circle_area(num1):
                # radius
    return 3.14 * pow(num1, 2)

def fac(num1):
    num_list = []
    y = 1
    for i in range(1, int(num1) + 1):
        num_list.append(i)
    for x in num_list:
        num1 = num1 * x
    return num1

def sqrt(num1):
    assert num1 >= 0, "Can't take the square root of negative numbers"
    def f(guess):
        if(guess == num1/guess):
            return guess
        else:
            return f((num1/guess + guess)/2)
    return f(1)

def pi():
    total = 4.0
    d = 3.0
    toAdd = False
    while 4/d > pow(10, -5):
        if(toAdd):
            total += 4 / d
        else:
            total -= 4 / d
        toAdd = not toAdd
        d += 2
    return total
"""
def e(num1):
    total2 = 1.0
    d = 1.0
    while pow(num1, d)/fac(d) > pow(10, -7):
        total2 += pow(num1, d)/fac(d)
        d += 1
    return total2

"""

def integrate(num1, num2, num3):
    if(num2 > num3):
        return - integrate(num1, num3, num2)
    total = 0
    iters = 1000
    while(num2 <= num3):
        total += (num1(num2) + num1(num2+1.0/iters)) / (2 * iters)
        num2 += 1.0 / iters
    return round(total, 8)

def ln(num1):
    assert num1 > 0, "Can't take the natural log of a negative number or 0"
    return integrate(lambda n: 1/n, 1, num1)

fact = lambda n: (lambda f, n: f(f, n))(lambda f, n: n * f(f, n-1) if n > 1 else 1, n)
=======
>>>>>>> 0cd6b73977149b6af5be7ae2b25b7ff57248cd75

def circle_area(radius):
    return math.pi * pow(radius, 2)
