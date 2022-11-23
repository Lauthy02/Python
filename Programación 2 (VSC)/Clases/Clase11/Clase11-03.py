import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

dicc = {'id':[1,2,3,4],'nombre':['Ana','Pepe','Santi','Lolo'],'genero':['F','M','M','M'],'edad':[54,23,12,67]}
df = pd.DataFrame(dicc)

serie = pd.Series(df['genero'].value_counts())
df = pd.DataFrame(serie)

'''
mp.pie(df['genero'], labels=df.index,autopct='%0.1f%%')
mp.title('cantidad por genero')
mp.show()
'''