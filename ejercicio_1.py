#Se crea una lista de varias notas.
calificaciones = [8.5, 9.0, 7.5, 6.0, 10.0]
#Se crea una funcion.
def promedio_notas():
    #Se verifica cual es el menor y el mayor numero de las lista
    calificacion_alta = max(calificaciones)
    calificacion_baja = min(calificaciones)
    #Convertimos esos dos valores en una tupla
    tupla_extremos = (calificacion_baja, calificacion_alta)
    print(f"las notas de extremos es {tupla_extremos}")
    print("------ Analisis de notas ----")
    promedio = sum(calificaciones) / len(calificaciones)
    #se hace una sentencia for para 
    for notas in calificaciones:
        print(f"las notas actuales son: {notas} y el promedio general fue de: {promedio}")
    return promedio
    
    
promedio_notas()


     