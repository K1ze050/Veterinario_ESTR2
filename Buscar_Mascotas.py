import json

def buscar_Codigo():
    try:
        with open("mascotas.json", "r", encoding="utf-8") as archivo:
            lista_mascotas = json.load(archivo)
    except FileNotFoundError:
        print("El archivo mascotas.json no existe o no se encuentra en esta ruta.")
        return
    
    cod = input("Ingresa el código de tu mascota: ")

    encontrado = False

    for mascota in lista_mascotas:
        if mascota["codigo"] == cod:
            print("\nMASCOTA EN REGISTRO")
            print(f"Nombre: {mascota['nombre']}")
            print(f"Especie: {mascota['especie']}")
            print(f"Raza: {mascota['raza']}")
            print(f"Propietario: {mascota['propietario']}")
            encontrado = True
            break

    if not encontrado:
        print("\nTu mascota no está en el registro.")
buscar_Codigo()