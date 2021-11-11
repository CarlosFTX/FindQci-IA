# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:25:15 2021

@author: Juan Carlos
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
import pickle

#Carga de modelo realizado con el clasificador K-Means
model = pickle.load(open('src/Modelo_Clasificacion.sav','rb'))
data = pd.read_csv(('src/data.csv'), index_col=0)
data = np.array(data)[:,3:7]
data = (np.array(data, dtype=np.float64) / 255) #Normalizar(Números entre 0 y 1)
x = data


y = (model.predict(x))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)


#Selección del modelo
model = KNeighborsClassifier(n_neighbors=2)
model.fit(x_train, y_train)
print('- Train: ', model.score(x_train, y_train))
print('- Test: ', model.score(x_test, y_test))


#Prediccion de resultados con el conjunto de test
y_pred = model.predict(x_test) #Predicciones realizadas por K-NN

#Se guarda el modelo
pickle.dump(model, open('src/Modelo_Recomendacion.sav', 'wb'))
