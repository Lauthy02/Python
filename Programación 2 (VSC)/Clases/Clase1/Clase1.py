#Fecha: 18/08/2022 - Clase1 - P2

print ("Hola mundo")

#Comentario



# TODO Cambiar esto por lo otro 

'''
Básico del lenguaje a conocer para relacionar todos los lenguajes q vimos
    Variables -- tiene un tipado dinámico, no necesita identificar el tipo de dato.
    a=5 Python decide q tipo de dato
    Pero si yo modifico el dato, por ejemplo le paso un string sin querer, lo cambia a string

    -Tipos de datos
        str: String
        bool: Boolean
        int: Entero
        float: Flotante

    -Constantes: La constante no es variable, no cambia el valor. Para python todas son variables, no existen constantes
    
    -Variables: El valor cambia con respecto al tiempo. Python no necesita que se escriba q tipo de dato es la variable
        Reglas a tener en cuenta:
            -Las variables siempre en minúscula 
                edad_del_perro = 10
            -Cuando una variable, q nuestra intención es no cambiar el valor, escribimos la variable todo el mayúscula
                NOMBRE = Santi 
                PI = 3.14
    
    -Decisión 
        if
            Estructura del if
                ----------------------
                if (condición):
                    intrucción simple  
                    intrucción simple
                ----------------------
            Estructura del if anidado
                ----------------------
               if (a==5):
                    print("a es igual a: " + str(a))
                else:
                    if (b==5):
                        print("Es aaaaaaa")
                    else:
                        print("aaaaa") 
                ----------------------
        else
            Estructura del else
                ----------------------
                if (a==5):
                    print("a es igual a: " + str(a))
                else:
                    print("Es aaaaaaa")
                print("esta línea no está dentro del if porque no está tabulada")
                ----------------------
        elif: elseif
            Estructura del elif
                ----------------------
                if (a==5):
                    print("a es igual a: " + str(a))
                elif (a>5):  
                    print("Es aaaaaaa")
                else: #Este else pasa a ser el else de todos los elif
                    if (b==5):
                        print("Es aaaaaaa")
                    else:
                        print("aaaaa")
                ----------------------
        switch: no existe en python 
    
   -Repetición
        for 
            Estructura del for
                ----------------------
                for i in range (5): #Me imprime de 0 a 4
                    print(i)
                ----------------------
                for i in 'range' : #Me recorre el string
                    print(i)
                ----------------------
                for i in range (5,2,-1): #inicio, final, orientación
                    print(i)
                ----------------------
        while 
            Estructura del while
                ----------------------
                a=0
                while(a<10):
                    a=a+1
                    a+=1            
                ----------------------
        do-while: no existe
    
    -Funciones
        siempre empiezan con def
            ----------------------
            def sumar(a,b):
                return a+b
            print(sumar(2,3))
            ----------------------
            def sumar(a,b):
                return a,b #puede devolver más de un valor
            a,b=sumar(2, 3)
            print(a,b)
             ----------------------

'''
a=5
print(tyipe(a))
print("el valor de a es: " + a) #Python no me deja concaternar porque esa es una propiedad de los string, entonces lo convierto
print("el valor de a es: " + str(a))
print("el valor de a es: " + bin(a)) #Convierto el valor a binario 
print("el valor de a es: " + hex(a)) #Convierto el valor a hexadecimal 
print("el valor de a es: " + int(a)) #Convierto el valor a entero
print("el valor de a es: " + bool(a)) #Convierto el valor a boolean
print("el valor de a es: " + float(a)) #Convierto el valor a flotante 

'''
las variables siempre en minúscula 
edad_del_perro = 10

cuando una variable, q nuestra intención es no camiar el valor, escribimos la variable todo el mayúscula
NOMBRE = Santi 
PI = 3.14

intruccion simple 
    print("hola mundo")

instruccion compleja
    conjunto de instrucciones simples 
    c#
    {
        intruccion
        intruccion
    }

Estructura del if
    if (condicion):
        intruccion simple  
        intruccion simple
    
'''
if (a==5):
    print("a es igual a: " + str(a))
else:
    print("Es aaaaaaa")
print("esta linea no esta dentro del if")

#ifs anidados
if (a==5):
    print("a es igual a: " + str(a))
else:
    if (b==5):
        print("Es aaaaaaa")
    else:
        print("aaaaa")

if (a==5):
    print("a es igual a: " + str(a))
elif (a>5):  
    print("Es aaaaaaa")
else: #Este else pasa a ser el else de todos los elif
    if (b==5):
        print("Es aaaaaaa")
    else:
        print("aaaaa")

a=0
while(a<10):
    a=a+1
    a+=1


for i in range (5):
    print(i)

for i in 'range' : #me recorre la lista
    print(i)


print("hola" * 4)

def sumar(a,b):
    return a+b

print(sumar(2,3))



def sumar(a,b):
    return a,b #puede devolver mas de un valor

a,b=sumar(2, 3)

print(a,b)