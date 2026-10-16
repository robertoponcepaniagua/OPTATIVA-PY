MARCAS_MODELOS = { "SEAT": ["Ibiza", "Leon", "Ateca", "Arona"], "Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"] }
ventas = [
["SEAT", "Ibiza", 2024, 2023, 18000], ["SEAT", "Ibiza", 2024, 2024, 18500], ["SEAT", "Ibiza", 2024, 2024, 19000],
["SEAT", "Ibiza", 2025, 2024, 19500], ["SEAT", "Ibiza", 2025, 2025, 20000], ["SEAT", "Ibiza", 2025, 2025, 20200],
["SEAT", "Ibiza", 2026, 2025, 20500], ["SEAT", "Ibiza", 2026, 2026, 21000], ["SEAT", "Ibiza", 2026, 2026, 21500],
["SEAT", "Leon", 2024, 2024, 24000], ["SEAT", "Leon", 2024, 2024, 24500], ["SEAT", "Leon", 2024, 2023, 23800],
["SEAT", "Leon", 2025, 2025, 25500], ["SEAT", "Leon", 2025, 2025, 26000], ["SEAT", "Leon", 2025, 2024, 25200],
["SEAT", "Leon", 2026, 2026, 27000], ["SEAT", "Leon", 2026, 2026, 27500], ["SEAT", "Leon", 2026, 2025, 26800],
["SEAT", "Ateca", 2024, 2024, 28000], ["SEAT", "Ateca", 2025, 2025, 29500], ["SEAT", "Ateca", 2026, 2026, 31000],
["SEAT", "Arona", 2024, 2024, 21000], ["SEAT", "Arona", 2025, 2025, 22000], ["SEAT", "Arona", 2026, 2026, 23000],
["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500], ["Toyota", "Corolla", 2024, 2023, 25800],
["Toyota", "Corolla", 2025, 2025, 27500], ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500], ["Toyota", "Corolla", 2026, 2025, 28800],
["Toyota", "Yaris", 2024, 2024, 20000], ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500], ["Toyota", "RAV4", 2026, 2026, 41000],
["Toyota", "C-HR", 2024, 2024, 31000], ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000]
]

option = 0;

while True:
    print("==========================================")
    print("SISTEMA DE GESTIÓN DE VENTAS")
    print("==========================================")
    print("1.- Dar de alta una nueva venta")
    print("2.- Resumen de ventas (Marca_Modelo_Año)")
    print("3.- Resumen de ventas (Marca_Modelo - Todos los años)")
    print("4.- Resumen de ventas (Marca - Todos los modelos y años)")
    print("5.- Salir del programa")

    option = int(input("Elige un número del 1 al 5: \n"))

    
    match(option):
        case 1:
            print("1.- Dar de alta una nueva venta")
            print("------------------")
            print("Marcas disponibles")
            print("------------------")
            
            for marca in MARCAS_MODELOS:
                print(f"| {marca}")

            marcaElegida = input("Escribe el nombre de la marca que deseas: \n")

            
            if marcaElegida in MARCAS_MODELOS:
                print(f'Has elegido : {marcaElegida}')
            else:
                print("Marca no valida")

            print("---------------Modelos---------------")
            for modelo in MARCAS_MODELOS[marcaElegida]:
                print(f"| {modelo}")

            modeloElegido = input("Escribe el modelo que deseas: \n")

            if modeloElegido in MARCAS_MODELOS[marcaElegida]:
                print(f"Marca y Modelo seleccionados: {marcaElegida} | {modeloElegido}")
            else:
                print("Modelo no encontrado")

            # VALIDACIONES DE AÑO DE VENTA

            while True:
                try:
                    anio_venta = int(input("Introduce el año de la venta (2024 - 2026)"))
                    if(anio_venta > 2026 or anio_venta < 2024):
                        print("Bien")
                    else:
                        print("Tiene que ser entre 2024 y 2026")
                except:
                    print("El número debe de ser entero")

                try:
                    anio_fabricacion = int(input(f"Introduce el año de fabricación (1990 - {anio_venta})"))
                    if(anio_fabricacion >= 1990 and anio_fabricacion <= anio_venta):
                        print("Bien")
                    else:
                        print(f"El año de fabricación tiene que ser entre (1990 - {anio_venta})")
                except:
                    print("El número debe de ser entero")

                try:
                    precio = float(input("Dime el precio: (1.000 - 100.000)"))
                except:
                    print("El numero debe de ser un float")



        case 2:
            print("2.- Resumen de ventas (Marca_Modelo_Año)")
        case 3:
            print("3.- Resumen de ventas (Marca_Modelo - Todos los años)")
        case 4:
            print("4.- Resumen de ventas (Marca - Todos los modelos y años)")
        case 5:
            print("5.- Salir del programa")

    