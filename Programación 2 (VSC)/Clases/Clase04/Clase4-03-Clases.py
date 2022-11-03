
# Se pueden crear objetos/clases
# podemos manejar dentro de python el:
# estado: propiedades estaticas y valores dinamicos
# comportamiento: no puedo tener métodos q estén vacios, siempre tiene q tener parametros y como minimo el parametro q tiene q tener es (self).
# en python no existen las cosas privadas, es todo público
class Persona:
    # estado/propiedades
    Nombre = None
    Edad = 0
    FechaNacimiento
    # comportamiento/métodos

    def __init__(self, nomb, fechNac):  # Esto es el constructor, siempre es así
        self.Nombre = nomb
        self.FechaNacimiento = fechNac

    def __del__(self):  # Esto es el destructor, siempre es así
        pass

    def setNombre(self, value):  # el value sirve para escribir Pers.setNombre("Juan"). value es una variable, no tiene q llamarse value si o si
        Nombre = value

    def setApellido(self, Ape):
        Apellido = Ape

    def calcularEdad(self):  # No me hace falta el value porque no tiene ningún valor de entrada
        return 45


def main():
    Pers = Persona()
    Pers.setNombre("Juan")
    Pers.setApellido("Perez")
    Pers2 = Persona("Angela", "19-02-2002")


if __name__ == "__main__":
    main()
