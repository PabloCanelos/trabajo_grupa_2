# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
#______________________________________

nombre = " "
numero_telefono = 0
def agregar_contacto(contactos):
    while True:
        if len(nombre) < 3:
            nombre = input("Ingrese nombre del contacto:\n").lower()
        else:
            contactos.append(nombre)
            print("Contacto agragado exitosamente")
    
            
            
    
    numero_telefono = int(input("Ingrese numero de teléfono:\n"))

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