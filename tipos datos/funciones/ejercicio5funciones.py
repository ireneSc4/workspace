def cantidad_segundos(horas,minutos,segundos):
    return horas * 3600+ minutos *60 + segundos

def cantidad_horas(segundos):
    horas = segundos // 3600
    minutos= (segundos % 3600)// 60
    segundos= segundos % 60
    print(f"Son {horas} horas, {minutos} minutos y {segundos} segundos")

    opcion= input('pon "1" si queires cambiar de segundos a horas,minutos y segundos; pon "2" si quieres cambiar de  horas,minutos y segundos a segundos: ')
    if opcion== '1':
        segundos=int(input('dime cuantos segundos: '))
        cantidad_horas(segundos)
    else:
        horas=int(input('dimme las horas: '))
        minutos=int(input('dimme los minutos: '))
        segundos=int(input('dimme los minutos: '))
        cantidad_segundos(horas,minutos,segundos)
