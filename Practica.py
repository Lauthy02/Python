'''
1- Crear  un  programa  que  permita  cargar  por  teclado,  una  cantidad  de  valores  enteros,  pero 
asegurando que los valores cargados por el usuario desde el teclado sean siempre positivos. 
La carga termina al poner un cero, y luego de terminar la carga el sistema muestra los valores 
en pantalla. 

2- Crear un programa, Que permita cargar una lista con 100 valores positivos, y que al ejecutarse 
muestra el siguiente menú: 
    ###################### 
    1- Estadística 
    2- Salir 
    ####################### 
    Seleccione una opción > 
Al presionar 1, muestre: 
    a. si los valores de la secuencia están en aumento 
    b. La diferencia del último valor con el primero expresado en porcentaje 
    c. El promedio de todos los valores 
    d. El valor más pequeño de la lista 
 
Con 2 saldrá del programa y mostrará el mensaje “fin”. El programa no terminará si el 
usuario no selecciona el 2.
'''
import os
import math
import random as rnd

def main():
    Ejercicio = 1
    os.system("cls")
    while(Ejercicio != 0):
        print("----Final de programación 2----")
        print("----Menu----")
        print("Escriba [1] para el Ejercicio 1")
        print("Escriba [2] para el Ejercicio 2")
        print("Escriba [0] para salir")
        print("-------------------------------")
        Ejercicio = int(input("¿Que número elije? "))
        if(Ejercicio == 0):
            os.system("cls")
            print("--Saliendo--")
            input()
        elif(Ejercicio == 1):
                os.system("cls")
                print("--Ejercicio 1--")

                NumIngresado = 1
                cont = 0
                ListaDeNumeros = []

                while(NumIngresado != 0):
                    NumIngresado = int(input(f"Ingrese el numero [{cont}]: "))
                    if(NumIngresado > 0):
                        ListaDeNumeros.append(NumIngresado)
                        cont = cont + 1 
                    elif(NumIngresado < 0):
                        print("No se pueden ingresar numeros negativos")
                    else:
                        print("Ingreso de números finalizado")
                
                print(f"La lista está conformada por los números: {ListaDeNumeros} :-)")
                input()
                os.system("cls")

        elif(Ejercicio == 2):
                os.system("cls")
                print("--Ejercicio 2--")

                Opcion = 0

                print("######################") 
                print("1- Estadística")
                print("2- Salir") 
                print("######################")
                Opcion = int(input("Seleccione una opción >"))

                while(Opcion != 2):
                    if(Opcion == 1):
                        os.system("cls")
                        
                        ListaDeValores = []
                        CantidadDeValores = 100
                        for i in range(CantidadDeValores):
                            ListaDeValores.append(rnd.randrange(0,100))
                        
                        input()
                        os.system("cls")
                    elif(Opcion == 2):
                        os.system("cls")
                        print("Saliendo")
                        input()
                        os.system("cls")
                    else:
                        os.system("cls")
                        print("Valor no valido. :-(")
                        input()
                        os.system("cls")
                input()
                os.system("cls")
        else:
            os.system("cls")
            print("Valor no valido. :-(")
            input()
            os.system("cls")

if(__name__=="__main__"):
    main()