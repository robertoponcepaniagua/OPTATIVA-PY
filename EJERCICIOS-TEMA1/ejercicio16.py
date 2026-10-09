# EJERCICIO 16:
# Enunciado: Añade al ejercicio anterior un control de errores o control de excepciones con
# try/except, incluye reglas de negocio con raise, por ejemplo una distancia en metros no
# puede ser negativa y las excepciones de ValueError y ZeroDivisionError.

import math  # Buena práctica: los imports se dejan arriba del todo

opcion = -1

while opcion != 0:

    print("--- MENÚ DE EJERCICIOS ---")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("0. Salir")

    try:
        # Si el usuario escribe texto aquí, saltará directamente al 'except ValueError'
        opcion = int(input("Escribe un número del ejercicio 9 al 13: \n"))

        if opcion == 0:
            print("Saliendo del programa...")
            break

        if opcion > 13 or opcion < 9:
            print("Elige del ejercicio 9 al 13.")
            continue

        # Ponemos el match-case DENTRO del try para que controle los errores de cada caso
        match opcion:
            case 9:
                centimetros = float(input("Escribe los cm: "))

                if centimetros < 0:
                    raise ValueError("Los centímetros no pueden ser negativos.")

                metros = centimetros / 100
                print(f" {centimetros}cm a metros: {metros}m")

            case 10:
                radio = float(input("Escribe el radio del círculo: "))

                if radio < 0:
                    raise ValueError("El radio no puede ser < 0.")

                area = math.pi * (radio ** 2)
                print(f"El área es: {area}")

            case 11:
                costeComida = float(input("Escribe el coste de la comida: "))

                if costeComida < 0:
                    raise ValueError("El coste de la comida no puede ser < 0.")

                porcentajePropina = int(input("Escribe el porcentaje de la propina: "))

                if porcentajePropina < 0:
                    raise ValueError("El porcentaje no puede ser < 0.")

                calculo = costeComida + ((costeComida * porcentajePropina) / 100)
                print(f"El coste total es: {calculo}")

            case 12:
                peso = float(input("Cuánto pesas (kg): "))
                if peso < 0:
                    raise ValueError("El peso no puede ser < 0.")

                altura = float(input("Cuánto mides (m): "))
                if altura < 0:
                    raise ValueError("La altura no puede ser < 0.")
                
                # REGLA DE NEGOCIO: Validar la división por cero antes de hacer el cálculo
                if altura == 0:
                    raise ZeroDivisionError("La altura no puede ser 0 metros.")

                imc = peso / (altura ** 2)
                print(f"Peso: {peso} Altura: {altura} IMC: {imc}")

            case 13:
                nombre = input("Escribe tu nombre: \n")
                if not nombre.strip():
                    raise ValueError("El nombre no puede estar vacío.")

                apellido = input("Escribe tu apellido: \n")
                if not apellido.strip():
                    raise ValueError("El apellido no puede estar vacío.")

                print(f"Nombre completo: {nombre} {apellido}")

    except ValueError as e:
        # Captura datos mal introducidos
        print(f"Error de valor: {e}")

    except ZeroDivisionError as e:
        # Captura el error de dividir entre cero
        print(f"Error aritmético: {e}")

    except Exception as e:
        # Captura cualquier otro imprevisto
        print(f"Ocurrió un error inesperado: {e}")
