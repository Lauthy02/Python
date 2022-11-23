'''
https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

'''
Al ejecutar esto es normal que me salga un error de archivo no encontrado
Cuando pasa eso debo dirigir la ruta en la consola donde está el ejecutable con el archivo a leer 
'''

DatosExcel = pd.read_csv('Libro1.csv')

'''
las x y las y deben tener el mismo nombre que en la tabla del csv que estoy leyendo
'''

DatosExcel.plot(kind='scatter',x='producto',y='precio',title='costos por producto',figsize=(5,5),xlabel='productos',ylabel='pesos',legend=False)
mp.show()
