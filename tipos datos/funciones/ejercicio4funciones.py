def calcular_circulo(radio):
    area=3.14 * radio**2
    perimetro= 2 * 3.14 * radio
    print(f"els area es {area} y el perimetro es {perimetro}")

radio=float(input('introduce el radio: '))
calcular_circulo(radio)