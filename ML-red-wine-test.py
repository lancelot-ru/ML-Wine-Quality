# Открываем файл с вектором характеристик вина (11 характеристик), получаем ответ на вопрос "Является ли вино с такими характеристиками хорошим?"

import os.path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

import pickle

fname = input('Введите имя файла (по умолчанию - wine-test.csv): ')
if (len(fname) < 1) or not os.path.exists(fname): fname = 'wine-test.csv'

columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
data = pd.read_csv(fname, names=columns)

data.drop(['residual sugar', 'free sulfur dioxide', 'pH'], axis=1, inplace=True)

array = data.values
X = array[:,0:8]

loaded_model = pickle.load(open('final_model.sav', 'rb'))
predictions = loaded_model.predict(X)

if int(predictions[0]) == 1:
    print ('This wine is good / Это хорошее вино')
else:
    print ('This wine is bad / Это плохое вино')
