#Ejercicio 2: lista de compras interactiva

# Se crea una lista de compras vacia
lista_compras = []
# Se crea un bucle while para que el usuario ingrese una opcion del menu
while True:
    print("\n--- Menu ---")
    print("1. Agregar item")
    print("2. Eliminar item")
    print("3. Mostrar lista")
    print("4. Salir")
    print("------------")
    opcion = input("Ingrese una opcion: ")

    #Se verifica la opcion ingresada por el usuario
    if opcion == "1":
        item = input("Ingrese el item: ")
        while item == "": # Se verifica que el item no este vacio si esta vacio vuelve y le pregunta la variable item
            print("El item no puede estar vacio.")
            item = input("Ingrese el item: ")
        lista_compras.append(item)
        print(f"{item} agregado.")
# Se verifica la opcion ingresada por el usuario
    elif opcion == "2":
        if len(lista_compras) == 0:
            print("La lista esta vacia.")
        else:
            item = input("Ingrese el item a eliminar: ") # Se verifica que el item no este vacio
            if item in lista_compras:
                lista_compras.remove(item) # Se elimina el item
                print(f"{item} eliminado.")
            else:
                print(f"{item} no esta en la lista.")
# Se verifica la opcion ingresada por el usuario
    elif opcion == "3":
        if len(lista_compras) == 0:
            print("La lista esta vacia.")
        else:
            print("\n--- Lista de compras ---")
            for item in lista_compras: 
                print(f"  - {item}")
            print("------------------------")
            print(f"Total de items: {len(lista_compras)}")
    elif opcion == "4":
        print("Hasta luego.")
        break # Rompe el bucle while

    else:
        print("Opcion no valida.")