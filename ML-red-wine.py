# Обучаем модель Random Forest Classifier, сохраняем ее в файл

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

import pickle

###

data_with_dichotomy = pd.read_csv('winequality-red.csv')

for i in range(data_with_dichotomy.shape[0]):
    if(data_with_dichotomy['quality'][i] < 7):
        data_with_dichotomy['quality'][i] = 0
    else:
        data_with_dichotomy['quality'][i] = 1

data_with_dichotomy.drop(['residual sugar', 'free sulfur dioxide', 'pH'], axis=1, inplace=True)

array = data_with_dichotomy.values
X = array[:,0:8]
Y = array[:,8]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

final_model = RandomForestClassifier(n_estimators=100, random_state=42)
final_model.fit(X_train, Y_train)
filename = 'final_model.sav'
pickle.dump(final_model, open(filename, 'wb'))
