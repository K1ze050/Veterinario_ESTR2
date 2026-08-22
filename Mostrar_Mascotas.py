import json

def mostrar_JSON():
    with open("mascotas.json", "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    print("\nMASCOTAS REGISTRADAS ACTUALMENTE")
    for mascotas in productos:
        print(f'\nCódigo: {mascotas["codigo"]}')
        print(f'Nombre: {mascotas["nombre"]}')
        print(f'Especie: {mascotas["especie"]}')
        print(f'Raza: {mascotas["raza"]}')
        print(f'Fecha de nacimiento: {mascotas["fecha"]}')
        print(f'Propietario del perro: {mascotas["propietario"]}') 
        print(f'Numero de teléfono: {mascotas["telefono"]}') 
        print(f'Estado actual del perro en clinica: {mascotas["estado"]}')      