class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

    # __str__ indica qué texto se muestra al hacer print del objeto
    def __str__(self):
        return f"Empleado: {self.nombre} - Sueldo: {self.calcular_sueldo()} €"


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
        # Sumamos el sueldo del gerente y el de los demás empleados para sacaar la nómina total
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


# Creamos los empleados y los departamentos.
ana = Empleado("Ana", 1200)
carlos = Vendedor("Carlos", 1200, 350)
marta = Gerente("Marta", 2000, 500)

nacional = Departamento("Nacional", marta)
internacional = Departamento("Internacional", Gerente("John", 2500, 850))
# En este apartado el enunciado repite "Nacional", pero es Nuevos Productos
nuevos_productos = Departamento("Nuevos Productos", Gerente("Marta", 2000, 450))

nacional.agregar_empleados(ana)
nacional.agregar_empleados(carlos)

internacional.agregar_empleados(Vendedor("Sarah", 1500, 600))
internacional.agregar_empleados(Vendedor("Pierre", 1500, 550))

nuevos_productos.agregar_empleados(Empleado("Jaime", 1200))
nuevos_productos.agregar_empleados(Vendedor("Secundino", 1200, 350))

print(nacional)
print()
print(internacional)
print()
print(nuevos_productos)
