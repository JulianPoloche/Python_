
class Empleado:
 ##construuctor
    def __init__(self):
        self.__nombre = None
        self.apellido = None
        self.cargo = None
        self.sueldo = None

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre = nombre


        
    def __str__(self):
        return str(
            "nombre : {} \n "
            "Apellido : {} \n "
            "cargo : {} \n "
            "Sueldo : {} \n "
        ).format(
            self.__nombre,
            self.apellido,
            self.cargo,
            self.sueldo
        )


