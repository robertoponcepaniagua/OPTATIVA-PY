from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    # Las clases hijas deben implementar este método.
    @abstractmethod
    def calcular_sueldo(self):
        pass

    # __str__ indica qué texto se muestra al hacer print del objeto.
    def __str__(self):
        return f"Empleado: {self.nombre} - Sueldo: {self.calcular_sueldo()} €"


# EmpleadoBase representa a los empleados sin comisión ni bono.
class EmpleadoBase(Empleado):
    def calcular_sueldo(self):
        return self.sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision

    def __str__(self):
        return f"Vendedor: {self.nombre} - Sueldo: {self.calcular_sueldo()} €"


class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion

    def __str__(self):
        return f"Gerente: {self.nombre} - Sueldo: {self.calcular_sueldo()} €"


class Departamento:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def agregar_empleados(self, empleado):
        self.empleados.append(empleado)

    def nomina_total(self):
        # Sumamos el sueldo del gerente y el de los demás empleados.
        total = self.gerente.calcular_sueldo()
        for empleado in self.empleados:
            total += empleado.calcular_sueldo()
        return total

    def __str__(self):
        resultado = f"Departamento: {self.nombre}\n"
        resultado += str(self.gerente) + "\n"
        for empleado in self.empleados:
            resultado += str(empleado) + "\n"
        resultado += f"Nómina total: {self.nomina_total()} €"
        return resultado


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def agregar_departamento(self, departamento):
        if departamento not in self.departamentos:
            self.departamentos.append(departamento)

    def transferir_empleado(self, empleado, departamento_nuevo):
        if departamento_nuevo not in self.departamentos:
            print("El departamento de destino no pertenece a la empresa.")
            return

        # Buscamos al empleado en los departamentos de la empresa.
        for departamento in self.departamentos:
            if empleado in departamento.empleados:
                departamento.empleados.remove(empleado)
                departamento_nuevo.agregar_empleados(empleado)
                print(f"{empleado.nombre} se ha trasladado a {departamento_nuevo.nombre}.")
                return

        print("No se ha encontrado al empleado.")

    def calcular_nomina_global(self):
        total = 0
        for departamento in self.departamentos:
            total += departamento.nomina_total()
        return total

    def imprimir_informacion(self):
        print(f"Empresa: {self.nombre}")
        for departamento in self.departamentos:
            print()
            print(departamento)
        print(f"\nNómina global: {self.calcular_nomina_global()} €")


# Creamos los empleados y los departamentos.
ana = EmpleadoBase("Ana", 1200)
carlos = Vendedor("Carlos", 1200, 350)
marta = Gerente("Marta", 2000, 500)

nacional = Departamento("Nacional", marta)
internacional = Departamento("Internacional", Gerente("John", 2500, 850))
# En este apartado el enunciado repite "Nacional", pero es Nuevos Productos.
nuevos_productos = Departamento("Nuevos Productos", Gerente("Marta", 2000, 450))

nacional.agregar_empleados(ana)
nacional.agregar_empleados(carlos)

internacional.agregar_empleados(Vendedor("Sarah", 1500, 600))
internacional.agregar_empleados(Vendedor("Pierre", 1500, 550))

nuevos_productos.agregar_empleados(EmpleadoBase("Jaime", 1200))
nuevos_productos.agregar_empleados(Vendedor("Secundino", 1200, 350))


empresa = Empresa("Tienda Roberto")
empresa.agregar_departamento(nacional)
empresa.agregar_departamento(internacional)
empresa.agregar_departamento(nuevos_productos)

print("ANTES DEL TRASLADO")
empresa.imprimir_informacion()

print()
empresa.transferir_empleado(ana, nuevos_productos)

print("\nDESPUÉS DEL TRASLADO")
empresa.imprimir_informacion()
