'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de 
la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación 
que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase  
    1.  Un constructor.  
    2.  Los setters y getters para el nuevo atributo.  
    3.  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que 
    crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 
    25 años y falso encaso contrario.  
    4.  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.  
    5.  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.  
    6.  Piensa los métodos heredados de la clase madre que hay que reescribir
'''
class Cuenta:
    _titular = None
    _cantidad = None

    def esTitularValido():
        pass

    def retirarDinero():
        pass

    def mostrar():
        pass


class CuentaJoven(Cuenta):
    #Atributos
    _bonific = None

    #Constructor
    def __init__(self):
        pass

    #Getter y setter
    def getBonific(self):
        return self._bonific

    def setBonific(self, value):
        self._bonific = value
    Bonificacion = property(getBonific, setBonific)

    #Métodos
    def esTitularValido():
        pass

    def retirarDinero():
        pass

    def mostrar():
        pass
