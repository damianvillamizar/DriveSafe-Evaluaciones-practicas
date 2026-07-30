from Data import guardar_evaluaciones
from datetime import datetime

def validar_fecha():
    while True:
        fecha = input("Fecha (YYYY-MM-DD): ")

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Debe tener el formato YYYY-MM-DD.")

def registrar_evaluacion(evaluaciones):
    estudiante = input("Estudiante: ")
    instructor = input("Instructor: ")

    fecha = validar_fecha()

    while True:
        try:
            calificacion = float(input("Calificación (0-100): "))
            if 0 <= calificacion <= 100:
                break
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Ingrese un número válido.")

    evaluacion = {
        "estudiante": estudiante,
        "instructor": instructor,
        "fecha": fecha,
        "calificacion": calificacion
    }

    evaluaciones.append(evaluacion)
    guardar_evaluaciones(evaluaciones)

    print("Evaluación registrada correctamente.")

def consultar_estudiante(evaluaciones):
    nombre = input("Ingrese el nombre del estudiante: ")

    encontrados = False

    for evaluacion in evaluaciones:
        if evaluacion["estudiante"].lower() == nombre.lower():
            if not encontrados:
                print(f"\nEvaluaciones de {nombre}:")
                encontrados = True

            print(f"- {evaluacion['fecha']} | Instructor: {evaluacion['instructor']} | Calificación: {evaluacion['calificacion']}")

    if not encontrados:
        print("No existen evaluaciones para ese estudiante.")

def promedio_general(evaluaciones):
    if len(evaluaciones) == 0:
        print("No hay evaluaciones registradas.")
        return

    suma = 0

    for evaluacion in evaluaciones:
        suma += evaluacion["calificacion"]

    promedio = suma / len(evaluaciones)

    print(f"Promedio general de calificaciones: {promedio:.2f}")