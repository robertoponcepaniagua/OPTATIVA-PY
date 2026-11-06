# EJERCICIO 17:
# Tienes una lista de datos de ventas donde cada registro es una tupla con el formato:
# ("producto", cantidad, precio_unitario). Los datos los metes directamente en el programa,
# pongamos 5 tuplas o lineas de la compra, ejemplo de tupla: manzanas, cantidad 3 kilos y
# precio 2,7 eur.
# El programa debe hacer lo siguiente:
# Convierta el nombre del producto a mayúsculas.
# Calcule el total gastado en cada producto (cantidad * precio) y redondee el resultado final
# a 2 decimales usando la función round().
# Muestre por pantalla el total de esa compra y el total de la suma de todas las cantidades.


# ("producto", cantidad, precio_unitario)
frutas = [
    ("manzanas", 3, 2.7),
    ("kiwis", 10, 4.2),
    ("melocotones", 4, 2.2),
    ("limones", 6, 1.3),
    ("peras", 4, 2.4),
]

total_gastado_producto = []

total_compra = 0
total_cantidades = 0

for producto, cantidad, precioUnitario in frutas:
    nombreMayusculas = producto.upper()

    precio_producto = cantidad * precioUnitario

    total_cantidades += cantidad
    total_compra += precio_producto

    total_gastado_producto.append(
        (nombreMayusculas, round(precio_producto, 2))
    )

# Mostrar el importe de cada producto
for nombre, precio in total_gastado_producto:
    print(f"Nombre: {nombre} | Precio total: {precio:.2f} €")

print("----------------------------")
print(f"Total de cantidades: {total_cantidades}")
print(f"Total de la compra: {round(total_compra, 2):.2f} €")