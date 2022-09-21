
#Como importar funciones de otra librería 
import Librerias.Funciones
#También se puede escribir de la siguiente manera
import Librerias.Funciones as Lib
#Para traer 1 sola función y no toda la librería 
from Librerias.Funciones import LimpiaConsola
from multipledispatch import dispatch


def main():
    Librerias.Funciones.LimpiaConsola()
    Lib.LimpiaConsola()
    print(SumarPlus(2, 2))

#Hay funciones q no devuelven valores y que no reciban parámetros  
def Saludar():
    print("Vamos bokita")

#Hay funciones q no devuelven valores y que si reciban parámetros 
def Sumar(a,b,):
    print(a+b)

#Hay funciones q si devuelven valores y que si reciban parámetros 
def SumarPlus(a,b,):
    sumar=a+b
    return sumar

#Hay funciones recursivas 
def Recursiva(a):
    if(a==0):
        return a
    Recursiva(a-1)

#sumular sobrecarga
@dispatch()
def saludar(): #Acá entra cuando escribimos saludar()
    print("Hola hola")
@dispatch(str) #Acá entra cuando escribimos saludar("Holaaaa")
def saludar(a):
    print(a) 


if __name__=="__main__":
    main()
