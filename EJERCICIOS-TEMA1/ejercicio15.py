# EJERCICIO 15:
# Enunciado: Añadir al ejercicio anterior una opción para salir del programa y un bucle del
# que sólo saldrá el programa cuando el usuario seleccione dicha opción de salida.

opcion = -1

while opcion != 0:

    print("--- MENÚ DE EJERCICIOS ---")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("0. Salir")

    opcion = int(input("Escribe un número del ejercicio 9 al 13: \n"))

    if opcion > 13 or opcion < 9:
        print("Elige del ejercicio 9 al 13: ")
        continue

    match opcion:
        case 9:
            import ejercicio9
        case 10:
            import ejercicio10
        case 11:
            import ejercicio11
        case 12:
            import ejercicio12
        case 13:
            import ejercicio13
        case 0:
            exit