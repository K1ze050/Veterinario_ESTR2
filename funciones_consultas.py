import json


def cargar_consultas():
    try:
        with open("consultas.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_consultas(consultas):
    with open("consultas.json", "w", encoding="utf-8") as archivo:
        json.dump(consultas, archivo, indent=2, ensure_ascii=False)


def generar_codigo_consulta(consultas):
    numero = len(consultas) + 1
    return f"C{numero:03d}"


def registrar_consulta(codigo_mascota):
    consultas = cargar_consultas()

    fecha = input("Fecha (AAAA-MM-DD): ")
    motivo = input("Motivo: ")
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento: ")

    while True:
        try:
            costo = float(input("Costo: Q"))
            break
        except ValueError:
            print("Ingresa un número válido para el costo.")

    nueva_consulta = {
        "codigo_consulta": generar_codigo_consulta(consultas),
        "codigo_mascota": codigo_mascota,
        "fecha": fecha,
        "motivo": motivo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "costo": costo
    }

    consultas.append(nueva_consulta)
    guardar_consultas(consultas)

    print(f"\nConsulta {nueva_consulta['codigo_consulta']} registrada correctamente para la mascota {codigo_mascota}.")


def consultar_historial(codigo_mascota):
    consultas = cargar_consultas()

    historial = [c for c in consultas if c["codigo_mascota"] == codigo_mascota]

    if not historial:
        print(f"\nNo hay consultas registradas para la mascota {codigo_mascota}.")
        return

    print(f"\n===== HISTORIAL DE CONSULTAS - {codigo_mascota} =====")
    for consulta in historial:
        print(f"\nCódigo: {consulta['codigo_consulta']}")
        print(f"Fecha: {consulta['fecha']}")
        print(f"Motivo: {consulta['motivo']}")
        print(f"Diagnóstico: {consulta['diagnostico']}")
        print(f"Tratamiento: {consulta['tratamiento']}")
        print(f"Costo: Q{consulta['costo']:.2f}")