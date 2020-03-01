import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10.01, 0.1)
plt.plot(x, np.sin(x),
         x, np.cos(x),
         [1, 2, 3, 4, 5],
         [3, 5, 2, 5, 4])
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.grid(True)
plt.savefig('1.png')
plt.show()
