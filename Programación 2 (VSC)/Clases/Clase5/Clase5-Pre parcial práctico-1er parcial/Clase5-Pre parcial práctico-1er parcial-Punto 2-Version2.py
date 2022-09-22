'''
Desarrollar un programa que permita informar el comportamiento de los precios de un 
producto. Los precios del último mes se encuentran cargados en una lista secuencialmente día 
por día. Se debe informar: 
a. 1- si los precios están en aumento 
b. 2- La diferencia del último precio con el primero expresado en porcentaje 
c. 3- El nombre del producto y el precio más alto en ese mes 
'''
import os

def main():

    ListaDePrecios = []
    os.system(cls)
    NombreProd = input("Ingrese el nombre del producto: ")
    CantVentas = input(f"Ingrese la cantidad de ventas en el mes del producto {NombreProd}: ")
    for i in range (CantVentas):
        ListaDePrecios.append(input(f"Ingrese el precio {i}: "))
    




if(__name__=="__main__"):
    main()