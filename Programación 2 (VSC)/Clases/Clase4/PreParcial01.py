'''
Permita llenar un diccionario con valores entre 0 y 2000. El proyecto deberá tener una función para llenar el diccionario y otra que devuelva el dato cargado segúnuna key que se pasa como argumento.
'''
import random as rnd

diccionario={}

def llenarDic():
    for i in range(2000):
        dic[i]=rnd.randrange(0,2000)

def mostrarNodo(key):
    print(diccionario[key])


def main():
    llenarDic()
    mostrarNodo(3)


if __name__=="__main__":
    main()
