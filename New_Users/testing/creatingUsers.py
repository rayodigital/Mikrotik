import random
import string
import pyfiglet
#import connectionToMikrotik

def generar_usuario_y_contrasena():
    # Generar un nombre de usuario aleatorio
    usuario = ''.join(random.choices(string.ascii_lowercase, k=5))
    
    # Generar una contraseña aleatoria
    contrasena = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    print("Usuario: {} => Contraseña: {}".format(usuario,contrasena))

    
    return usuario, contrasena







banner = pyfiglet.figlet_format("CompuTec ST")
print(banner)




# Número de usuarios a crear
num_usuarios = int(input("Número de Usuarios: "))
op_profile = input("30 o 60 minutos: ")
#print(op_profile)


if op_profile == "30":
    profile = "30 MINUTES"
elif op_profile == "60":
    profile = "60 MINUTES"
else:
    profile = "default"
    print("valor no valido")

#print(profile)
#exit();

# Crear el archivo de texto
with open("new_users.rsc", "w") as archivo:
    for _ in range(num_usuarios):
        usuario, contrasena = generar_usuario_y_contrasena()
        #archivo.write(f"{usuario} {contrasena}\n")
        #archivo.write(f"{usuario} {contrasena}\n")
        archivo.write('/ip hotspot user add name={} password={} profile="{}"\n'.format(usuario, contrasena, profile))


print(f"{num_usuarios} usuarios aleatorios creados en 'usuarios_aleatorios.txt'.")

#connectionToMikrotik.main()