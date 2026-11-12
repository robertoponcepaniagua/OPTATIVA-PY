# Ejercicio 26 poo
# Nombre archivo python: ej26poo_vuestronombreyprimeraletradelprimerapellido.py
# Sistema de Empleados de una Tienda
# Queremos modelar el cálculo del sueldo mensual de los empleados de una tienda:
# Clase Base (Empleado):
# Atributos: nombre y sueldo_base.
# Método: calcular_sueldo(), que por defecto devuelve únicamente el sueldo_base.
# Clase Hija 1 (Vendedor) — Herencia:
# Hereda de Empleado.
# Atributo propio: comision (un importe fijo extra por sus ventas del mes).
# Sobrescribe calcular_sueldo() para sumar la comisión al sueldo base.
# Clase Hija 2 (Gerente) — Herencia:
# Hereda de Empleado.
# Atributo propio: bono_gestion (un porcentaje o extra fijo por liderar el equipo).
# Sobrescribe calcular_sueldo() para sumar el bono al sueldo base.
# Polimorfismo:
# Crea una lista que contenga objetos mezclados (Empleado, Vendedor, Gerente).
# Empleada: Ana, 1200 eur
# Vendedor: Carlos, 1200 eur, 350 eur
# Gerente: Marta, 2000 eur, 500 eur
# Escribe por pantalla el sueldo de cada empleado

# La clase padre guarda los datos comunes de todos los empleados.
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


# Vendedor y Gerente heredan los atributos de Empleado con super().
class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision


class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion


# Ejemplo de uso
empleados = [
    Empleado("Ana", 1200),
    Vendedor("Carlos", 1200, 350),
    Gerente("Marta", 2000, 500),
]

# Polimorfismo: el mismo método calcula un sueldo según el tipo de empleado.
for empleado in empleados:
    print(f"{empleado.nombre}: {empleado.calcular_sueldo():.2f} €")
