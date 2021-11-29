from numpy import *
import matplotlib.pyplot as plt
x=linspace(0,10,51)
y=x**cos(x**2)
plt.plot(x,y,'g--',label='x^cos(x^2)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('My first graphic')
plt.legend()
plt.show()