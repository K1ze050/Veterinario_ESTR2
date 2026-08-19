# funcion # 6
import csv

with open(
    "vacunas.csv",
    "w",
    newline="",
    encoding="utf-8",
) as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Vacuna", "Fecha", "Próxima dosis", "Veterinario Responsable"])
    escritor.writerow(["Rabia", "19-08-2026", "25-08-2026", "Dr. Juanito"])
    escritor.writerow(["Bortedella", "19-08-2026", "25-08-2026", "Dr. Simi"])