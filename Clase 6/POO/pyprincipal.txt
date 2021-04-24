
from nomina import Nomina

nominas = []

while True:
    print("1. Ingresar Nomina")
    print("2. Salir")

    opcion = input('Ingrese la Opción : ')

    if opcion == '1':
        renglon = []
        n = Nomina()
        salario = float(input("Ingrese el sueldo Basicó : "))
        diasL = float(input("Ingrese los dias Liquidados : "))
        n.setSalarioBasico(salario)
        n.setDiasLiquidados(diasL)
       
        renglon.append({'variable': 'Salario Basico', 'Resultado': n.getSalarioBasico()})
        renglon.append({'variable': 'Dias Liquidados', 'Resultado': n.getDiasLiquidados()})
        renglon.append({'variable': 'Salario Devengado', 'Resultado': n.salarioDevengado()})
        renglon.append({'variable': 'Auxilio Transporte', 'Resultado': n.auxilioTransporte()})
        renglon.append({'variable': 'Total Devengado', 'Resultado': n.totalDevengado()})
        print(n)
        nominas.append(renglon)

    elif opcion == '2':
        print("Saliendo")
        break
f = open('nomina.txt','w')

for i in nominas:
    f.write('**********')
    for j in i :
        f.write(str(j) + "\n")
f.close()    
