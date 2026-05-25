# CONCEPTOS APLICADOS: Diccionarios
# Inicializamos el diccionario vacío donde guardaremos los datos.
# Recuerda que un diccionario almacena parejas de datos llamadas Clave: Valor
# En este caso será -> Nombre: Teléfono
agenda_contactos = {}


# CONCEPTOS APLICADOS: Funciones
# Definimos funciones independientes para modular el código y mantenerlo limpio.

def añadir_contacto():
    print("\n--- Opción 1: Añadir Contacto ---")
    
    # CONCEPTOS APLICADOS: input()
    # Capturamos los datos que digita el usuario por consola
    nombre = input("Escribe el nombre del contacto: ")
    telefono = input(f"Escribe el teléfono de {nombre}: ")
    
    # Guardamos los datos directamente en el diccionario
    agenda_contactos[nombre] = telefono
    print(f"¡Contacto de {nombre} guardado correctamente!")


def buscar_contacto():
    print("\n--- Opción 2: Buscar Contacto ---")
    nombre_buscar = input("Ingresa el nombre del contacto que deseas buscar: ")
    
    # Verificamos si la clave (el nombre) existe dentro de nuestro diccionario
    if nombre_buscar in agenda_contactos:
        print(f"El teléfono de {nombre_buscar} es: {agenda_contactos[nombre_buscar]}")
    else:
        print(f"El contacto '{nombre_buscar}' no existe en la agenda.")


def mostrar_contactos():
    print("\n--- Opción 3: Lista de todos los contactos ---")
    
    # Verificamos si hay elementos en el diccionario antes de intentar leerlos
    if len(agenda_contactos) == 0:
        print("La agenda está vacía en este momento.")
    else:
        # CONCEPTOS APLICADOS: bucle for para iterar sobre diccionarios
        # Usamos el método .items() para extraer simultáneamente la clave y el valor
        for nombre, telefono in agenda_contactos.items():
            print(f"Nombre: {nombre} ------ Teléfono: {telefono}")


# --- CONTROLADOR DEL MENÚ PRINCIPAL ---
def iniciar_programa():
    # Usamos un bucle while infinito para que el menú se repita hasta que decidamos salir
    while True:
        print("\n=== MENÚ AGENDA DE CONTACTOS ===")
        print("1. Añadir un nuevo contacto")
        print("2. Buscar el teléfono de un contacto por su nombre")
        print("3. Mostrar todos los contactos")
        print("4. Salir del programa")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            print("Cerrando la agenda... ¡Hasta luego!")
            break # Rompe el bucle while y finaliza la ejecución
        else:
            print("Opción no válida. Por favor, marca un número del 1 al 4.")

# Ejecución inicial del programa
iniciar_programa()