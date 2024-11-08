n_palabras=int(input('Dime cunatas palabras tiene la lista: '))
list=[]
for i in range (1,n_palabras+1):
    palabra=input(f'Dime la palabra{i}: ')
    list.append(palabra)
print(f'La lista creada es {list}')
lista_inversa=list(reversed{lista})
print(f'La lista inversa es {lista_inversa}')