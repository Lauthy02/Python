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
    ejerecicio = 0
    print("-----------Punto 1-----------")
    print("-----------Punto 2-----------")
    print("-----------Punto 3-----------")
    print("-----------Punto 4-----------")
    print("-----------Punto 5-----------")
    print("-----------Punto 6-----------")
    print("-----------Punto 7-----------")
    print("-----------Punto 8-----------")
    print("-----------Punto 9-----------")
    print("-----------Punto 10-----------")
    print("-----------Punto 11-----------")
    print("-----------Punto 12-----------")
    print("-----------Punto 13-----------")
    ejerecicio = int(input("Ingrese a que ejerecicio decide entrar: "))
    
    if(ejerecicio==1):
        #Declarar 2 cariables y mostrar la suma
        os.system("cls") #Limpia la consola
        print("-----------Punto 1-----------")
        Var1 = 10
        Var2 = 2
        print(f"Hola, el numero es: {Var1+Var2}")
        input() #La consola espera a q toque una tecla para finalizar la ejecución
    
    elif(ejerecicio==2):
        #Dada una variable entera, sumarle 1 en una línea diferente y mostrar el resultado en pantalla.
        os.system("cls")
        print("-----------Punto 2-----------")
        Var3 = 10
        Var3 += 1 
        print(f"El valor final es: {Var3}")
        input()
    
    elif(ejerecicio==3):
        # Ingresar cadena por teclado 
        os.system("cls")
        print("-----------Punto 3-----------")
        Cadena = input("Ingrese cadena: ")
        print()
        print(f"La cadena q ingresó es: {Cadena}")
        input()
    
    elif(ejerecicio==4):
        # Ingresar valor por teclado y mostrar el 25%
        os.system("cls")
        print("-----------Punto 4-----------")
        Var4 = input("Ingrese el valor: ")
        print(f"El 25% de {Var4} es: {float(Var4)*0.25} ")
        input()
    
    elif(ejerecicio==5):
        # Ingresar int en una variable temperatura y localidad y mostar
        os.system("cls")
        print("-----------Punto 5-----------")
        Temp = int(input("Ingrese la temperatura: "))
        Localidad = input("Ingrese la localidad: ")
        print("En la zona de %s tenemos una temperatura de %d" %(Localidad,Temp))
        input()
    
    elif(ejerecicio==6):
        # Dados los lados de un cuadrado, mostrar en pantalla el valor de su superficie
        os.system("cls")
        print("-----------Punto 6-----------")


        input()

    elif(ejerecicio==7):
        #Copiar y ejecutar el siguiente código, justifique la salida que se obtiene por pantalla
        os.system("cls")
        print("-----------Punto 7-----------")
        numero1,numero2=0,0 
        
        numero1=int(input("Ingresar un numero : ")) 
        numero2=int(input("Ingresar un numero : ")) 
        
        if numero1 > numero2: 
            print(f"{numero1} es mayor a {numero2}") 
        else: 
            if numero2 > numero1: 
                print(f"{numero2} es mayor a {numero1}") 
            else: 
                print(f"{numero2} es igual  a {numero1}") 
        print()
        print("Los números siguen una secuencia de condiciones para q la salida sea correcta.")
        print("Primero entra en un if preguntando si N1 es mayor a N2, si si N1 es mayor, si no,")
        print("pregunta si N2 es mayor a N1, si si N2 es mayo pero si no, son iguales")
        input()

    elif(ejerecicio==8):
        #Implementar un algoritmo en Python que, dados dos valores de las acciones de 
        # la empresa Techint del día 23-8-2022 y otra del día 22-8-2022 permita informar 
        # si las acciones están el alza.
        # ingresar valores para las distintas fechas.
        os.system("cls")
        print("-----------Punto 8-----------")
        numero1,numero2=0,0 
        
        numero1=int(input("Ingresar el valor de las acciones del día 22-8-2022: ")) 
        numero2=int(input("Ingresar el valor de las acciones del día 23-8-2022: ")) 
        
        if numero1 > numero2: 
            print(f"{numero1} es mayor a {numero2}, por lo tanto, bajó el valor") 
        else: 
            if numero2 > numero1: 
                print(f"{numero2} es mayor a {numero1}, por lo tanto, aumentó el valor") 
            else: 
                print(f"{numero2} es igual  a {numero1}, por lo tanto, el valor se mantuvo") 
        input()
    
    elif(ejerecicio==9):
        os.system("cls")
        print("-----------Punto 9-----------")
        input()
    
    elif(ejerecicio==10):
        os.system("cls")
        print("-----------Punto 10-----------")
        input()
    
    elif(ejerecicio==11):
        os.system("cls")
        print("-----------Punto 11-----------")
        input()
        
    elif(ejerecicio==12):
        os.system("cls")
        print("-----------Punto 12-----------")
        input()

    elif(ejerecicio==13):
        os.system("cls")
        print("-----------Punto 13-----------")
        input()

    else:
        os.system("cls")
        print("No seleccionó ningún ejercicio.")
        input()     
    
if (__name__=="__main__"):{
    main()
}