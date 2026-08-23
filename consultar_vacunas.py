# funcion 7
import csv
import os
import json

def consultar_vacunas():

    codigo_mascota = input("Código de la mascota: ")

    if not os.path.exists("mascotas.json"):
        print("No existe el archivo de mascotas.")
        return

    nombre_mascota = None

    with open(
        "mascotas.json",
        "r",
        encoding="utf-8"
    ) as archivo:

        mascotas = json.load(archivo)

        for mascota in mascotas:

            if mascota["codigo"] == codigo_mascota:
                nombre_mascota = mascota["nombre"]
                break

    # Verificar si la mascota existe
    if nombre_mascota is None:
        print("No existe una mascota con ese código.")
        return

    # Verificar si existen vacunas
    if not os.path.exists("vacunas.csv"):
        print("La mascota existe, pero no tiene vacunas registradas.")
        return

    encontrado = False

    with open(
        "vacunas.csv",
        "r",
        newline="",
        encoding="utf-8",
    ) as archivo:

        lector = csv.reader(archivo)

        for fila in lector:

            if not fila:
                continue

            if fila[0] == "Código Mascota":
                continue

            if fila[0] == codigo_mascota:

                print("------------------------------------")
                print(" Vacuna")
                print("------------------------------------")
                print("Código de mascota:", codigo_mascota)
                print("Nombre de mascota:", nombre_mascota)
                print("Nombre de la vacuna:", fila[1])
                print("Fecha de aplicación:", fila[2])
                print("Próxima dosis:", fila[3])
                print("Veterinario responsable:", fila[4])
                print("------------------------------------")

                encontrado = True

    if not encontrado:
        print("La mascota no tiene vacunas registradas.")