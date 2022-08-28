'''
Autor:
Fecha:
Descripcion:
'''
#import Librerias.Funciones
def main():
    a=1
    Nombre = "Lautaro"
    print("1- La suma es: " + str(2))
    print("2- La suma es: " , str(a))
    print(a)
    
    for i in range (5): #Me imprime de 0 a 4
        print(i)

    for i in 'range' :{ #Me recorre el string
        print(i)
    }
    
    def Restar(c,d): #Funicón
        return c-d

    c=5
    d=2
    print("la resta de c y d es: " + str(Restar(c, d)))
    
    if(c > 4):{
        print("c es mayor a 4")
    }

    print("Hola {}, tenés {} años".format(Nombre,a))
    print(f"Hola {Nombre}, tenés {a} años")
    

if __name__=="__main__":
    main()
