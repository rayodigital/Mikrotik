import random
import string
import pyfiglet
import connectionToMikrotik

def generar_usuario_y_contrasena():
    # Generar un nombre de usuario aleatorio
    usuario = ''.join(random.choices(string.ascii_lowercase, k=5))
    # Generar una contraseña aleatoria - solo letras minusculas
    contrasena = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    # letras mayusculas y minusculas
    #contrasena = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    print("Usuario: {} => Contraseña: {}".format(usuario,contrasena))

    # test
    #creating_html_report_CODING(usuario, contrasena)
    #

    return usuario, contrasena




def creating_html_report_START():
    html_content = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CompuTec ST - Fichas</title>
            <style>
                * {
                    font-size: 12px;
                }
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }

                table {
                    width: 100px;
                    border-collapse: collapse;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    background-color: #ffffff;
                    border-radius: 8px;
                    overflow: hidden;
                }

                th, td {
                    padding: 5px 10px;
                    text-align: left;
                }

                th {
                    background-color: #4CAF50;
                    color: white;
                    text-transform: uppercase;
                }

                tr:nth-child(even) {
                    background-color: #f2f2f2;
                }

                tr:hover {
                    background-color: #ddd;
                }

                td {
                    color: #333;
                }

                /* Estilo de las celdas cuando están seleccionadas */
                td.selected {
                    background-color: #90EE90;
                }


                /* Agregar una línea de separación en la parte superior */
                table::before {
                    content: "";
                    display: block;
                    width: 100%;
                    height: 2px;
                    background-color: #ddd;
                }

                table img {
                    width: 30px;
                }

                .img_icon{
                    text-align: center;
                }

                .img_icon img {
                    margin-top: 10px;
                }

                .header_time {
                    font-size: 15px;
                    text-align: center;
                }

                .text_center {
                    text-align: center;
                }

                .contenedor {
                  display: flex;
                  flex-wrap: wrap;
                  width: 100%;
                  height: 100vh;
                  max-width: 215.9mm;
                  max-height: 279.4mm;
                }

                .item {
                  flex: 1 0 30%;
                  margin: 10px;
                  height: 100px;
                }

            </style>
        </head>
        <body class="contenedor">
    """
    file_html.write(html_content)

def creating_html_report_CODING(user, password):
    html_content = """
        <table class="item">
            <thead>
                <tr>
                    <th class="header_time">{} MINUTOS</th>
                    <th>Usuario</th>
                    <th>Clave</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="img_icon">
                        <span style="display:block;"><strong>Papeleria Gaby</strong> </span>
                        <span> <img src="icon.png"> </span>
                    </td>
                    <td class="text_center">{}</td>
                    <td class="text_center">{}</td>
                </tr>
            </tbody>
        </table>    
    """.format(op_profile, user, password)
    file_html.write(html_content)


def creating_html_report_END():
    html_content = """
        </body>
        </html>
    """ 


# INICIO
banner = pyfiglet.figlet_format("CompuTec ST")
print(banner)


file_html = open("sample_page.html", "w")
#html_content = "";

creating_html_report_START();


#file_html.close()
#exit();

# Número de usuarios a crear
num_usuarios = int(input("Número de Usuarios: "))
op_profile = input("30 o 60 O 120 minutos: ")

if op_profile == "30":
    profile = "30 MINUTES"
elif op_profile == "60":
    profile = "60 MINUTES"
elif op_profile == "120":
    profile = "120 MINUTES"
else:
    profile = "default"
    print("valor no valido")

# Crear el archivo de texto
with open("new_users.rsc", "w") as archivo:
    for _ in range(num_usuarios):
        usuario, contrasena = generar_usuario_y_contrasena()
        creating_html_report_CODING(usuario, contrasena)
        #archivo.write(f"{usuario} {contrasena}\n")
        #archivo.write(f"{usuario} {contrasena}\n")
        archivo.write("/ip hotspot user add name={} password={} profile=\"{}\"\n".format(usuario, contrasena, profile))

print(f"{num_usuarios} usuarios aleatorios creados en 'usuarios_aleatorios.txt'.")
creating_html_report_END();
#connectionToMikrotik.main()