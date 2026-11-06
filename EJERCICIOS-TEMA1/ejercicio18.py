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
info_tienda = ("Frutería La Huerta", "Calle Mayor 12", "912345678", 2010)

# DICCIONARIO
precios = {
    "manzanas": 1.50,
    "plátanos": 2.10,
    "naranjas": 1.20,
    "kiwis": 3.45,
    "fresas": 2.80
}


while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestión de lista (productos)")
    print("2. Información de la tienda")
    print("3. Gestión de diccionario (precios)")
    print("4. Salir")

    try:
        opcion = int(input("Elige una opción: "))

        match opcion:

            # 1. GESTIÓN DE LISTA
            case 1:
                while True:
                    print("\n--- SUBMENÚ 1: PRODUCTOS ---")
                    print("a. Consultar")
                    print("b. Añadir")
                    print("c. Modificar")
                    print("d. Eliminar")
                    print("e. Volver")

                    subopcion = input("Elige una opción: ").strip().lower()

                    match subopcion:

                        case "a":
                            print("\n--- LISTA DE PRODUCTOS ---")

                            for indice, producto in enumerate(productos):
                                print(f"{indice} | {producto}")

                            print(f"Total almacenado: {len(productos)}")

                        case "b":
                            producto_añadir = input(
                                "¿Qué producto quieres añadir?: "
                            ).strip().lower()

                            if not producto_añadir:
                                print("El nombre no puede estar vacío.")

                            elif producto_añadir in productos:
                                print("Ese producto ya está en la lista.")

                            else:
                                productos.append(producto_añadir)
                                print("Producto añadido con éxito.")

                        case "c":
                            if not productos:
                                print("No hay productos para modificar.")
                                continue

                            for indice, producto in enumerate(productos):
                                print(f"{indice} | {producto}")

                            try:
                                modificar = int(
                                    input("Introduce el índice que quieres modificar: ")
                                )

                                producto_actual = productos[modificar]

                                nuevo_nombre = input(
                                    "Introduce el nuevo nombre: "
                                ).strip().lower()

                                if not nuevo_nombre:
                                    print("El nombre no puede estar vacío.")

                                elif (
                                    nuevo_nombre != producto_actual
                                    and nuevo_nombre in productos
                                ):
                                    print("Ese producto ya existe.")

                                else:
                                    productos[modificar] = nuevo_nombre
                                    print("Producto modificado correctamente.")

                            except ValueError:
                                print("Debes introducir un número entero.")

                            except IndexError:
                                print("El índice no existe.")

                        case "d":
                            if not productos:
                                print("No hay productos para eliminar.")
                                continue

                            for indice, producto in enumerate(productos):
                                print(f"{indice} | {producto}")

                            try:
                                indice_eliminar = int(
                                    input("Introduce el índice que quieres eliminar: ")
                                )

                                producto_eliminado = productos.pop(indice_eliminar)

                                print(f"Producto eliminado: {producto_eliminado}")

                            except ValueError:
                                print("Debes introducir un número entero.")

                            except IndexError:
                                print("El índice no existe.")

                        case "e":
                            break

                        case _:
                            print("Opción no válida.")

            # 2. INFORMACIÓN DE LA TIENDA
            case 2:
                while True:
                    print("\n--- SUBMENÚ 2: INFORMACIÓN ---")
                    print("a. Consultar información")
                    print("b. Volver")

                    subopcion = input("Elige una opción: ").strip().lower()

                    match subopcion:

                        case "a":
                            print("\n--- INFORMACIÓN DE LA TIENDA ---")
                            print(f"Tupla completa: {info_tienda}")
                            print(f"Longitud: {len(info_tienda)}")

                            print(f"Nombre: {info_tienda[0]}")
                            print(f"Dirección: {info_tienda[1]}")
                            print(f"Teléfono: {info_tienda[2]}")
                            print(f"Año de fundación: {info_tienda[3]}")

                        case "b":
                            break

                        case _:
                            print("Opción no válida.")

            # 3. GESTIÓN DE DICCIONARIO
            case 3:
                while True:
                    print("\n--- SUBMENÚ 3: PRECIOS ---")
                    print("a. Consultar catálogo completo")
                    print("b. Mostrar nombres y precios")
                    print("c. Añadir o actualizar")
                    print("d. Eliminar")
                    print("e. Volver")

                    subopcion = input("Elige una opción: ").strip().lower()

                    match subopcion:

                        case "a":
                            print("\n--- CATÁLOGO COMPLETO ---")

                            for fruta, precio in precios.items():
                                print(f"{fruta} | {precio:.2f} €/kg")

                        case "b":
                            print("\n--- NOMBRES DE LAS FRUTAS ---")

                            for fruta in precios.keys():
                                print(fruta)

                            print("\n--- PRECIOS POR KILO ---")

                            for precio in precios.values():
                                print(f"{precio:.2f} €/kg")

                        case "c":
                            fruta = input(
                                "Introduce el nombre de la fruta: "
                            ).strip().lower()

                            if not fruta:
                                print("El nombre no puede estar vacío.")
                                continue

                            try:
                                precio = float(
                                    input("Introduce el precio por kilo: ")
                                )

                                if precio < 0:
                                    print("El precio no puede ser negativo.")

                                else:
                                    precios[fruta] = precio
                                    print("Precio guardado correctamente.")

                            except ValueError:
                                print("Debes introducir un precio numérico válido.")

                        case "d":
                            fruta = input(
                                "Introduce la fruta que quieres eliminar: "
                            ).strip().lower()

                            if fruta in precios:
                                del precios[fruta]
                                print("Fruta eliminada correctamente.")

                            else:
                                print("Esa fruta no existe en el catálogo.")

                        case "e":
                            break

                        case _:
                            print("Opción no válida.")

            # 4. SALIR
            case 4:
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida.")

    except ValueError:
        print("Debes introducir un número entero para elegir la opción.")