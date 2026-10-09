# EJERCICIO 10
# Enunciado: Escribe un programa que calcule el área de un círculo. El programa deberá
# pedir al usuario que introduzca el radio del círculo y, utilizando la fórmula Área = Pi *
# radio^2

import math

radio = float(input("Escribe el radio del circulo: "))

area = math.pi * (radio ** 2)

print(f"El área es: {area}")