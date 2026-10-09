# EJERCICIO 17c:
# Escribe un programa en Python que inicialice una lista llamadafrutas con los
# elementos"manzana" ,"platano" y"naranja" .
# El programa debe presentar de forma continua un menú dentro de un buclewhile
# con las siguientes opciones numéricas:
# 1. Ver lista completa: Muestra la lista completa por pantalla.
# 2. Ver un elemento por índice: Pide una posición al usuario y muestra el elemento
# guardado en dicho índice.
# 3. Añadir elemento: Pide el nombre de una nueva fruta y la añade al final de la lista.
# 4. Modificar elemento: Pide la posición que se desea cambiar y el nuevo nombre para
# actualizar ese valor en la lista.
# 5. Borrar elemento: Pide el índice del elemento que se quiere eliminar y lo quita de la
# lista.
# 6. Salir: Muestra un mensaje de despedida y finaliza la ejecución del programa.

llamadafrutas = ["manzana", "platano", "naranja"]

opcion = None;

while(opcion != 6):
    print("--- MENÚ DE FRUTAS ---")
    print("1. Ver lista completa")
    print("2. Ver un elemento por índice")
    print("3. Añadir elemento")
    print("4. Modificar elemento")
    print("5. Borrar elemento")
    print("6. Salir")
    print("-----------------------\n")
    
    opcion = int(input("Elige un número del 1 al 6:\n"))
    match opcion:
        case 1:
            for fruta in llamadafrutas:
                print(f"Fruta {fruta}")
        case 2:
            indice = int(input("Introduce el índice (0, 1, 2...): "))
            print(f"La fruta en la posición {indice} es: {llamadafrutas[indice]}")

        case 3:
            añadirElemento = input("Dime el nombre de una fruta: \n")
            llamadafrutas.append(añadirElemento)
        case 4:
            for fruta in llamadafrutas:
                print(f"Fruta {fruta}")
            indice = int(input("Introduce la fruta que quieras modificar (0, 1, 2...): "))

            nombreNuevo = input("Dime el nombre nuevo: \n")
            llamadafrutas[indice] = nombreNuevo
        case 5:
            print("5: ")
        case 6:
            break
    