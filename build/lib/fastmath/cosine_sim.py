import math

def cosine_sim(vector1, vector2):
    vector1 = list(vector1)
    vector2 = list(vector2)
    dot_prod = 0
    for i, v in enumerate(vector1):
        dot_prod += v * vector2[i]
    mag_1 = math.sqrt(sum([x**2 for x in vector1]))
    mag_2 = math.sqrt(sum([x**2 for x in vector2]))
    return dot_prod / (mag_1 * mag_2)