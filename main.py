import os
from functions import agregar_contacto, listar_contactos, buscar_contacto, eliminar_contacto, salir_menu

os.system("cls")
contactos = []
while True:
    print("========= MENÚ =========")
    print("1. Agregar contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto por nombre")
    print("4. Eliminar un contacto")
    print("5. Salir")
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("Agregar contacto")
            agregar_contacto(contactos)
            os.system("Pause")
        elif opcion == 2:
            os.system("cls")
            print("Lista de contactos")
            listar_contactos(contactos)
            os.system("Pause")
        elif opcion == 3:
            os.system("cls")
            print("Buscar contacto por nombre")
            buscar_contacto(contactos)
            os.system("Pause")
        elif opcion == 4:
            os.system("cls")
            print("Eliminar contacto")
            eliminar_contacto(contactos)
            os.system("Pause")
        elif opcion == 5:
            os.system("cls")
            salir_menu()
            os.system("Pause")
            break
        else:
            print("opcion ingresada no existe")
            os.system("Pause")
    except:
        print("Ingrese un valor numerico correcto!")
