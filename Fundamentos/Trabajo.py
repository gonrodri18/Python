#%%
# importing csv module 
import csv, operator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename1 = "/Users/gonzalo/Desktop/Fundamentos/datos2019.csv"
filename2 = '/Users/gonzalo/Desktop/Fundamentos/datos2018.csv'
  
# initializing the titles and rows list 
fields = [] 
data_2018 = []
data_2019 = []
  
with open(filename1) as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        a = reg[0].split(';')
        data_2019.append(a)  # Cada línea se muestra como una lista de campos
with open(filename2) as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        a = reg[0].split(';')
        data_2018.append(a)  # Cada línea se muestra como una lista de campos

fields = data_2018[0]
data_2018=data_2018[1:]
data_2019=data_2019[1:]
#traspaso de datos (no es nigun ejercicio)

#ejercicio 1
def med_estacion(estacion,magnitud):
    estacion = str(estacion)
    magnitud = str(magnitud)
    lista = []

    for i in data_2018:
        if i[2] == estacion and i[3] == magnitud:
            lista.append(i[7:])

    for i in data_2019:
        if i[2] == estacion and i[3] == magnitud:
            lista.append(i[7:])

    # Este ultimo bucle transforma las str en numeros para su mejor manejo
    # a la hora de hacer operaciones
    for i in lista:
        for j in range(len(i)):
            if j % 2 == 0:
                i[j] = float(i[j])
    return lista

#ejercicio 1 


#ejercicio 2
def media1_estacion(estacion,mes,ano):
    lista = []
    if ano == 2018:
        for i in data_2018:
            if int(i[2]) == estacion and int(i[6]) == mes:
                lista.append([i[3]]+i[7:])
    else:
        for i in data_2019:
            if int(i[2]) == estacion and int(i[6]) == mes:
                lista.append([i[3]]+i[7:])

    d = {}
    for i in lista:
        m = 0
        c = 0
        for j in range(len(i) - 2):
            if j % 2 == 0 and i[j+2] != 'N':
                m = m + float(i[j+1])
                c = c+1
        print(m)
        med = m/c

        d[i[0]] = med
    return d

#ejercicio 2

