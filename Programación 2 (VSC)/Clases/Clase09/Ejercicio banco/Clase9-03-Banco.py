import os
import lib.Clases as bco

def main():
    os.system("cls")

    cc = bco.CtaCorriente()
    ca = bco.CtaCajaAhorro()
    cli = bco.Cliente()

    cc.saldo = 1000
    ca.saldo = 300
    cli.ca = ca
    cli.cc = cc

    

if(__name__=="__main__"):
    main()