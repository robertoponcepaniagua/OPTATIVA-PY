from pathlib import Path

import pandas as pd


# PARTE 1: orient="records"
nombre_archivo = Path(__file__).with_name("Ej27_Pandas_RobertoP.xlsx")
nombre_hoja = "Alumnos"
datos = {}

excel = pd.ExcelFile(nombre_archivo)
df = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=None)
df = df.fillna("")

print("\n========== PARTE 1: RECORDS ==========\n")
print("DataFrame leído:")
print(df)

datos[nombre_hoja] = df.to_dict(orient="records")
print("\nDiccionario completo:")
print(datos)

print("\nAlumnos, dato a dato:")
for alumno in datos[nombre_hoja]:
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")
    print("---")


# PARTE 2: orient="dict", "index" y "list" (sin índice propio)
print("\n========== PARTE 2: OTROS ORIENT ==========\n")

# 2.1: Diccionario de diccionarios: {columna: {indice: valor}}
datos_dict = df.to_dict(orient="dict")
print("\n--- orient='dict': estructura completa ---")
print(datos_dict)
print("\nRecorrido dato a dato:")
for columna, filas in datos_dict.items():
    print(f"\nColumna: {columna}")
    for indice, valor in filas.items():
        print(f"Fila {indice}: {valor}")

# 2.2: Diccionario de diccionarios: {indice: {columna: valor}}
datos_index = df.to_dict(orient="index")
print("\n--- orient='index': estructura completa ---")
print(datos_index)
print("\nRecorrido dato a dato:")
for indice, alumno in datos_index.items():
    print(f"\nFila {indice}:")
    for columna, valor in alumno.items():
        print(f"{columna}: {valor}")

# 2.3: Diccionario de listas: {columna: [valor1, valor2, ...]}
datos_list = df.to_dict(orient="list")
print("\n--- orient='list': estructura completa ---")
print(datos_list)
print("\nRecorrido dato a dato:")
for columna, lista_valores in datos_list.items():
    print(f"\nColumna: {columna}")
    for valor in lista_valores:
        print(f"{valor}")


# PARTE 3: id_persona como índice
print("\n========== PARTE 3: ID_PERSONA COMO ÍNDICE ==========\n")

df_indice = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=0)
df_indice = df_indice.fillna("")
print("DataFrame con id_persona como índice:")
print(df_indice)

# 3.1: {columna: {id_persona: valor}}
datos_dict_id = df_indice.to_dict(orient="dict")
print("\n--- orient='dict' con id_persona: estructura completa ---")
print(datos_dict_id)
print("\nRecorrido dato a dato:")
for columna, alumnos in datos_dict_id.items():
    print(f"\nColumna: {columna}")
    for id_persona, valor in alumnos.items():
        print(f"{id_persona}: {valor}")

# 3.2: {id_persoa: {columna: valor}}
datos_index_id = df_indice.to_dict(orient="index")
print("\n--- orient='index' con id_persona: estructura completa ---")
print(datos_index_id)
print("\nRecorrido dato a dato:")
for id_persona, datos_alumno in datos_index_id.items():
    print(f"\nAlumno {id_persona}:")
    for columna, valor in datos_alumno.items():
        print(f"{columna}: {valor}")

print("\n========== EJERCICIO TERMINADO ==========")

