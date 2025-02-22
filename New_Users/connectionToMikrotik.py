import paramiko
from scp import SCPClient, SCPException

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(server, port, user, password)
    except paramiko.SSHException as e:
        print(f"Error de conexión SSH: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    return client

def main():
    # Configura tus credenciales y el archivo
    router_ip = '192.168.100.100'  # Cambia esto por la IP de tu router
    username = 'admin'          # Cambia esto por tu usuario
    password = ''  # Cambia esto por tu contraseña
    file_to_copy = 'new_users.rsc'  # Archivo que deseas copiar al MikroTik
    remote_path = '/new_user1.rsc'    # Ruta donde se guardará en el MikroTik

    # Crear conexión SSH
    ssh_client = create_ssh_client(router_ip, 22, username, password)
    if ssh_client is None:
        print("No se pudo establecer la conexión SSH. Finalizando.")
        return

    try:
        # Copiar el archivo al MikroTik
        with SCPClient(ssh_client.get_transport()) as scp:
            scp.put(file_to_copy, remote_path)
            print(f"Archivo {file_to_copy} copiado a {remote_path} en MikroTik.")
    except SCPException as e:
        print(f"Error al copiar el archivo: {e}")
        ssh_client.close()
        return
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        ssh_client.close()
        return

    try:
        # Ejecutar el script en MikroTik
        stdin, stdout, stderr = ssh_client.exec_command(f"/import {remote_path}")
        
        # Leer y mostrar la salida estándar
        print(stdout.read().decode())
        
        # Leer y mostrar cualquier error
        error_output = stderr.read().decode()
        if error_output:
            print("Errores durante la ejecución del script:")
            print(error_output)
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")

    # Cerrar la conexión
    ssh_client.close()

if __name__ == "__main__":
    main()
