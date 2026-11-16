# Las propiedades permiten leer y modificar atributos privados con validación
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):
        if not 0 < sueldo_base < 200000:
            raise ValueError("El sueldo debe ser mayor que 0 y menor que 200000.")

        self.__sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self, comision):
        if not 0 <= comision < self.sueldo_base / 2:
            raise ValueError("La comisión debe ser positiva o cero y menor que el 50% del sueldo.")
        self.__comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision


class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion

    @property
    def bono_gestion(self):
        return self.__bono_gestion

    @bono_gestion.setter
    def bono_gestion(self, bono_gestion):
        if not 0 <= bono_gestion < self.sueldo_base / 2:
            raise ValueError("El bono debe ser positivo o cero y menor que el 50% del sueldo.")
        self.__bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion


# Ejemplo de uso
vendedor = Vendedor("Carlos", 1200, 350)
print(f"Comisión inicial: {vendedor.comision:.2f} €")

vendedor.comision += 100
print(f"Comisión actualizada: {vendedor.comision:.2f} €")
print(f"Sueldo total: {vendedor.calcular_sueldo():.2f} €")

try:
    vendedor.sueldo_base = -1200
except ValueError as error:
    print(f"No se pudo modificar el sueldo: {error}")
print(f"El sueldo base sigue siendo: {vendedor.sueldo_base:.2f} €")
