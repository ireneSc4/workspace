numero=int(input('digame un numero: '))
lista=[]

for i in range(1,numero+1):
    if i%2==0:
        lista.append(i)
print(f'Los numeros primos hasta {numero} son: {lista}')