# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
#______________________________________

# nombre = " "
# numero_telefono = 0
def agregar_contacto(contactos):
    while True:
        nombre = input("Ingrese nombre del contacto:\n").lower()
        if len(nombre) < 3:
            print("El nombre debe tener al menos 3 caracteres.")
        else:
            break
            # contactos.append(nombre)
            # print("Contacto agragado exitosamente")
    try:
        numero_telefono = input("Ingrese número de teléfono:\n").strip()
        mail = input("Ingrese correo electrónico:\n").strip()

        nuevo_contacto = {
            "nombre": nombre,
            "telefono": numero_telefono,
            "mail": mail
        }
        contactos.append(nuevo_contacto)
        print("Contacto agregado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def listar_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
    else:
        print("Lista de contactos:")
        for contacto in contactos:
            print(f"{contacto['nombre']}, {contacto['telefono']}, {contacto['mail']}")


def buscar_contacto(contactos):
    nombre_buscar = input("Ingresa el nombre del contacto que quieras buscar:\n").lower()
    encontrados = []
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre_buscar:
            encontrados.append(contacto)
    if encontrados:
        print("Contacto(s) encontrados(s):\n")
        for i in encontrados:
            print(f"{i['nombre']}, {i['telefono']}, {i['mail']}")
    else:
        print("No se encontro ningun contacto!")
def eliminar_contacto(contactos):
    nombre_eliminar = input("Ingresa el nombre del contacto que deseas eliminar:\n").lower()
    encontrado = False
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre_eliminar:
            contactos.remove(contacto)
            print("🗑️ Contacto eliminado exitosamente.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún contacto con ese nombre.")

def salir_menu():
    print("Saliendo del menú.... ¡Hasta pronto!")