from main import sqrt
from statsfolder import variance

def rms(num):
    # Root Mean Square
    if type(num) not in [list, tuple]:
        raise TypeError('rms() expects a list or a tuple.')
    squs = []
    # Squares

    squs = [pow(n, 2) for n in num]
    sos = sum(squs)
    # sum of squares
    ms = sos / len(num)
    r_m_s = sqrt(ms)
    return r_m_s
