numeros = [1, 2, 34, 86, 4, 5, 98, 890, 45]

pares=[]
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(pares)