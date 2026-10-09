# EJERCICIO 11
# Enunciado: Escribe un programa que calcule el importe total a pagar en un restaurante. El
# programa deberá pedir al usuario el coste de la comida y el porcentaje de propina que
# quiere dejar, y luego devolver el importe total.

costeComida = float(input("Escibe el coste de la comida: "))

porcentajePropina = int(input("Escribe el procentaje de la propina: "))

calculo = costeComida + ((costeComida * porcentajePropina) / 100)

print(f"El coste total es: {calculo}")