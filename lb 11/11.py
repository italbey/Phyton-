import matplotlib.pyplot as plt
import sympy as sp
from math import e


def Teylor(x):
    y=0
    d1 = sp.diff(f,x)
    d2 = sp.diff(d1,x)
    d3 = sp.diff(d2,x)
    print ('d1= ', d1, 'd2= ',d2, 'd3= ', d3)
    y += f + d1 * x + d2*(x-0)**2/2+d3 * (x-0)**3/6
    print ( "y= ", y)
    return y
x = sp.symbols('x')
f = e ** - 2+x **2
Teylor_x = Teylor(x)
pl= sp.plot (f, Teylor_x, (x,-10,10), label= 'Teylor')
plt.show
    