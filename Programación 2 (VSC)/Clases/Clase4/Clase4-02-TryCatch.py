def Dvidir():
    try:
        a=10/0
    except ZeroDivisionError(): #acá tengo el error q quiero capturar o q supongo q pasará
        print("No se puede dividir por 0.")
    except: #Y este es el error por defecto
        print("Entra cuando SI hay errores")
    else:
        print("Enta a este else cuando NO hay errores dentro del try")
    finally:
        print("Acá entra siempre")
