#Y(x)=10*cos(x^2)/x^2, x=[0...4] 
from numpy import *
import matplotlib.pyplot as plt
x = linspace(1,4)
y = 10*cos(x*2)/x*2
plt.plot(x, y, 'g^')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
loc='best'
plt.show()