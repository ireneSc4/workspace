# programa que calcula IMG
peso=float(input('introduce tu peso en Kg: '))
altura=float(input('introduce tu altura en metros: '))
imc=round(peso/(altura*altura),2)
print(f'tu IMC es {imc}')

if imc <18.5:
    print('tienes influencia ponderal')
elif (18.5<imc<24.9):
    print('su peso es normal')
elif(25<imc<29.9):
    print('tienes sobrepeso')
else:
    print('tienes obesidad')




