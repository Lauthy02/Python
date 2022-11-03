'''
1- Crear un programa en Python, que permita ingresar 20 números distintos de cero. Cuando el 
usuario ingresa un cero el programa termina y muestra la suma de todos los valores ingresados 
y el promedio de los números pares.
'''
#import Librerias.Funciones as Lib


def main():
    Numero = 1
    ListaDeNumeros = []
    ValorTotPares = 0
    ContadorDePares = 0
    SumaGeneral = 0
    Cont = 0
    # Lib.LimpiaConsola()
    print("Si desea dejar de ingresar números digite 0.")

    while (Numero != 0 and Cont <= 20):
        Numero = int(input(f"Ingrese el número [{Cont}]: "))
        if (Numero != 0):
            ListaDeNumeros.append(Numero)
            SumaGeneral = SumaGeneral + Numero
            if (Numero % 2 == 0):
                ContadorDePares = ContadorDePares + 1
                ValorTotPares = ValorTotPares + Numero
            Cont = Cont + 1

    print()
    print("La cantidad de los números pares es: ", ContadorDePares)
    print("La suma de todos los números pares es: ", ValorTotPares)
    print("El promedio de los numeros pares es: ",
          ValorTotPares/ContadorDePares)
    print("La suma de todos los números es: ", SumaGeneral)
    input()


if __name__ == "__main__":
    main()
