import json
def mascotas_JSON():
    productos = []
    cantidad = int(input("¿Cuantas mascotas se regitraran? "))

    for i in range(cantidad):
        print(f"\nProducto {i + 1}")
        codigo = input("Código: ")
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
        productos.append(mascota)

    
    with open("mascotas.json", "w", encoding="utf-8") as archivo:
        json.dump(
            productos,
            archivo,
            indent=4,          
            ensure_ascii=False  
        )
    print("\nInformación almacenada correctamente.")

