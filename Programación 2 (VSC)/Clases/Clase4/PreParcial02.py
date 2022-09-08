'''
Permita llenar una tupla de python con valores enteros impares entre 0 y 1000. La acción de llenar debe implementarse en una función debe tener un argumneto de entrada y como valor de retorno la misma tupla

La tupla no es dinámica, no puedo tener una funcion q le pase cosas a la tupla. pero si puedo tener una lista y la lista la paso a tupla
'''
def generarTupla():
    lista=[]
    for i in range(1,1000,2):
        lista.append(i)
    return tuple(lista)


def main():
    pass
    


if __name__=="__main__":
    main()
