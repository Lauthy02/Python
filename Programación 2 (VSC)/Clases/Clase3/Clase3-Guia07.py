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
    '''
    1- Crear un programa que muestre todos los números entre 1 y 10
    '''
    print("Punto 1")
    for i in range(1,11):
        print(i)
    
    '''
    2- Crear un programar que muestre sólo los números pares entre el 0 y el 10
    '''
    print("Punto 2 - propuesta 2")
    os.system("cls") 
    for i in range(0,11): 
        if i/2==int(i/2): 
            print(i)

    '''
    3- Crear  un  programa,  que  permita  mostrar  números  enteros  distintos  de  cero,  
    al ingresar cero el programa termina y muestra un mensaje de fin
    '''
    os.system("cls") 
    valor=int(input("Ingresar un valor, o cero para terminar : ")) 
    
    while valor!=0: 
            print(valor) 
            valor=int(input("Ingresar un valor, o cero para terminar : ")) 
    print("fin") 

    '''
    4- Crear un programa que muestra el siguiente menú:
        ###################### 
        1- Abrir 
        2- Listar 
        3- Salir 
        ####################### 
        Seleccione una opción >
    '''
    import os 
    os.system("cls") 
    salir=False 
    
    while not salir: 
            print("#################") 
            print("1- Abrir") 
            print("2- Listar") 
            print("3- Salir") 
            print("#################") 
            valor=int(input("Ingresar un valor del 1 al 3 : ")) 
    
            if valor==3: 
                salir=True 
            elif valor==1: 
                print ("abrir") 
                print ("presione una tecla para seguir") 
                input() 
                os.system("cls") 
            elif valor==2: 
                print ("Listar") 
                print ("presione una tecla para seguir") 
                input() 
                os.system("cls") 
    print("fin") 

if __name__=="__main__":
    main()