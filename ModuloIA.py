# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 01:25:36 2021

@author: Juan Carlos
"""
import urllib.request
import pandas as pd
import numpy as np
import pickle
import random

def predictor(data):

    tipo = data[0]
    data.remove(tipo)
    print("data0: ", data)
    data = list(map(int, data))
    print("data: ", data)

    objeto = np.array(data).reshape(1, -1)
    objeto = np.array(objeto, dtype=np.float64) / 255

    model = pickle.load(open('src/Modelo_Recomendacion.sav', 'rb'))
    clase_pred = model.predict(objeto)
    print('Predicción: ', clase_pred)
    print('')
    clases = pd.read_csv(('src/clases.csv'), index_col=0)
    registros = []
    nombres = []
    fotos = []

    for i in range(clases['Clase'].size):
        if clases['Clase'][i] == clase_pred:
            if clases['Tipo'][i] == tipo:
                registro = [clases['ID_Objeto'][i], clases['ID_Pro'][i]]
                registros.append(registro)
                print(registro)
                nombre = urllib.request.urlopen('http://api.findqci.online/objeto/objeto.php?opc=8&id=' + str(registro[0])).read().decode()
                foto = urllib.request.urlopen('http://api.findqci.online/imagenes_objeto/imagenes_objeto.php?opc=10&objeto=' + str(registro[0])).read().decode()
                nombres.append(nombre)
                fotos.append(foto)
    clase = clase_pred[0]
    print(registros.__len__())
    return registros, nombres, tipo, fotos
