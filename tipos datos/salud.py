quieres_saludar = 'S'  
NUM_MAX_SALUDOS=4
num_saludos=0
while quieres_saludar=='S':
    print('Hola que tal!')	
    num_saludos +=1
    if num_saludos == NUM_MAX_SALUDOS:
         print('Has alcanzado el nº máximo de salidos')
         break
    quieres_saludar=input('¿Quiere otro saludo? [S/N])')
    while quieres_saludar not in ('S','N'):
         quieres_saludar =input('solo se aceptan los caracteres \'S\' O \'N\'.¿Quiere otro saludo? [S/N]')
        
    
print('que tenga un buen dia')
    
   