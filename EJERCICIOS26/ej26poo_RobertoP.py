class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


# Vendedor y Gerente heredan los atributos de Empleado con super()
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

for empleado in empleados:
    print(f"{empleado.nombre}: {empleado.calcular_sueldo():.2f} €")
