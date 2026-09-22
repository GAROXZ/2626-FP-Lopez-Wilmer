def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Agregar o actualizar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def agregar_contacto(agenda):
    """Permite agregar un nuevo contacto al diccionario."""
    nombre = input("Ingrese el nombre del contacto: ").strip().capitalize()
    telefono = input("Ingrese el número de teléfono: ").strip()

    agenda[nombre] = telefono
    print(f"✅ Contacto '{nombre}' guardado exitosamente.")


def mostrar_contactos(agenda):
    """Recorre y muestra la información almacenada en el diccionario."""
    if not agenda:
        print("⚠️ La agenda de contactos está vacía.")
    else:
        print("\n--- LISTA DE CONTACTOS ---")
        for nombre, telefono in agenda.items():
            print(f"• Nombre: {nombre} | Teléfono: {telefono}")


def buscar_contacto(agenda):
    """Realiza la búsqueda de un contacto por su nombre."""
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip().capitalize()

    if nombre in agenda:
        print(f"🔎 Encontrado -> Nombre: {nombre} | Teléfono: {agenda[nombre]}")
    else:
        print(f"❌ El contacto '{nombre}' no existe en la agenda.")


def eliminar_contacto(agenda):
    """Elimina un contacto existente del diccionario."""
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().capitalize()

    if nombre in agenda:
        del agenda[nombre]
        print(f"🗑️ Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"❌ El contacto '{nombre}' no se encuentra en la agenda.")


def main():
    """Función principal que controla el flujo del programa."""
    # Colección de datos utilizada: Diccionario
    agenda = {}

    # Datos iniciales opcionales para pruebas rápidas
    agenda["Carlos"] = "0991234567"
    agenda["María"] = "0987654321"

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            mostrar_contactos(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            print("\n¡Gracias por utilizar la Agenda de Contactos! Hasta luego.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()