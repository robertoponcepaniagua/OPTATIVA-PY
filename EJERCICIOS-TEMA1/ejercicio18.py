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