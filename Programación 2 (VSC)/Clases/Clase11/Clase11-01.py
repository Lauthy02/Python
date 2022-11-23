'''
Clase 11 27/10/2022
 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

lista = [12,232,13,54]
serie = pd.Series(lista)
print(serie)

dicc = {'id':[1,2,3,4],'nombre':['Ana','Pepe','Santi','Lolo'],'genero':['F','M','M','M'],'edad':[54,23,12,67]}
tabla = pd.DataFrame(dicc)
print(tabla)

mayA30 = pd.Series(tabla['edad'] > 30)
print(mayA30)

cuantas = pd.Series(tabla['genero'].value_counts())
serie = pd.DataFrame(cuantas)
print(serie)
