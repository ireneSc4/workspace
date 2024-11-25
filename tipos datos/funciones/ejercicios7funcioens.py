def calcular_mcd(a,b):
    while b != 0:
        a,b = b, a % b
        return a
num1=int(input('introduce el ptimer numero: '))
num2=int(input('introduce el segundo numero: '))
print(f'el MCD DE {num1} y {num2} es: {calcular_mcd(num1,num2)}')