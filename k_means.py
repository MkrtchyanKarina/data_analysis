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
x3 = uniform(min(y), max(y))
y3 = uniform(min(y), max(y))



for k in range(5):
    spices = []
    X1 = 0
    Y1 = 0
    X2 = 0
    Y2 = 0
    X3 = 0
    Y3 = 0
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('sepalLength')
    ax.set_ylabel('petalLength')
    for i in range(150):
        l1 = math.sqrt((x[i] - x1) ** 2 + (y[i] - y1) ** 2)
        l2 = math.sqrt((x[i] - x2) ** 2 + (y[i] - y2) ** 2)
        l3 = math.sqrt((x[i] - x3) ** 2 + (y[i] - y3) ** 2)
        if l1 < l2 and l1 < l3:
            spices.append(0)
            X1 += x[i]
            Y1 += y[i]
        elif l2 < l3 and l2 < l1:
            spices.append(1)
            X2 += x[i]
            Y2 += y[i]
        else:
            spices.append(2)
            X3 += x[i]
            Y3 += y[i]

    x1 = X1 / spices.count(0)
    x2 = X2 / spices.count(1)
    y1 = Y1 / spices.count(0)
    y2 = Y2 / spices.count(1)
    X3 = X3 / spices.count(2)
    Y3 = Y3 / spices.count(2)
    for j in range(len(x)):
        if spices[j] == 1:
            ax.scatter(x[j], y[j], color="red")
        elif spices[j] == 0:
            ax.scatter(x[j], y[j], color="green")
        else:
            ax.scatter(x[j], y[j], color="blue")
    ax.scatter(x1, y1, color="black")
    ax.scatter(x2, y2, color="black")
    ax.scatter(x3, y3, color="black")
    plt.show()
    
    
    
   """
from sklearn.cluster import KMeans
import pandas as pd
dataframe = pd.read_csv("iris.csv")
import matplotlib.pyplot as plt

dataframe['variety'].replace("Setosa",1,inplace= True)
dataframe['variety'].replace("Versicolor",2,inplace = True)
dataframe['variety'].replace("Virginica",3,inplace=True)

# Описываем модель
model = KMeans(n_clusters=3)

# Проводим моделирование
model.fit(dataframe)

x = dataframe['sepalLength']
y = dataframe['petalLength']
# Предсказание на всем наборе данных
spices = model.predict(dataframe)
fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('sepalLength')
ax.set_ylabel('petalLength')
for j in range(len(x)):
    if spices[j] == 1:
        ax.scatter(x[j], y[j], color="red")
    elif spices[j] == 0:
        ax.scatter(x[j], y[j], color="green")
    else:
        ax.scatter(x[j], y[j], color="blue")

plt.show()"""
