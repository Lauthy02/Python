'''
Autor:
Fecha:
Descripcion:
'''
def main():
    import Librerias.Funciones #No creo q ande
    Nombre = input("Escriba su nombre: ") #Los valores que guarda el input siempre van a ser una cadena
    Edad = int(input("Escriba su edad: ")) #Si quiero guardar un tipo entero tengo q parsear el input

    print(f"Hola {Nombre}, tienes {Edad} años.")

    if(Edad>=18):{
        input("Usted es mayor de edad.")
    }
    else:{
        input("Usted es menor de edad.")
    }



if (__name__=="__main__"):{
    main()
}
