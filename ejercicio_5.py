# Ejercicio 5: Mini Sistema de Gestion de Inventario

inventario = []

def agregar_producto():
    nombre   = input("Nombre del producto: ")
    precio   = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en inventario: "))
    producto = {
        "nombre"   : nombre,
        "precio"   : precio,
        "cantidad" : cantidad
    }
    inventario.append(producto)
    print("Producto agregado al inventario.")

def realizar_venta():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    nombre = input("Nombre del producto a vender: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] == 0:
                print("No hay stock disponible.")
                return
            cantidad_venta = int(input("Cuantas unidades? "))
            if cantidad_venta > producto["cantidad"]:
                print("No hay suficientes unidades.")
                return
            producto["cantidad"] -= cantidad_venta
            total = cantidad_venta * producto["precio"]
            print("Venta realizada. Total: $" + str(total))
            return
    print("Producto no encontrado.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    print("\n=============INVENTARIO=============")
    for producto in inventario:
        print("  Nombre   : " + producto["nombre"])
        print("  Precio   : $" + str(producto["precio"]))
        print("  Cantidad : " + str(producto["cantidad"]) + " unidades")
        print("  ----------------------------------")
    print("  Total de productos: " + str(len(inventario)))
    print("====================================")
    input("Presiona Enter para continuar...")

while True:
    print("\n=============GESTION DE INVENTARIO=============")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")
    print("===============================================")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        realizar_venta()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("Hasta luego.")
        break
    else:
        print("Opcion no valida.")
