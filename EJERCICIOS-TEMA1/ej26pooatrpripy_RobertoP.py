class Empleado:
    #__nombre
    #__sueldo_base
    #__comision
    #__bono
    def __init__(self, nombre: str, sueldo_base: float, comision: float, bono: float) -> None:

        if type(nombre) is not str: raise TypeError("Nombre no valido")
        if nombre.strip() == "": raise ValueError("Nombre no puede estar vacío")

        if type(sueldo_base) is not float: raise TypeError("Sueldo no valido")
        if sueldo_base <= 0 or sueldo_base >= 200000: raise ValueError("Sueldo fuera de rango")

        if type(comision) is not float: raise TypeError("Comisión no valido")
        if comision >= sueldo_base * 0.5: raise ValueError("Comisión debe de ser < 50% del sueldo")

        if type(bono) is not float: raise TypeError("Bono no valido")
        if bono >= sueldo_base * 0.5: raise ValueError("Bono debe de ser < 50% del sueldo")

        self.__nombre = nombre
        self.__sueldo_base = sueldo_base
        self.__comision = comision
        self.__bono = bono

    def calcular_sueldo(self) -> float:
        return self.__sueldo_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if type(nuevo_nombre) is not str: raise TypeError("Nombre no valido")
        if nuevo_nombre.strip() == "": raise ValueError("Nombre no valido")
        self.__nombre = nuevo_nombre

    @property
    def sueldo_base(self) -> float:
        return self.__sueldo_base


    @sueldo_base.setter
    def sueldo_base(self, sueldo_base: float) -> None:
        if type(sueldo_base) is not float: raise TypeError("Nuevo sueldo no valido")
        if sueldo_base <= 0 or sueldo_base >= 200000: raise ValueError("Sueldo fuera de rango")
        
        self.__sueldo_base = sueldo_base

    @property
    def comision(self) -> float:
        return self.__comision

    @comision.setter
    def comision(self, comision: float) -> None:
        if type(comision) is not float: raise TypeError("Comisión no valido")
        if comision >= self.sueldo_base * 0.5: raise ValueError("Comisión debe de ser < 50% del sueldo")

        self.__comision = comision

    @property
    def bono(self) -> float:
        return self.__bono

    @bono.setter
    def bono(self, bono: float) -> None:
        if type(bono) is not float: raise TypeError("Bono no valido")
        if bono >= self.sueldo_base * 0.5: raise ValueError("Bono debe de ser < 50% del sueldo")

        self.__bono = bono

empleado = Empleado("Roberto",1200.00, 100.00,30.00)


empleado.comision += 100


try:
    empleado.sueldo_base = -1200
except:
    raise ValueError("No se puede poner el sueldo base en negativo")
