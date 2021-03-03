# importing complex math formulas
# basic formulas will be in the main.py file
import math

from .lib import *


def add(num1, num2):
    return num1 + num2 


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def circle_area(radius):
    return math.pi * pow(radius, 2)
