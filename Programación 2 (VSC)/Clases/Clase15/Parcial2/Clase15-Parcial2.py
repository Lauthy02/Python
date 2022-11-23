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
import os
import lib.Clases as clas

def main():
    os.system("cls")

    print("")
    print("-------- Cliente 1 --------")
    Cliente1 = clas.Cliente()
    CtaJoven1 = clas.CuentaJoven()

    Cliente1.edad = 20
    Cliente1.nomb = "Juan"
    Cliente1.ctajoven = CtaJoven1

    CtaJoven1.titular = Cliente1.nomb
    CtaJoven1.saldo = 10000
    CtaJoven1.Bonificacion = 10

    CtaJoven1.mostrar()

    print("-- Operaciones --")
    CtaJoven1.ingresarDinero(500,Cliente1.edad)
    CtaJoven1.retirarDinero(9000,Cliente1.edad)
    CtaJoven1.aplicarBonific(CtaJoven1.Bonificacion,Cliente1.edad)
    print("----")
    
    CtaJoven1.mostrar()

    print("")
    print("-------- Cliente 2 --------")
    Cliente2 = clas.Cliente()
    CtaJoven2 = clas.CuentaJoven()

    Cliente2.edad = 22
    Cliente2.nomb = "Bokita pasion"
    Cliente2.ctajoven = CtaJoven2

    CtaJoven2.titular = Cliente2.nomb
    CtaJoven2.saldo = 700
    CtaJoven2.Bonificacion = 20

    CtaJoven2.mostrar()

    print("-- Operaciones --")
    CtaJoven2.ingresarDinero(500,Cliente2.edad)
    CtaJoven2.retirarDinero(9000,Cliente2.edad)
    CtaJoven2.aplicarBonific(CtaJoven2.Bonificacion,Cliente2.edad)
    print("----")

    CtaJoven2.mostrar()

    print("")
    print("-------- Cliente 3 --------")
    Cliente3 = clas.Cliente()
    CtaJoven3 = clas.CuentaJoven()

    Cliente3.edad = 17
    Cliente3.nomb = "Traeme la copa Messi"
    Cliente3.ctajoven = CtaJoven3

    CtaJoven3.titular = Cliente3.nomb
    CtaJoven3.saldo = 700
    CtaJoven3.Bonificacion = 30

    CtaJoven3.mostrar()

    print("-- Operaciones --")
    CtaJoven3.ingresarDinero(500,Cliente3.edad)
    CtaJoven3.retirarDinero(9000,Cliente3.edad)
    CtaJoven3.aplicarBonific(CtaJoven3.Bonificacion,Cliente3.edad)
    print("----")

    CtaJoven3.mostrar()

    print("")
    print("-------- Cliente 4 --------")
    Cliente4 = clas.Cliente()
    CtaJoven4 = clas.CuentaJoven()

    Cliente4.edad = 27
    Cliente4.nomb = "Si ganamos el mundial voy hasta Luján caminando"
    Cliente4.ctajoven = CtaJoven4

    CtaJoven4.titular = Cliente4.nomb
    CtaJoven4.saldo = 900
    CtaJoven4.Bonificacion = 40

    CtaJoven4.mostrar()

    print("-- Operaciones --")
    CtaJoven4.ingresarDinero(500,Cliente4.edad)
    CtaJoven4.retirarDinero(9000,Cliente4.edad)
    CtaJoven4.aplicarBonific(CtaJoven4.Bonificacion,Cliente4.edad)
    print("----")

    CtaJoven4.mostrar()

if(__name__=="__main__"):
    main()