'''
Clase 8 06/10/2022
Un conjunto, un set: Se declara como diccionario y tiene caracteristicas de la tupla 
El tipo de dato set no toma valores repetidos
'''
import math
from math import sqrt
import math as mate
import os 
from datetime import datetime

def main():
    os.system("cls")

    conjunto={1,2,3,4}
    print(type(conjunto))

    conjunto={1,2,3,4,1,2,3,7}
    print(conjunto)
    for i in conjunto:
        print(i)
    
    for i in 'PalabraLarga':
        print(i, sep="-")

    date_time_string = '06/10/22 01:55:19'
    date_time_obj = datetime.strptime(date_time_string, '%d/%m/%y %H:%M:%S')

if(__name__=="__main__"):
    main()