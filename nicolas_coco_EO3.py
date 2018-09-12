#Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita
# continuar hasta que la haya ingresado correctamente.

password= str("estoyprogramandoenPYTHON!")
ingrese_password= str(input("Ingrese su contraseña "))
while password != ingrese_password:
    print("Su contraseña es incorrecta. Intentelo de nuevo")
    ingrese_password = str(input("Ingrese su contraseña "))
print("Su contraseña es correcta")
