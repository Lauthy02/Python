import datetime

i=1

while(i==1):
    dia1 = int(input(f"ingrese el día de la fecha 1: "))
    mes1 = int(input(f"ingrese el mes de la fecha 1: "))
    anio1 = int(input(f"ingrese el año de la fecha 1: "))
    dia2 = int(input(f"ingrese el día de la fecha 2: "))
    mes2 = int(input(f"ingrese el mes de la fecha 2: "))
    anio2 = int(input(f"ingrese el año de la fecha 2: "))
    i = i + 1
    

fecha1 = datetime.date(anio1,mes1,dia1)
fecha2 = datetime.date(anio2,mes2,dia2)

print(fecha1)