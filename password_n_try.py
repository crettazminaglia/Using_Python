#Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

password= str("estoyprogramandoenPYTHON!")
ingrese_password= str(input("Ingrese su contraseña "))
intentos=0
while password != ingrese_password:
    print("Su contraseña es incorrecta. Intentelo de nuevo ")
    intentos= intentos + 1
    if (intentos ==3):
        break
    ingrese_password = str(input("Ingrese su contraseña "))
print("Su contraseña es correcta")
