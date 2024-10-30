#programa que decide si un numero es  primer o 

t=int(int('introduce el numero de casos que cal processar: '))
for i in range(0,t):
    k=int(input('Introdueix un nombre entre 0 i 100: '))
    n=int(input('Introdueix un nombre sancer entre 1 i 100000 : '))
    if k == 0:
        if (n%2 == 0):
            print('NO')
        else:
            print('SI')
        


