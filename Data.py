import json
import os

ARCHIVO = "evaluaciones.json"

def cargar_evaluaciones():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            return []
    return []

def guardar_evaluaciones(evaluaciones):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(evaluaciones, archivo, indent=4, ensure_ascii=False)