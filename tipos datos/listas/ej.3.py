n_palabras=int(input('Dime cunatas palabras tiene la lista: '))
lista=[]
for i in range (1,n_palabras+1):
    palabra=input(f'Dime la palabra{i}: ')
    lista.append(palabra)
print(f'La lista creada es {lista}')
lista2=sorted(lista)
print(f'La lista ordenada es {lista2}')