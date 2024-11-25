def login(usuario, contraseña, intentos):
    if usuario == "usuario1" and contraseña == "asd123":
        return True, intentos
    else:
        intentos +=False, intentos
    
intentos=0
while intentos <3:
    usuario=input("introduce el nombre de usuario: ")
    contraseña=input('initroduce la contraseña: ')
    acceso, intentos=login(usuario,contraseña,intentos)
    if acceso:
        print("acceso concedido")
        break
    else:
        print(f'acceso denegado.intententos restantes: {3-intentos}')

if intentos==3:
    print('has agotado tus intentos.')
              
              
              
