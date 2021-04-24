from indicadores import Indicadores
class Nomina(Indicadores):
    def __init__(self):
        self.__salarioBasico = 0
        self.__diasLiquidados = 0
        self.__smlv = self.salariominimo()
        self.__auxilioT = 106454 

    def setSalarioBasico(self,salarioBasico):
        if str(type(salarioBasico)) == "<class 'init'>" or str(type(salarioBasico))== "<class 'float'>":
            
            if salarioBasico >= self.salariominimo():
                self.__salarioBasico = salarioBasico
            else :
                print('El salario Basico no puede ser inferior a SMLV')
    
    def getSalarioBasico(self):
        return self.__salarioBasico
    
    #def setSalarioBasico(self,salarioBasico):
     #   self.__salarioBasico = salarioBasico

    def getDiasLiquidados(self):
        return self.__diasLiquidados

    def setDiasLiquidados(self,diasliquidados):
        self.__diasLiquidados= diasliquidados
    
    def salarioDevengado(self):
        try :
             return (self.__salarioBasico / 30) * self.__diasLiquidados
        except Exception as e: 
            print(e)
            print('Error al calcular Salario Devengado')
    
    def auxilioTransporte(self):
        
        if self.__salarioBasico > (self.__smlv *2):
            return 0
        else:
            return self.__auxilioT / 30 * self.__diasLiquidados

    def totalDevengado(self):
        return self.salarioDevengado() + self.auxilioTransporte()

    def __str__(self):
        return str("Salario Basico:{}"
                    "\nDias Liquidados: {} "
                    "\nSalario Devengado: {}"
                    "\nAuxilio de Transporte : {}"
                    "\nTortal Devengado : {}").format(
                        self.__salarioBasico,
                        self.__diasLiquidados,
                        self.salarioDevengado(),
                        self.auxilioTransporte(),
                        self.totalDevengado()
                    )