import numpy as np
import matplotlib.pyplot as plt
import math
n = -10
h = 0.1
r = 100
x = []
y = []
p = []

f = lambda x_: math.sin(x_)

for i in range(r):
    x.append(n)
    y.append(f(n))
    p_ = math.cos(n)
    p.append(p_)
    n -= p_ * h
    # h *= 0.8

for i in range(r):
    print(str(i + 1) + " точка: (" + str(x[i]) + " ; " + str(y[i]) + "), производная " + str(p[i]))

x = np.array(x)
y = np.array(y)
plt.figure(figsize=(5, 5))
plt.plot(x, y)

for i in range(r):
    plt.scatter(x[i], y[i])
plt.show()
# P = lambda x_: (f(x_ - 2 * q) - 8 * f(x_ - q) + 8 * f(x_ + q) - f(x_ + 2 * q)) / (12 * q)
