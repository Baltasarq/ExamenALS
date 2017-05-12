# Main
from os import path
import datetime


notes_filename = "notas.txt"

dni = None
apellidos = None
nombre = None
email = None

def create_notes_file():
    if dni:
        if not path.isfile(notes_filename):
            with open(notes_filename, "wt") as f:
                f.write("\nDNI: " + str(dni))
                f.write("\nApellidos: " + str(apellidos))
                f.write("\nNombre: " + str(nombre))
                f.write("\nEmail: " + str(email))
                f.write("\nDate: " + str(datetime.datetime.now()))
                f.write("\n")
                f.write("\nEjercicio 1: ")
                f.write("\nEjercicio 2: ")
                f.write("\nEjercicio 3: ")
                f.write("\nEjercicio 4: ")
                f.write("\nEjercicio 5: ")
                f.write("\n")
                f.write("\nNota:        ")
                f.write("\n")


if __name__ == "__main__":
    create_notes_file()

    print("DNI:", "n/a" if not dni else str(dni))
    print("Apellidos:", "n/a" if not apellidos else str(apellidos))
    print("Nombre:", "n/a" if not nombre else str(nombre))
    print("Email:", "n/a" if not email else str(email))
    print()
    
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
    
    if not dni:
        print("\n** Recuerda modificar tus datos en main.py **\n")
