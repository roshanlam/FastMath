import math 


<<<<<<< HEAD
def qudratic(num1, num2, num3):
    try:
        discRoot = math.sqrt((num2 * num2) - 4 * num1 * num3)
        root1 = (-num2 + discRoot) / (2 * num1)
        root2 = (num2 - discRoot) / (2 * num1)
        return dp % root1, dp % root2
    except ValueError as e:
        print("Something is wrong look at the message below\n", e)
=======
def quadratic(a, b, c, decimal_places='%.2f'):
    """
    Quadratic formula: (-b + or - sqrt(b^2 - 4ac)) / 2a
    :a, b, c: coefficents
    :decimal_places: Output is limited to 2 decimal places, but can be changed
    """
>>>>>>> MartinKondor-feature/better_usage

    disc_root = math.sqrt(pow(b, 2) - 4 * a * c)
    denom = (2 * a)
    root_1 = (-b + disc_root) / denom
    root_2 = (b - disc_root) / denom

    return decimal_places % root_1, decimal_places % root_2
