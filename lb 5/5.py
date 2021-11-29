from scipy import optimize
from math import sin
from math import cos
from math import fabs

x0 = -0.8
y0 = 1


def f1(y):
    return -1 + sin(y + 0.5)


def f2(x):
    return -cos(x - 2)


def method(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1

    while ((fabs(xn1 - xn) >= e) and (fabs(yn1 - yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n += 1

    print("x1= ", xn, "\ny1= ", yn, "\n Amount of iteration= ", n)


method(x0, y0, 0.001)

def check(x):
    return sin(x[0] + 0.5) - x[1] -1, cos(x[1] - 2) +x[0]
