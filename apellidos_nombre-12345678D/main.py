# charset: utf-8
# Main

from os import path
import datetime


info_filename = "usr_exam_data.txt"

def retrieve_info_file(usr_data):
    try:
        with open(info_filename, "r") as f:
            usr_data["dni"] = f.readline().strip()
            usr_data["nombre"] = f.readline().strip()
            usr_data["apellidos"] = f.readline().strip()
            usr_data["email"] = f.readline().strip()
    except FileNotFoundError or IOError:
        return

if __name__ == "__main__":
    usr_data = {"dni": None, "apellidos": None, "nombre": None, "email": None}
    retrieve_info_file(usr_data)

    print("DNI:" + "n/a" if not usr_data["dni"] else str(usr_data["dni"]))
    print("Apellidos:" +
          "n/a" if not usr_data["apellidos"] else str(usr_data["apellidos"]))
    print("Nombre:" +
          "n/a" if not usr_data["nombre"] else str(usr_data["nombre"]))
    print("Email:" + "n/a" if not usr_data["email"] else str(usr_data["email"]))
    print("\n")

    import ejercicio1
    ejercicio1.main()

    import ejercicio2
    ejercicio2.main()

    import ejercicio3
    ejercicio3.main()

    import ejercicio4
    ejercicio4.main()

    import ejercicio5
    ejercicio5.main()

    if not usr_data["dni"]:
        print("\n** Recuerda crear tus datos en '" + info_filename + "' **\n")
