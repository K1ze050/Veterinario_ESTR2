# funcion 9
import json
import csv
import os

def mostrar_resumen():

    mascotas = 0
    consultas = 0
    vacunas = 0
    archivos = 0

    # Contar mascotas
    if os.path.exists("mascotas.json"):

        with open(
            "mascotas.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(archivo)
            mascotas = len(datos)

    # Contar consultas
    if os.path.exists("consultas.json"):

        with open(
            "consultas.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(archivo)
            consultas = len(datos)

    # Contar vacunas
    if os.path.exists("vacunas.csv"):

        with open(
            "vacunas.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as archivo:

            lector = csv.reader(archivo)

            for fila in lector:

                if not fila:
                    continue

                if fila[0] == "Código Mascota":
                    continue

                vacunas += 1

    # Contar archivos externos
    if os.path.exists("archivos_externos.json"):

        with open(
            "archivos_externos.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(archivo)
            archivos = len(datos)

    print("------------------------------------")
    print(" RESUMEN GENERAL DEL SISTEMA")
    print("------------------------------------")
    print("Mascotas registradas:", mascotas)
    print("Consultas registradas:", consultas)
    print("Vacunas registradas:", vacunas)
    print("Archivos asociados:", archivos)
    print("------------------------------------")