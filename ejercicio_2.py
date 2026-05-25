productos = ["Televisor","Telefono","nevera","audifonos"]

print("Ingresa la opcion que quieras realizar:\n A: VER PRODUCTOS \n B: Agregar nuevo Item \n C: Eliminar Item de la lista. ")
Opcion_Usuario = input("Ingresa la Opcion: ")

if Opcion_Usuario == "A":
    print(f"Los productos que estan en la lista son: {productos}")
elif Opcion_Usuario == "B":
    item_nuevo = input("Ingresa un producto :")
    while item_nuevo == "":
        print("El Campo no puede estar vacio")
        item_nuevo = input("ingresa un producto valido: ")
    agregar_item = productos.append(item_nuevo)
    print(f"se ingreso el nuevo producto a la lista {productos}")
elif Opcion_Usuario == "C":
    print(f"Estos son los productos que estan en la lita: {productos}")
    item_eliminar = input("Ingrese el producto que deseea eliminar: ")
    while item_eliminar == "":
        print("El Campo no puede estar vacio")
        item_eliminar = input("ingresa un producto valido: ")
    eliminar_producto = productos.remove(item_eliminar) 
    print(f"El Producto {item_eliminar} fue eliminado de los productos {productos}")

 