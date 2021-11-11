# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:03:46 2021

@author: Juan Carlos
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
import pickle

np.random.seed(6)
data = pd.read_csv(('src/data.csv'), index_col=0)
size = len(data)
ids = np.array(data)[:,0]
tipo = np.array(data)[:,1]
idp = np.array(data)[:,2]
data = np.array(data)[:,3:7]
m = np.array(data, dtype=np.float64)
data = np.array(data, dtype=np.float64) / 255 #Normalizar(Números entre 0 y 1)
x = data

#Mostrar valores para cada registro
plt.imshow(data[0:6])
plt.title('Valores de cada registro')
plt.show()

clusters = 4# Se va a mandar cuantos clusters por dataset

#Instanciar modelo
model = cluster.KMeans(n_clusters = clusters)
model.fit(x)
y = (model.predict(x))#Como es no supervisado se envia solo variable de entrada

for i in range (size):
    print("Registro", i, "pertenece a la clase", y[i])

#Se guarda el modelo
pickle.dump(model, open('src/Modelo_Clasificacion.sav', 'wb'))

clases = pd.DataFrame(columns=('ID_Objeto', 'ID_Pro', 'Tipo', 'Clase'))

for i in range (size):
    clases.loc[len(clases)]=[ids[i], idp[i], tipo[i], y[i]]
clases.to_csv('src/clases.csv')
