'''
Crear el personaje Bumba, tiene un color, una posición en el plano de 2 coordenadas que se pueden leer y escribir.
Un valor de salto privado medido en una unidad de salto
'''

class Bumba:
    _color = None
    _x = None
    _y = None
    _salto = None

    #constructor
    def __init__(self):
        self._color = "Rojo"
        self._x = 0
        self._y = 0
        self._salto = 1

    def get_x(self):
        return self._x
    def set_x(self, value):
        self._x = value
    X = property(get_x,set_x)

    def get_y(self):
        return self._y
    def set_y(self, value):
        self._y = value
    Y = property(get_y,set_y)