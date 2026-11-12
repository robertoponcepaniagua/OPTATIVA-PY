# El doble guion bajo indica que el atributo es privado.
class Empleado:
    def __init__(self, nombre, sueldo_base):
        # Usamos los setters para validar también los datos iniciales.
        self.setNombre(nombre)
        self.setSueldo_base(sueldo_base)

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    def getSueldo_base(self):
        return self.__sueldo_base

    def setSueldo_base(self, sueldo_base):
        if not 0 < sueldo_base < 200000:
            raise ValueError("El sueldo debe ser mayor que 0 y menor que 200000.")

        self.__sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.__sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.setComision(comision)

    def getComision(self):
        return self.__comision

    def setComision(self, comision):
        if not 0 <= comision < self.getSueldo_base() / 2:
            raise ValueError("La comisión debe ser positiva o cero y menor que el 50% del sueldo.")
        self.__comision = comision

    def calcular_sueldo(self):
        return self.getSueldo_base() + self.__comision


class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.setBono_gestion(bono_gestion)

    def getBono_gestion(self):
        return self.__bono_gestion

    def setBono_gestion(self, bono_gestion):
        if not 0 <= bono_gestion < self.getSueldo_base() / 2:
            raise ValueError("El bono debe ser positivo o cero y menor que el 50% del sueldo.")
        self.__bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.getSueldo_base() + self.__bono_gestion


# Ejemplo de uso
vendedor = Vendedor("Carlos", 1200, 350)
print(f"Comisión inicial: {vendedor.getComision():.2f} €")
vendedor.setComision(vendedor.getComision() + 100)
print(f"Comisión actualizada: {vendedor.getComision():.2f} €")
print(f"Sueldo total: {vendedor.calcular_sueldo():.2f} €")

# Capturamos el error para que el programa pueda continuar.
try:
    vendedor.setSueldo_base(-1200)
except ValueError as error:
    print(f"No se pudo modificar el sueldo: {error}")
print(f"El sueldo base sigue siendo: {vendedor.getSueldo_base():.2f} €")
