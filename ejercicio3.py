#punto 3

listaUsuarios = {"Juan1223": "J12an*.",
                 "Maria2345":"M23a*.",
                 "Pablo1459":"P14o*.",
                 "Ana3456":"A34a*."}
intentosFallidos = 0

#Logica de acceso
for fallido in range(3):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario not in listaUsuarios and contraseña not in listaUsuarios:
        intentosFallidos += 1
        if intentosFallidos == 3:
            print("Lo siento, su acceso no es permitido ")
            break
        print("Datos incorrectos")
    else:
        print("Acceso permitido")
        break