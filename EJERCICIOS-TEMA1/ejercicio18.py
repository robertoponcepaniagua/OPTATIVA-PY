# EJERCICIO 18:
# Enunciado del Ejercicio: Sistema de Gestión para Frutería
# Una frutería local quiere digitalizar la gestión de sus datos utilizando las tres estructuras
# principales de colecciones en Python: listas, tuplas y diccionarios.
# Para garantizar la integridad y coherencia de los datos introducidos por el usuario, es
# obligatorio limpiar y normalizar todo texto leído por teclado mediante.strip().lower()
# (eliminando espacios sobrantes al inicio/final y convirtiendo las cadenas a minúsculas).
# Datos iniciales requeridos:
# • Lista de productos (productos ):["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
# • Tupla de información (info_tienda ):("Frutería La Huerta", "Calle Mayor 12", "912345678",2010)
# • Diccionario de precios (precios ):{"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20,"kiwis": 3.45, "fresas": 2.80}
# Requisitos de la aplicación:
# El programa debe tener un control de excepciones, con uso de ValueError e IndexError.
# El programa se ejecutará dentro de un buclewhile controlado por un menú principal con
# las opciones y sub-opciones siguientes (tendremos 4 opciones y al elegir una opción
# aparecerá un submenú con las subopciones identificadas con letras: a, b, c ...)
# 1. Gestión de Lista (Productos):
# a) Consultar: Mostrar todos los productos y la cantidad total almacenada.
# b) Añadir: Pedir el nombre del producto y agregarlo a la lista.
# c) Modificar: Mostrar los productos con sus índices, pedir la posición a modificar y el nuevo
# nombre.
# d) Eliminar: Pedir el índice del producto a borrar y eliminarlo.
# 2. Consulta de Tupla (Información de la Tienda):
# a) Mostrar por pantalla la tupla completa, su longitud mediante y acceder individualmente a
# cada uno de sus elementos usando índices (tupla[0] ,tupla[1] , etc.).
# 3. Gestión de Diccionario (Precios por Kilo):
# a) Consultar catálogo completo: Mostrar las parejas fruta/precio.
# b) Ver solo nombres / solo precios: Mostrar las frutas usando.keys() o únicamente los
# precios con.values() .
# c) Añadir o actualizar: Pedir el nombre de la fruta y su precio para guardarlo o actualizarlo.
# d) Eliminar: Pedir el nombre de la fruta a eliminar, comprobar si existe y borrarla.



# LISTA
productos = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
# TUPLA
info_tienda = ("Frutería La Huerta", "Calle Mayor 12", "912345678",2010)
# DICCIONARIO
precios = {"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20,"kiwis": 3.45, "fresas": 2.80}

# ValueError Y IndexError

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("Opción 1")
    print("Opción 2")
    print("Opción 3")
    print("Opción 4: Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:

        case 1:
            while True:
                print("\n--- SUBMENÚ 1 ---")
                print("1. Consultar")
                print("2. Añadir")
                print("3. Modificar")
                print("4. Eliminar")
                print("5. Volver")

                subopcion = int(input("Elige una opción: "))

                match subopcion:
                    case 1:
                        for producto in productos:
                            print(producto)

                        print(f"Total almacenado: {len(productos)}")
                    case 2:
                        producto_añadir = input("Que producto quieres añadir: ").lower().strip()
                        if producto_añadir in productos:
                            print("Ya está en la lista")
                        else:
                            productos.append(producto_añadir)
                            print("Añadido con exito")
                        
                    case 3:
                        for indice ,producto in enumerate(productos):
                            print(f"{indice} | {producto}")

                        modificar = int(input("Dime el indice que quieras modificar: "))

                        if productos[modificar] in productos:
                            nuevo_nombre = input("Dime el nuevo nombre: ")
                            productos[modificar] = nuevo_nombre

                    case 4:
                        for indice, producto in enumerate(productos):
                           print(f"{indice} | {producto}")
                        indice_eliminar = int(input("Que producto quieres eliminar (indice) : "))
                        productos.pop(indice_eliminar)

                    case 5:
                        break

                    case _:
                        print("Opción no válida.")

        case 2:
            while True:
                print("\n--- SUBMENÚ 2 ---")
                print("1. Consultar")
                print("2. Volver")

                subopcion = int(input("Elige una opción: "))

                match subopcion:
                    case 1:
                        for indice, info in enumerate(info_tienda):
                            print(f"{indice} | {info_tienda[indice]}")
                        print(f"Longitud: {len(info_tienda)}")
                    case 2:
                        break

                    case _:
                        print("Opción no válida.")

        case 3:
            while True:
                print("\n--- SUBMENÚ 3 ---")
                print("1. Consultar")
                print("2. Solo nombres y solo precios")
                print("3. Añadir o actualizar")
                print("4. Eliminar")
                print("5. Salir")

                subopcion = int(input("Elige una opción: "))

                match subopcion:
                    case 1:
                        for fruta in precios:
                            print(f"{fruta} | {precios[fruta]}")

                    case 2:
                        print("Solo nombres: ")
                        for fruta in precios:
                            print(f"{fruta}")
                        print("Solo precios: ")
                        for fruta in precios:
                            print(f"{precios[fruta]}")

                    case 3:
                        aux = input("Dime el nombre de la fruta: ")
                        aux_precio = int(input("Dime el precio de la fruta: "))

                        if aux in precios:
                            if aux_precio != precios[aux]:
                                precios[aux] = aux_precio
                        else:
                            precios[aux] = aux_precio

                    case 4:
                        aux = input("Dime el nombre de la fruta: ")
                        if aux in precios:
                            precios.pop(aux)
                        else:
                            print("No existe")
                    case 5:
                        break

                    case _:
                        print("Opción no válida.")

        case 4:
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida.")