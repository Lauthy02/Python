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
    os.system("cls")
    TuplaPrecios = (30,20,10,20,25,50,40)
    LargoDeTupla = (len(TuplaPrecios)-1)

    print(type(LargoDeTupla))
    print(LargoDeTupla)

    print(TuplaPrecios[0])
    print(TuplaPrecios[LargoDeTupla])

    if(TuplaPrecios[0] < TuplaPrecios[LargoDeTupla]):
        print("El precio está en alza")
        print(f"La diferencia porcentual es: {DiferenciaPorcentual(TuplaPrecios[LargoDeTupla],TuplaPrecios[0])}")
    elif(TuplaPrecios[0] > TuplaPrecios[LargoDeTupla]):
        print("El precio está en baja")
        DifPor2 = (((TuplaPrecios[LargoDeTupla]/TuplaPrecios[0])*100)-100)
        print("La diferencia porcentual es: %0.2f" %(DifPor2))
    else:
        print("El precio se mantuvo")
    print(f"El precio máximo del producto --PILUSOS DE BOKITA-- fué de: {max(TuplaPrecios)}")
    input()
    
if __name__=="__main__":
    main()