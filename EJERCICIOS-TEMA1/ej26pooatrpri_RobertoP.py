class Empleado:
    def __init__(self, __nombre, __sueldo_base, __comision, __bono):

        if type(__nombre) is not str: raise TypeError("Nombre no valido")
        if __nombre.strip() == "": raise ValueError("Nombre no puede estar vacío")

        if type(__sueldo_base) is not float: raise TypeError("Sueldo no valido")
        if __sueldo_base <= 0 and __sueldo_base < 200.000: raise ValueError("Sueldo no puede ser <= 0")

        if type(__comision) is not float: raise TypeError("Comisión no valido")
        if __comision < (__sueldo_base // 2): raise ValueError("Comisión debe de ser < 50% del sueldo")

        if type(__bono) is not float: raise TypeError("Bono no valido")
        if __bono < (__sueldo_base // 2): raise ValueError("Bono debe de ser < 50% del sueldo")

        self.__nombre = __nombre
        self.__sueldo_base = __sueldo_base
        self.__comision = __comision
        self.__bono = __bono

    def calcular_sueldo(self):
        return self.sueldo_base