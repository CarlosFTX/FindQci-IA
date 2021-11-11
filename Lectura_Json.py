# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:01:44 2021

@author: Juan Carlos
"""
import pandas as pd
import urllib.request
import json

getUrl = "http://api.findqci.online/objeto/objeto.php?opc=4"

df = pd.DataFrame(columns=('id', 'tipo', 'id_p', 'estado', 'cantidad', 'tamanio', 'modulo'))

estado = {'Bueno' : '0', 'Malo' : '1', 'Regular': '2', '': '2'}
cantidad = {'1' : '0', '2' : '1', '3 o mas': '2', '': '2'}
size = {'Chico' : '0', 'Mediano' : '1', 'Grande': '2', '': '2'}
modulo = {'X' : '0', 'P' : '1', 'Otro' : '2', '' : '2'}
valores = []

response = urllib.request.urlopen(getUrl)
content = response.read()

data = json.loads(content.decode("utf-8"))
dict2 = dict(data['objeto'])
ids = dict2.keys()


print ("\n\n")
for clave in dict2.keys(): #Obtenemos la clave de cada diccionario
    for item, valor in dict2[clave].items():
        if item == "id" or item == "propietario_id" or item == "tipoObjeto":
            valores.append(valor)
        elif item == "estado":
            valores.append(estado[valor])
        elif item == "cantidad":
            valores.append(cantidad[valor])
        elif item == "tamanio":
            valores.append(size[valor])
        elif item == "modulo":
            valores.append(modulo[valor])
    df.loc[len(df)] = valores
    valores.clear()

df.to_csv('src/data.csv')
