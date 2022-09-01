'''
Listas
3 tipo de elementos 
    tuplas: es inmutable, es como una constante, le asigno valores a los nodos de la tupla y desp no los puedo cambiar, el caracter q representa la tupla son los ()
    listas: las modifico libremente, el caracter q la representa es el []
    diccionarios: en cada nodo tiene una dupla de clave y valor y los caracteres q lo representa son las {}, es como una matriz
las 3 son cadenas de nodos q tienen valores

tipo de dato simple
    int
    float
    string
    bool

Tipo de dato complejo

'''

import os  # Importa una librería
import math
import datetime


def main():

    tupla = (1, 2, 3)
    print(tupla[0])

    tupla = (1, (1, 2, 3), 3)  # tupla dentro de una tupla
    print(tupla[1][0])

    tupla = (1, "Hola", True)
    Num, MSH, VF = tupla  # Le asigno nombre a cada valor de la tupla
    for i in tupla:
        print(i)
    print(type(tupla))
    # Devuelve la cantidad de nodos q tiene la tupla, 1 nodo es 1 valor dentro de la tupla
    print(len(tupla))
    tupla = (1)  # No lo reconoce como tupla
    tupla = (1,)  # Lo reconoce como tupla

    lista[1, 2, 3]
    lista[0] = 699
    print(type(lista))
    print(lista)  # Imprime todos los valores de la lista
    # agregar
    lista.append(4)  # me agrega un nodo mas
    # insertar
    lista.insert(1, 50)  # agrega el valor 50 en la posición 1
    # eliminar
    lista.remove(50)  # Me elimina el primero q encuentra q sola vez
    # ordena al revés
    lista.reverse()
    # ordena la lista
    lista.sort(reverse=True)  # ordena de menor a mayor
    # el pop sempre me borra el ultimo de la lista, y si pongo el pop dentro del insert, me devuelve el valor q va a borrar
    lista.pop()
    print(lista)
    print("Ejecutar pop: ", lista.pop())
    print(lista)
    lista.pop(0)  # adentro del pop le podes decir q posición querés borrar
    # devuelve cuantos 50 tengo en la lista
    print("Tengo una cantidad de 50", lista.count(50))
    # me da la posición del primero q encuentra
    print("Donde está el 50", lista.index(50))
    # desordenar los elementos de la lista
    import random
    random.shuffle(lista)
    print(lista)
    #cambia el tipo de datos
    tupla2 = tuple(lista)
    print("Mostrar tupla2:", type(tupla2), tupla2)

    diccionario={1:"uno",2:"dos",3:"tres",4:"cuatro",5:True,6:600}
    print(dic[1])
    for i in diccionario:
        print(i)
    for i in diccionario.values():
        print(i)
    #el len también se puede usar en el diccionario
    
if __name__ == "__main__":
    main()
