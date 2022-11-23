'''
Clase 9 13/10/2022
debo construir métodos para modificar los datos de las variables
Los constructores no se heredan  
'''
import os

class Persona:
    _nombre = None
    _edad = None
    
    #constructor
    def __init__():
        pass
    
    #destructor

    #getter y setter
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, value):
        self._nombre = value
    nombre = property(get_nombre, set_nombre)
    
    def calc_edad():
        return 20

class Operador(Persona):
    def __init__():
        super().__init__()
    
    def calc_edad():
        super().calc_edad

def main():
    os.system("cls")

    p=Persona()
    p.nombre = "juan"
    print(p.nombre)

    o=Operador()
    o.nombre = "pepe"



if(__name__=="__main__"):
    main()