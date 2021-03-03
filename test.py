import math

from fastmath import *


def test(func, desired_result, *params):
    res = func(*params)
    return res == desired_result, res


# Main tests
TESTS = [
    ('add', add, 2, 1, 1),
    ('sub', sub, 0, 1, 1),
    ('mul', mul, 2, 1, 2),
    ('div', div, 0.5, 1, 2),
    ('circle_area', circle_area, math.pi, 1),

]

print('\nRunning tests ...\n')

for TEST in TESTS:
    print(TEST[0], end='\t=>\t')
    res = test(*TEST[1:])
    print('{}\t=>\t'.format(res[1]), end=' ')
    print('SUCCESSFUL' if res[0] else 'FAILED')

print('\ndone\n')
