'''
Autor:
Fecha:
Descripcion:
'''
import os #Importa una librería 
import math
import datetime

def main():
    print("Recorre letras")
    for i in 'aieou': #
        print(i)

    print("Recorre colección de números")
    for i in range(5): #range() crea una colección de 5 numeros, va de 0 a 4
        print(i)

    print("For para adelante")
    # int i=0; i<5; i++    
    for i in range(0,5): #indico el inicio de la colección, final de la colección
        print(i)

    print("For para atrás")
    # int i=0; i>5; i--    
    for i in range(5,0,-1): #(indico el inicio de la colección, final de la colección, y el sentido)
        print(i)





if __name__=="__main__":
    main()
