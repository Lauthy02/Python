'''
Crear una clase Tablero que puede dibujar, dada una pala-
bra, un conjunto de caracteres “_”. Donde cada “_” es una letra. 
La clase, cuando presento una letra me dice si existe o no. Si la 
letra existe, informa la posición. Si no existe, devuelve -1. Da-
da una letra que existe, la coloca en la posición real. La clase, 
me permite cargar la palabra del juego. Tiene un constructor 
que inicializa el tablero.
'''
import random as rnd

class Tablero:
    _palabras = ["cielo","mar","ciudad"]
    _palabra_oculta = []
    _palabra_actual = []

    def __init__(self):
        indice=rnd.randint(0, 2)
        palabra = self._palabras[indice]
        cont = 0
        for i in palabra:
            self._palabra_actual[cont] = i
            self._palabra_oculta[cont] = '_'
            cont += 1


    def generarPalabraOculta(self):
        pass

    def dibujarTablero(self):
        for i in self._palabra_oculta:
            print(i, end = "")

    def existeLetra(self, letra):
        existe = -1
        cont = 0
        for i in self._palabra_actual:
            if i == letra:
                self._palabra_oculta[cont] = letra
                existe = 1
            cont += 1
        return existe
