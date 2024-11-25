def leer_fecha():
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    return dia, mes, año

def dias_del_mes(mes, anio):
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and es_bisiesto(anio):
        return 29
    return dias_en_mes[mes - 1]

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def calcular_dia_juliano(dia, mes, año):
    dia_juliano = dia
    for m in range(1, mes):
        dia_juliano += dias_del_mes(m, año)
    return dia_juliano
