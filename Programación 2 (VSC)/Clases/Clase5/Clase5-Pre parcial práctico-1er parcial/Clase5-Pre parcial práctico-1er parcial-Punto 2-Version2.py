'''
Desarrollar un programa que permita informar el comportamiento de los precios de un 
producto. Los precios del último mes se encuentran cargados en una lista secuencialmente día 
por día. Se debe informar: 
a. 1- si los precios están en aumento 
b. 2- La diferencia del último precio con el primero expresado en porcentaje 
c. 3- El nombre del producto y el precio más alto en ese mes 
'''
import os

def DiferenciaPorcentual(NroNuevo,NroViejo):
    DifPor = (((NroNuevo/NroViejo)*100)-100)
    return DifPor

def main():

    ListaDePrecios = []
    NombreProd = input("Ingrese el nombre del producto: ")
    CantVentas = int(input(f"Ingrese la cantidad de ventas en el mes del producto {NombreProd}: "))
    
    for i in range (CantVentas):
        ListaDePrecios.append(int(input(f"Ingrese el precio {i}: ")))
    
    Diferencia = DiferenciaPorcentual(ListaDePrecios[CantVentas-1], ListaDePrecios[0])

    if(ListaDePrecios[0] < ListaDePrecios[CantVentas-1]):
        print("El precio está en alza")
        print("La diferencia en porcentaje es: %0.2f" %(Diferencia))
    elif(ListaDePrecios[0] > ListaDePrecios[CantVentas-1]):
        print("El precio está en baja")
        print("La diferencia en porcentaje es: %0.2f" %(Diferencia))
    else:
        print("El precio se mantuvo")
        print("La diferencia en porcentaje es: %0.2f" %(Diferencia))
    
    print(f"El precio máximo del producto {NombreProd} fué de: {max(ListaDePrecios)}")
    input()


if(__name__=="__main__"):
    main()