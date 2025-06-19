# Lista de ejemplo de contactos
contactos = [
    {"nombre": "Ana", "telefono": "123456789"},
    {"nombre": "Luis", "telefono": "987654321"},
    {"nombre": "María", "telefono": "555555555"}
]

# 3. Buscar un contacto por nombre
def buscar_contacto(nombre, lista_contactos):
    resultados = [c for c in lista_contactos if c["nombre"].lower() == nombre.lower()]
    if resultados:
        return resultados
    else:
        return None

# 4. Eliminar un contacto
def eliminar_contacto(nombre, lista_contactos):
    for i, contacto in enumerate(lista_contactos):
        if contacto["nombre"].lower() == nombre.lower():
            del lista_contactos[i]
            return True  # Contacto eliminado
    return False  # Contacto no encontrado

# 5. Salir del programa
def salir_programa():
    print("Saliendo del programa...")
    exit()

