import pandas as pd

nombre_archivo = "Ej 27 Pandas 1 Datos.xlsx"
nombre_hoja = "Alumnos"

datos = {}

excel = pd.ExcelFile(nombre_archivo)

df = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=None)

df = df.fillna("")

print(df)

datos[nombre_hoja] = df.to_dict(orient="records")

print(datos)

for alumno in datos[nombre_hoja]:
    for dato in alumno:
        print("")