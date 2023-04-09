# классификатор по наличию/отсутствию сердечных заболеваний
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


data = pd.read_csv("heart.csv")


ord_enc = OrdinalEncoder()
data["Sex"] = ord_enc.fit_transform(data[["Sex"]])
data["ChestPainType"] = ord_enc.fit_transform(data[["ChestPainType"]])
data["ST_Slope"] = ord_enc.fit_transform(data[["ST_Slope"]])
data["ExerciseAngina"] = ord_enc.fit_transform(data[["ExerciseAngina"]])
data["RestingECG"] = ord_enc.fit_transform(data[["RestingECG"]])
print(data)


min_max_Scalar = preprocessing.MinMaxScaler()
col = data.columns
scaled_df = pd.DataFrame(min_max_Scalar.fit_transform(data), columns=col)
print(scaled_df)



# 3. Random Forest Classifier (RF) - Случайный лес (используются деревья решений)
# 5. AdaBoost (Adaptive Boosting) Classifier (AB) - Адаптивное усиление
# 6. Decision tree classifier (DT) - Дерево решений (http://scikit-learn.org/stable/modules/tree.html)
# 8. Gaussian Naive Bayes (NB) - Гауссовский наивный байесовский классификатор
data_array = data.values
x = data_array[:, 0:11]  # характеристики
y = data_array[:, 11]  # класс


classifiers = []
classifiers.append(('RF', RandomForestClassifier(max_depth = 5, n_estimators = 10, max_features = 1)))
classifiers.append(('AB', AdaBoostClassifier()))
classifiers.append(('DT', DecisionTreeClassifier()))
classifiers.append(('NB', GaussianNB()))


results = []
names = []
k = 10
for name, classifier in classifiers:
    kfold = model_selection.KFold(n_splits = k, random_state = 348,  shuffle=True)
    cv_results = model_selection.cross_val_score(classifier, x, y, cv = kfold, scoring = 'accuracy')
    results.append(cv_results)
    names.append(name)
    print(name, np.round(cv_results, 3), 'Средняя точность: ', round(cv_results.mean(), 3))
    
fig = plt.figure()
fig.suptitle('Точность, показанная классификаторами')
ax = fig.add_subplot(1, 1, 1)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
