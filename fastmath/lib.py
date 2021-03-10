import math 

# quadratic formula: (-b + or - sqrt(b^2 - 4ac)) / 2a
# define constant
# output is limited to 2 decimal places, can be changed below
dp = '%.2f'

def qudratic(num1, num2, num3):
    try:
        discRoot = math.sqrt((num2 * num2) - 4 * num1 * num3)
        root1 = (-num2 + discRoot) / (2 * num1)
        root2 = (num2 - discRoot) / (2 * num1)
        return dp % root1, dp % root2
    except ValueError as e:
        print("Something is wrong look at the message below\n", e)


