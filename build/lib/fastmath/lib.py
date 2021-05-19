import math 

def quadratic(a, b, c, decimal_places='%.2f'):
    """
    Quadratic formula: (-b + or - sqrt(b^2 - 4ac)) / 2a
    :a, b, c: coefficents
    :decimal_places: Output is limited to 2 decimal places, but can be changed
    """
    disc_root = math.sqrt(pow(b, 2) - 4 * a * c)
    denom = (2 * a)
    root_1 = (-b + disc_root) / denom
    root_2 = (b - disc_root) / denom

    return decimal_places % root_1, decimal_places % root_2
