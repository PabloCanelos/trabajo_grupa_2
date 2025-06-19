from functions import buscar_contacto, eliminar_contacto, salir_programa

def main():
    contactos = [
        {"nombre": "Ana", "telefono": "123456789"},
        {"nombre": "Luis", "telefono": "987654321"},
        {"nombre": "María", "telefono": "555555555"}
    ]

    while True:
        print("\nOpciones:")
        print("1. Buscar contacto")
        print("2. Eliminar contacto")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre a buscar: ")
            resultado = buscar_contacto(nombre, contactos)
            if resultado:
                for x in resultado:
                    print(f"Nombre: {x['nombre']}, Teléfono: {x['telefono']}")
            else:
                print("Contacto no encontrado.")

        elif opcion == "2":
            nombre = input("Ingresa el nombre a eliminar: ")
            eliminado = eliminar_contacto(nombre, contactos)
            if eliminado:
                print("Contacto eliminado correctamente.")
            else:
                print("No se encontró el contacto para eliminar.")

        elif opcion == "3":
            salir_programa()

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()


