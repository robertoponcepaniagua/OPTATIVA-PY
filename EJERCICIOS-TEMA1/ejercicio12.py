# EJERCICIO 12
# Enunciado: Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario.
# El programa deberá pedir al usuario su peso (en kilogramos) y su altura (en metros), y
# luego calcular su IMC usando la fórmula: IMC = Peso / Altura^2

peso = float(input("Cuanto pesas (kg): "))

altura = float(input("Cuanto mides (m): "))

imc = peso / (altura ** 2)

print(f"Peso: {peso} Altura: {altura} IMC: {imc}")