# En esta tarea teneis que incluir vuestras prácticas sobre lista de listas y diccionario de listas, con ejemplos vuestros propios y sobre esos ejemplos poneis opciones de imprimir, añadir elementos, recorrer con un for, etc ... 

# Sobre los for, que son muy importantes practicar con lo que ya tenéis en los apuntes:

# 1. Lista
# frutas = ["manzana", "banana", "cereza"]
# for fruta in frutas:
# print(fruta.upper())
# Salida: MANZANA | BANANA | CEREZA
# 2. Tupla
# coordenadas = (10, 20, 30)
# for punto in coordenadas:
# print(f"Punto: {punto}")
# Salida: Punto: 10 | Punto: 20 | Punto: 30
# 3. Diccionario con .items() (obtiene clave y valor juntos)
# precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
# for producto, precio in precios.items():
# print(f"{producto}: {precio}€")
# Salida: pan: 1.2€ | leche: 0.9€ | café: 2.5€
# 4. Diccionario sin .items() (recorre solo las claves)
# precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
# for producto in precios:
# print(f"{producto} -> {precios[producto]}€")
# Salida: pan -> 1.2€ | leche -> 0.9€ | café -> 2.5€

# 5. Diccionario con .values() (recorre solo los valores)
# precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
# for precio in precios.values:
# print(precio)
# Salida: 1.2€ | 0.9€ | 2.5€
# Altenativa: print(f”Precio: {precio})
# Salida: Precio: 1.2€ | Precio: 0.9€ | Precio: 2.5€

# 6. Cadena de caracteres
# texto = "Python"
# for letra in texto:
# print(letra * 2)
# Salida: PP | yy | tt | hh | oo | nn


frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta.upper())


coordenadas = (10, 20, 30)
for punto in coordenadas:
    print(f"Punto: {punto}")


precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
for producto, precio in precios.items():
    print(f"{producto}: {precio}€")

precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
for producto in precios:
    print(f"{producto} -> {precios[producto]}€")

precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
for precio in precios.values:
    print(precio)

texto = "Python"
for letra in texto:
    print(letra * 2)