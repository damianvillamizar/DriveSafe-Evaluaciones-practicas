from Data import cargar_evaluaciones
from Funciones import registrar_evaluacion, consultar_estudiante, promedio_general

def menu():
    evaluaciones = cargar_evaluaciones()

    while True:
        print("\n=== SISTEMA DE EVALUACIONES DRIVESAFE ===")
        print("1. Registrar nueva evaluación")
        print("2. Consultar evaluaciones por estudiante")
        print("3. Calcular promedio general")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_evaluacion(evaluaciones)

        elif opcion == "2":
            consultar_estudiante(evaluaciones)

        elif opcion == "3":
            promedio_general(evaluaciones)

        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida.")

menu()
