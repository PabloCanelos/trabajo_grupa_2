def buscar_contacto(contactos):
    nombre_buscar = input("Ingresa el nombre del contacto que quieras buscar:\n").lower()
    encontrados = []
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre_buscar:
            encontrados.append(contacto) 
    if encontrados:
        print("Contacto(s) encontrados(s):\n")
        for i in encontrados:
            print(f"{i["nombre"]}, {i["telefono"]}, {i["mail"]}")
    else: 
        print("No se encontro ningun contacto!")

def salir_menu(): 
    print("Saliendo del menú.... ¡Hasta pronto!")

