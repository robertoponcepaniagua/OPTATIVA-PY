# 1. Lista
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta.upper())
    print(fruta.lower())
    print(fruta.capitalize())
    print(fruta.title())

print("--------------------------------------------")
# 2. Tupla
coordenadas = (10, 20, 30)

for punto in coordenadas:
    print(f"Punto: {punto}")
    print(punto * 2)

print("--------------------------------------------")
# 3. Diccionario con .items()
precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}

for producto, precio in precios.items():
    print(f"{producto}: {precio}€")
    print(f"{producto.capitalize()} cuesta {precio}€")

print("--------------------------------------------")
# 4. Diccionario sin .items()
precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}

for producto in precios:
    print(f"{producto} -> {precios[producto]}€")
    print(producto.upper())
    print(f"El producto {producto} cuesta {precios[producto]}€")

print("--------------------------------------------")
# 5. Diccionario con .values()
precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}

for precio in precios.values():
    print(precio)
    print(f"Precio: {precio}€")

print("--------------------------------------------")
# 6. Cadena de caracteres
texto = "Python"

for letra in texto:
    print(letra * 2)
    print(letra.upper())
    print(f"Letra: {letra}")

print("--------------------------------------------")