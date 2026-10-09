# EJERCICIO 14:
# Enunciado: Meter en un match / case los ejercicios del 9 al 13, de forma que aparezca un
# menú con las 5 opciones para que el usuario decida que ejercicio o enunciado quiere
# ejecutar.

print("--- MENÚ DE EJERCICIOS ---")
print("9. Ejercicio 9")
print("10. Ejercicio 10")
print("11. Ejercicio 11")
print("12. Ejercicio 12")
print("13. Ejercicio 13")

opcion = int(input("Escribe un número del ejercicio 9 al 13: \n"))

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