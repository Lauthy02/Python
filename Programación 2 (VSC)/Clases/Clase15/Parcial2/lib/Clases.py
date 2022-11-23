'''
---- 2do Parcial de Programación 2 (Python) ----
Alumno: Rojas Lautaro
Fecha: 23/11/2022
Tema 1
Localizacón: Centro (San Juan)

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

Notas: 
    1. Entiendo "cantidad" como saldo de la cuenta
    2. Entiendo "bonificación" al descuento que se le aplica al mantenimiento de la cuenta
        El costo del mantenimiento de la cuenta es un monto fijo
'''
class Cliente:
    #Atributos
    _nombre = None
    _edad = None
    _CJ = None

    #Getters y setters
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, value):
        self._nombre = value
    nomb = property(get_nombre,set_nombre)

    def get_edad(self):
        return self._edad
    def set_edad(self, value):
        self._edad = value
    edad = property(get_edad,set_edad)

    def getCJ(self):
        return self._CJ
    def setCJ(self, value):
        self._CJ = value
    ctajoven = property(getCJ,setCJ)

class Cuenta:
    #Atributos
    _titular = None    
    _saldo = None
    _cost_manten = None

    #Constructor
    def __init__(self):
        self._cost_manten = 12000

    #getters y setters
    def get_titular(self):
        return self._titular
    def set_titular(self, value):
        self._titular = value
    titular = property(get_titular,set_titular)

    def get_saldo(self):
        return self._saldo
    def set_saldo(self, value):
        self._saldo = value
    saldo = property(get_saldo,set_saldo)

    #Métodos
    def retirarDinero(self, importe):
        self._saldo -= importe

    def ingresarDinero(self, importe):
        self._saldo += importe

    def esTitularValido(self, edad):
        Ok = False
        if(edad > 18 and edad < 25):
            Ok = True
        return Ok

    def mostrar(self):
        print(f"El titular es: {self.titular}")
        print(f"El saldo es: {self.saldo} ARS")
        print(f"El mantenimiento de la cuenta es de: {self._cost_manten} ARS")

class CuentaJoven(Cuenta):
    #Atributos
    _bonific = None
    
    #Getter y setter
    def getBonific(self):
        return self._bonific
    def setBonific(self, value):
        self._bonific = value
    Bonificacion = property(getBonific, setBonific)

    #Métodos
    def retirarDinero(self, importe, edad):
        if(super().esTitularValido(edad)):
            print("AVISO: Operacion retirar dinero realizada con exito")
            super().retirarDinero(importe)
        else:
            print("ADVERTENCIA: No puede retirar dinero")

    def ingresarDinero(self, importe, edad):
        if(super().esTitularValido(edad)):
            print("AVISO: Operacion ingresar dinero realizada con exito")
            super().ingresarDinero(importe)
        else:
            print("ADVERTENCIA: No puede ingresar dinero")
    
    def aplicarBonific(self, bon, edad):
        if(super().esTitularValido(edad)):
            print("AVISO: Operacion aplicar bonificacion realizada con exito")
            aux = bon/100
            self._cost_manten -= self._cost_manten * aux
        else:
            print("ADVERTENCIA: No se puede aplicar bonificacion")
        
    def mostrar(self):
        print(f"Esta es la Cuenta Joven con una bonificación de: {self.Bonificacion} porciento")
        super().mostrar()