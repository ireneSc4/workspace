import random 
valor_minimo=int(input('introduce el valor minimo: '))
valor_maximo=int(input('introduce el valor minimo: '))
secreto=random.randint(valor_minimo,valor_maximo)
numero=int(input(f'Dime un numero entre el {valor_minimo} y {valor_maximo}: '))
intentos=1
while numero!= secreto:
    intentos +=1
    if numero>secreto:
        numero=int(input('es demasiado grande, intentalo otra vez: '))
    else:
        numero=int(input('es demasiado pequeño,introduce otro numero: '))
print(f'Acertaste el numero te ha costado {intentos} intentos.')
    

