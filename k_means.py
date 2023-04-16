import pandas as pd
import matplotlib.pyplot as plt
from random import uniform
import math
dataframe = pd.read_csv("iris.csv")

dataframe['variety'].replace("Setosa",1,inplace= True)
dataframe['variety'].replace("Versicolor",2,inplace = True)
dataframe['variety'].replace("Virginica",3,inplace=True)

x = dataframe['sepalLength']
y = dataframe['petalLength']
name = dataframe['variety']



x1 = uniform(min(x), max(x))
x2 = uniform(min(x), max(x))
y1 = uniform(min(y), max(y))
y2 = uniform(min(y), max(y))



for k in range(5):
    spices = []
    X1 = 0
    Y1 = 0
    X2 = 0
    Y2 = 0
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('sepalLength')
    ax.set_ylabel('petalLength')
    for i in range(150):
        l1 = math.sqrt((x[i] - x1) ** 2 + (y[i] - y1) ** 2)
        l2 = math.sqrt((x[i] - x2) ** 2 + (y[i] - y2) ** 2)
        if l1 < l2:
            spices.append(0)
            X1 += x[i]
            Y1 += y[i]
        else:
            spices.append(1)
            X2 += x[i]
            Y2 += y[i]
    x1 = X1 / spices.count(0)
    x2 = X2 / spices.count(1)
    y1 = Y1 / spices.count(0)
    y2 = Y2 / spices.count(1)
    for j in range(len(x)):
        if spices[j] == 1:
            ax.scatter(x[j], y[j], color="red")
        elif spices[j] == 0:
            ax.scatter(x[j], y[j], color="green")
    ax.scatter(x1, y1, color="black")
    ax.scatter(x2, y2, color="black")
    plt.show()
