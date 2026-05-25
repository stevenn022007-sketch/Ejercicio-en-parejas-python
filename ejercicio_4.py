#Ejercicio 4: Conversor de Unidades

# Factores de conversion a metros
conversiones = {
    "metros"      : 1.0,
    "pies"        : 0.3048,
    "pulgadas"    : 0.0254,
    "centimetros" : 0.01,
    "kilometros"  : 1000.0,
    "millas"      : 1609.34,
    "yardas"      : 0.9144
}

def convertir(cantidad, origen, destino):
    if origen not in conversiones:
        print(f"'{origen}' no es una unidad valida.")
        return None
    if destino not in conversiones:
        print(f"'{destino}' no es una unidad valida.")
        return None
    en_metros = cantidad * conversiones[origen]
    resultado = en_metros / conversiones[destino]
    return resultado

while True:
    print("\n=============CONVERSOR DE UNIDADES=============")
    print("Unidades disponibles:")
    for unidad in conversiones:
        print(f"  - {unidad}")
    print("===============================================")

    cantidad = input("\nIngrese la cantidad (o 'salir'): ")
    if cantidad.lower() == "salir":
        print("Hasta luego.")
        break

    cantidad = float(cantidad)
    origen   = input("Unidad de origen  : ").lower()
    destino  = input("Unidad de destino : ").lower()

    resultado = convertir(cantidad, origen, destino)
    if resultado is not None:
        print(f"\n{cantidad} {origen} = {resultado:.4f} {destino}")