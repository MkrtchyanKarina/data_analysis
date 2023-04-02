import numpy as np
import matplotlib.pyplot as plt
q = 0.05
# f1 = lambda x: ((x ** 2) * 2 + 5 * (x ** 2)) ** 3
# d1 = lambda x_: 48 * x_ ** 5 + 2400*(x_ ** 15) + 660 * (x_ ** 10) + 2625 * (x_ ** 20)

D1 = lambda x, F: (F(x - 2 * q) - 8 * F(x - q) + 8 * F(x + q) - F(x + 2 * q)) / (12 * q)
D2 = lambda x, F: (F(x + q) - F(x - q)) / (2 * q)

f1 = lambda x: 7 * x ** 6
d1 = lambda x: 42 * x ** 5

f2 = lambda x: 7 * x ** 3 + 4 * x ** 2 + 4
d2 = lambda x: 21 * x ** 2 + 8 * x

f3 = lambda x: np.sin(x ** 2)
d3 = lambda x: np.cos(x ** 2) * 2 * x

f4 = lambda x: (x ** 4 - 16) / x ** 7
d4 = lambda x: ((4 * x ** 3) * (x ** 7) - (7 * x ** 6) * (x ** 4 - 16)) / (x ** 14)

f5 = lambda x: x ** 2
d5 = lambda x: 2 * x


def gradient_descent(func, der):
    r = 15
    h = 0.04
    n = 1
    x_ = np.arange(-1, 1.01, 0.01)
    plt.plot(x_, func(x_))

    for i in range(r):
        d = der(n)
        plt.scatter(n, func(n))
        print(str(i + 1) + " точка: (" + str(n) + " ; " + str(func(n)) + "), производная " + str(d))
        if i == 14:
            print(str(i + 1) + " точка: (" + str(n) + " ; " + str(func(n)) + "), производная " + str(D1(n, func)))
            print(str(i + 1) + " точка: (" + str(n) + " ; " + str(func(n)) + "), производная " + str(D2(n, func)))
        n -= d * h
    plt.show()


print("\nПервая функция:\n")
gradient_descent(f1, d1)
print("\nВторая функция:\n")
gradient_descent(f2, d2)
print("\nТретья функция:\n")
gradient_descent(f3, d3)
print("\nЧетвёртая функция:\n")
gradient_descent(f4, d4)
print("\nПятая функция:\n")
gradient_descent(f5, d5)

# x = np.array(x)
# y = np.array(y)
# plt.figure(figsize=(5, 5))
# plt.plot(x, y)
#
# for i in range(r):
#     plt.scatter(x[i], y[i])
# plt.show()
