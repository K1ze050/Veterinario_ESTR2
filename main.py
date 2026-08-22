#1. Registrar una mascota.
#2. Mostrar las mascotas registradas.
#3. Buscar una mascota por código.
#4. Registrar una consulta para una mascota.
#5. Consultar el historial de consultas de una mascota.
#6. Registrar una vacuna.
#7. Consultar las vacunas de una mascota.
#8. Asociar al menos un archivo externo a una mascota.
#9. Mostrar un resumen general del sistema.
#10. Salir.




def programa():
    print("------------------------------------")
    print(" Programa de registro veterinario ")
    print("------------------------------------")
    
    while True:
        print("\nMenú")
        print("1. Registrar una mascota")
        print("2. Mostrar las mascotas registradas")
        print("3. Buscar una mascota por código")
        print("4. Registrar una consulta para una mascota")
        print("5. Consultar el historial de consultas de una mascota")
        print("6. Registrar una vacuna")
        print("7. Consultar las vacunas de una mascota")
        print("8. Asociar al menos un archivo externo a una mascota")
        print("9. Mostrar un resumen general del sistema")
        print("10. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            from Registrar_Mascotas import mascotas_JSON
            mascotas_JSON()
        elif opcion == "2":
            from Mostrar_Mascotas import mostrar_JSON
            mostrar_JSON()
        elif opcion == "3":
            from Buscar_Mascotas import buscar_Codigo
            buscar_Codigo()
        elif opcion == "4":
            print("Registrar una consulta para una mascota")
        elif opcion == "5":
            print("Consultar el historial de consultas de una mascota")
        elif opcion == "6":
            print("Registrar una vacuna")
programa()