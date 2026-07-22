import json
import os

archivo = "contactos.json"

# Si el archivo no existe, este lo crea (el de los contactos)
if not os.path.exists(archivo):
    with open(archivo, "w") as f:
        json.dump([], f)

while True:
    print("\n===== DIRECTORIO TELEFÓNICO =====")
    print("1. Crear contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el número telefónico: ")

        with open(archivo, "r") as f:
            contactos = json.load(f)

        contacto = {
            "nombre": nombre,
            "telefono": telefono
        }

        contactos.append(contacto)

        with open(archivo, "w") as f:
            json.dump(contactos, f, indent=4)

        print("Contacto guardado correctamente.")

    elif opcion == "2":
        buscar = input("Ingrese el nombre a buscar: ")

        with open(archivo, "r") as f:
            contactos = json.load(f)

        encontrado = False

        for contacto in contactos:
            if contacto["nombre"].lower() == buscar.lower():
                print("Nombre:", contacto["nombre"])
                print("Teléfono:", contacto["telefono"])
                encontrado = True

        if not encontrado:
            print("No se encontró el contacto.")

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")