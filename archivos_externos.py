# funcion 8
import json
import os
import shutil # funcion para copiar archivos

def asociar_archivo():

    codigo_mascota = input("Código de la mascota: ")

    if not os.path.exists("mascotas.json"):
        print("No existe el archivo de mascotas.")
        return

    with open(
        "mascotas.json",
        "r",
        encoding="utf-8"
    ) as archivo:

        mascotas = json.load(archivo)

    nombre_mascota = None

    for mascota in mascotas:

        if mascota["codigo"] == codigo_mascota:
            nombre_mascota = mascota["nombre"]
            break

    if nombre_mascota is None:
        print("No existe una mascota con ese código.")
        return

    print("Mascota:", nombre_mascota)

    ruta_archivo = input("Escriba la ruta del archivo: ")

    if not os.path.exists(ruta_archivo):
        print("El archivo no existe.")
        return

    nombre_archivo = os.path.basename(ruta_archivo)

    ruta_destino = os.path.join(
        "archivos_mascotas",
        nombre_archivo
    )

    shutil.copy2(ruta_archivo, ruta_destino)

    registros = []

    if os.path.exists("archivos_externos.json"):

        with open(
            "archivos_externos.json",
            "r",
            encoding="utf-8"
        ) as archivo:

            registros = json.load(archivo)

    registro = {
        "codigo_mascota": codigo_mascota,
        "nombre_mascota": nombre_mascota,
        "archivo": nombre_archivo
    }

    registros.append(registro)

    with open(
        "archivos_externos.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            registros,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print("Archivo asociado correctamente.")