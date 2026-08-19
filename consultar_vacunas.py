#funcion 7
import csv

with open(
    "vacunas.csv",
    "r",
    newline="",
    encoding="utf-8",
) as archivo:
    
    lector = csv.reader(archivo)
    
    for fila in lector:
        print(fila)