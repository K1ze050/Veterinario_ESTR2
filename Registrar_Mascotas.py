import json

def mascotas_JSON():

    mascotas = []

    try:
        with open("mascotas.json", "r", encoding="utf-8") as archivo:
            mascotas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        mascotas = []

    cantidad = int(input("¿Cuantas mascotas se registraran? "))

    for i in range(cantidad):

        print(f"\nMascota {i + 1}")

        codigo = input("Código: ")

        # Comprobar que el código no exista
        while any(mascota["codigo"] == codigo for mascota in mascotas):
            print("Ya existe una mascota con ese código.")
            codigo = input("Ingrese otro código: ")

        nombre = input("Nombre: ")
        especie = input("Especie: ")
        raza = input("Raza: ")
        fecha = input("Fecha de nacimiento del perro (Escribe en texto): ")
        propietario = input("Nombre del propietario: ")
        telefono = int(input("Ingresa tu numero de telefono: "))
        estado = input("Estado actual: ")

        mascota = {
            "codigo": codigo,
            "nombre": nombre,
            "especie": especie,
            "raza": raza,
            "fecha": fecha,
            "propietario": propietario,
            "telefono": telefono,
            "estado": estado
        }

        mascotas.append(mascota)

    with open("mascotas.json", "w", encoding="utf-8") as archivo:
        json.dump(
            mascotas,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print("\nInformación almacenada correctamente.")

