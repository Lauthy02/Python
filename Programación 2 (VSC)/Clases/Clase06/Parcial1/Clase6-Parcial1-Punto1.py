'''
1- Crear  un  programa  que  permita  cargar  por  teclado,  una  cantidad  de  valores  enteros,  pero 
asegurando que los valores cargados por el usuario desde el teclado sean siempre positivos. 
La carga termina al poner un cero, y luego de terminar la carga el sistema muestra los valores 
en pantalla. 

'''
import os
import math

def main():
    os.system("cls")
    ListaDeNumeros = []
    Numero = 1
    Cont = 1
    print("Si desea dejar de ingresar números digite 0.")

    while (Numero != 0):
        Numero = int(input(f"Ingrese el número [{Cont}]: "))
        if (Numero != 0 and Numero > 0):
            ListaDeNumeros.append(Numero)
            Cont = Cont + 1
        elif(Numero == 0):
            print()
            print("Finaliza el ingreso de números.")
        else:
            print()
            print("El numero ingresado no es mayor a 0.")

    
    print(f"La lista está conformada por los números: {ListaDeNumeros} :-)")
    input()



if(__name__=="__main__"):
    main()