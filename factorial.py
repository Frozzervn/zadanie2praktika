# factorial.py

from math import factorial


def fact(x):
    if x == 0:
        return 1
    return factorial(x)


print(fact(0))
