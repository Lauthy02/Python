'''
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
import random as rnd

def DiferenciaPorcentual(NroNuevo,NroViejo):
    DifPor = (((NroNuevo/NroViejo)*100)-100)
    return DifPor

def main():
    Salir = False
    while(Salir == False):
        os.system("cls")
        print("###################### ")
        print("    1- Estadística")
        print("    2- Salir ")
        print("####################### ")
        opcion = int(input("Seleccione una opción > "))

        if(opcion == 1):
            os.system("cls")
            print("---Usted entró al punto 1---")
            print()

            ListaValores = []
            CantidadDeValores = 100
            for i in range(CantidadDeValores):
                ListaValores.append(rnd.randrange(0, 100))
            
            SumaTotal = 0
            Promedio = 0
            for a in range(CantidadDeValores):
                SumaTotal = SumaTotal + ListaValores[a]
            Promedio = SumaTotal/CantidadDeValores

            TuplaValores = tuple(ListaValores)
            LargoTupla = (len(TuplaValores)-1)

            if(TuplaValores[0] < TuplaValores[LargoTupla]):
                print("El precio está en alza")
            elif(TuplaValores[0] > TuplaValores[LargoTupla]):
                print("El precio está en baja")
            else:
                print("El precio se mantuvo")
                
            print(f"El primer valor de la tupla es: {TuplaValores[0]}")
            print(f"El ultimo valor de la tupla es: {TuplaValores[LargoTupla]}")
            print("La diferencia en porcentaje es: %0.2f" %(DiferenciaPorcentual(TuplaValores[LargoTupla], TuplaValores[0])))
            print(f"La suma total de los valores es: {SumaTotal}")
            print(f"El promedio de todos los valores es: {Promedio}")
            print(f"El valor mas pequeño es: {min(TuplaValores)}")
            input()
        elif(opcion == 2):
            print()
            print("---Usted eligió salir---")
            Salir = True
        else:
            print()
            print("---No puso ningún valor válido---")
            input()
    print()
    print("Fin")
   '''
   Holaaaa
   '''     

if(__name__=="__main__"):
    main()