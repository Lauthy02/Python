'''
Grupo 2
'''
import os #Importa una librería 
import math
import Librerias.Funciones as miFuncion
import Librerias.Funciones.SUMAR as S
import Librerias.Funciones.LimpiaConsola as LC
#con import traigo la libreria entera
#con from traigo una funcion especifica 

def main():
    os.system("cls") #Limpia la consola
    miFuncion.SUMAR(2, 3)
    S(6,7)
    #----------- punto 1 -------------------
    #Declarar 2 cariables y mostrar la suma
    print("-----------Punto 1-----------")
    Var1 = 10
    Var2 = 2
    print(f"Hola, el numero es: {Var1+Var2}")

    #----------- punto 2 -------------------
    #
    print("-----------Punto 2-----------")
    Var3 = 10
    Var3 += 1 
    print(f"El valor final es: {Var3}")

    #----------- punto 3 -------------------
    # Ingresar cadena por teclado 
    LC()
    print("-----------Punto 3-----------")
    Cadena = input("Ingrese cadena: ")
    print()
    print(f"La cadena q ingresó es: {Cadena}")

    #----------- punto 4 -------------------
    # Ingresar valor por teclado y mostrar el 25%
    print("-----------Punto 4-----------")
    Var4 = input("Ingrese el valor: ")
    print(f"El 25% de {Var4} es: {float(Var4)*0.25} ")

    #----------- punto 5 -------------------
    # Ingresar int en una variable temperatura
    # y localidad y mostar
    print("-----------Punto 5-----------")
    Temp = int(input("Ingrese la temperatura: "))
    Localidad = input("Ingrese la localidad: ")
    print("En la zona de %s tenemos una temperatura de %d" %(Localidad,Temp))

    #----------- punto 6 -------------------
    # 
    # 
    print("-----------Punto 6-----------")


    input() #La consola espera a q toque una tecla para finalizar la ejecución



if (__name__=="__main__"):{
    main()
}