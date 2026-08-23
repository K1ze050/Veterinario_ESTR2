# funcion # 6
import csv
import os
import json

def registrar_vacuna():

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

    if nombre_mascota is None:
        print("No se encontró una mascota con ese código.")
        return

    print("Nombre de la mascota:", nombre_mascota)

    vacuna = input("Nombre de la vacuna: ")
    fecha = input("Fecha de aplicación: ")
    proxima_dosis = input("Fecha de próxima dosis: ")
    veterinario = input("Veterinario responsable: ")

    archivo_nuevo = not os.path.exists("vacunas.csv")

    with open(
        "vacunas.csv",
        "a",
        newline="",
        encoding="utf-8",
    ) as archivo:

        escritor = csv.writer(archivo)

        if archivo_nuevo:
            escritor.writerow([
                "Código Mascota",
                "Vacuna",
                "Fecha",
                "Próxima dosis",
                "Veterinario Responsable"
            ])

        escritor.writerow([
            codigo_mascota,
            vacuna,
            fecha,
            proxima_dosis,
            veterinario
        ])

    print("Vacuna registrada correctamente.")