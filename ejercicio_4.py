#ejercicio 4

factores = {
    "centimetros": 0.01,
    "metros": 1.0,
    "kilometros": 1000,
    "pies": 3.28,
    "yardas": 1.76,
    "millas": 1609.34
}
# Función para realizar la conversión
def convertir(cantidad, unidad_origen, unidad_destino):
    if unidad_origen in factores and unidad_destino in factores:
        factor_origen = factores[unidad_origen]
        factor_destino = factores[unidad_destino]
        resultado = cantidad * factor_origen / factor_destino
        return resultado
    else:
        return None
#funcion unidad que no exita en el diccionario
def unidad_no_existente(unidad):
    return unidad not in factores

# Ejemplo de uso
cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Ingrese la unidad de origen (centimetros, metros, kilometros, pies, yardas, millas): ")
unidad_destino = input("Ingrese la unidad de destino (centimetros, metros, kilometros, pies, yardas, millas): ")

resultado = convertir(cantidad, unidad_origen, unidad_destino)

if resultado is not None:
    print(f"{cantidad} {unidad_origen} son {resultado} {unidad_destino}")
else:
    print(f"La unidad '{unidad_origen}' o la unidad '{unidad_destino}' no existen entre los factores de conversión.") 
