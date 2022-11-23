import lib.Clases as cla
import os

def main():
    os.system("cls")

    p=cla.Persona()
    p.nombre = "juan"
    print(p.nombre)

    o=cla.Operador()
    o.nombre = "pepe"
    print(o.nombre)

if(__name__=="__main__"):
    main()