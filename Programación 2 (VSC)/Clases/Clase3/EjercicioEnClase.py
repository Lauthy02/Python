'''
Teniendo una cantiadad de números enteros que se ingresan por teclado mayores a 0, informar:
    La suma de todos
    El promedio 
    Y cuál es el mayor número ingresado
Los números cargados por teclado terminan cuando se ingresa un 0
'''
import os #Importa una librería 
import math
import datetime

def main():
    os.system("cls")
    promedio = 0
    contador = 0
    maximo = 0
    suma = 0
    valor = -1
    valor = int(input("Ingrese un valor mayor a 0: "))
    suma += valor
    maximo=valor
    contador+=1
    while(valor!=0):
        valor = int(input("Ingrese un valor mayor a 0: "))
        suma += valor 
        if(valor != 0):
            contador+=1
        if(valor>max):
            maximo=valor 

print(f"La suma de todos los valores es: {suma}")
promedio = suma/contador
print("El promedio de los valores es: %06.2f" % promedio)
print(f"El valor maximo fue {maximo}")


if __name__=="__main__":
    main()
