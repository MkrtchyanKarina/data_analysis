import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_excel("Iris.xlsx")


# Нормализация данных(заменяем названия вида цифрой от 1 до 3)
dataframe['Species'].replace("Iris-setosa",1,inplace= True)
dataframe['Species'].replace("Iris-versicolor",2,inplace = True)
dataframe['Species'].replace("Iris-virginica",3,inplace=True)



# Корреляционная матрица
correlation = dataframe.corr()
plt.figure(figsize=(15,15))
sns.heatmap(correlation, vmax=1, square=True,annot=True,cmap='cubehelix')

plt.title('Correlation between different fearures')
plt.show()



# Коэффициент корреляции
def coef_ab(x, y):
    l = len(x)
    # PetalLengthCm - y
    # PetalWidthCm - x
    a1 = l * sum([x[i] * y[i] for i in range(l)])
    a2 = sum(x) * sum(y)
    a3 = l * sum(i ** 2 for i in x)
    a4 = sum(x) ** 2
    a = (a1 - a2)/(a3 - a4)
    b = (sum(y) - sum(x) * a)/ l
    return [round(a, 2), round(b, 2)]
AB = coef_ab(dataframe['PetalWidthCm'], dataframe['PetalLengthCm'])
A = AB[0]
B = AB[1]
print(A, B)
plt.scatter(dataframe['PetalWidthCm'], dataframe['PetalLengthCm'])
plt.plot(dataframe['PetalWidthCm'], dataframe['PetalWidthCm'] * A + B, color="red")
plt.xlabel('PetalWidthCm')
plt.ylabel('PetalLengthCm')
plt.show()



# Отображаем данные ирисов на графике с 3 осями(длина чашелистика, длина и ширина лепестка)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('SepalLengthCm')
ax.set_ylabel('PetalLengthCm')
ax.set_zlabel('PetalWidthCm')

x = dataframe['SepalLengthCm']
y = dataframe['PetalLengthCm']
z = dataframe['PetalWidthCm']
name = dataframe['Species']

for i in range(len(x)):
    if name[i] == 1:
        ax.scatter(x[i], y[i], z[i], color="red")
    elif name[i] == 2:
        ax.scatter(x[i], y[i], z[i], color="green")
    else:
        ax.scatter(x[i], y[i], z[i], color="blue")
plt.show()
