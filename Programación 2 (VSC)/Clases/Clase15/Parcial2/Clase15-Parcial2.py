import os
import lib.Clases as clas

def main():
    os.system("cls")

    Cliente1 = clas.Cliente()
    CtaJoven = clas.CuentaJoven()

    Cliente1.edad = 20
    Cliente1.nomb = "Juan"
    Cliente1.ctajoven = CtaJoven

    CtaJoven.titular = Cliente1.nomb
    CtaJoven.saldo = 10000
    CtaJoven.Bonificacion = 10

    CtaJoven.mostrar()

if(__name__=="__main__"):
    main()