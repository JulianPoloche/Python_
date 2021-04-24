from tkinter import *
from empleado import Empleado
from nomina import Nomina 

class Ejercicio1:
        def frame(self):
            root = Tk()
            frame  =Frame(root)
            frame.pack()
            frame.config(bg="blue")
            frame.config(width =480,height=400)
            root.mainloop()


class Ejercicio2 : 
#
        def label1(self):
             root = Tk()
             Label(root, text = "Hola Mundo").pack()
             Label(root, text = "Hola Mundo 2").pack()
             Label(root, text = "Hola Mundo ultimo").pack()
             
             labelDiferente = Label(root, text = "Label Diferente")
             labelDiferente.pack (anchor = CENTER)
             labelDiferente.config(
                            fg = "blue",
                                bg="red",
                                font=("Verdana",24)
             )
             root.mainloop()

class Ejercicio3:
        def inputText(self):
            root = Tk()

            #Nombre
            frame = Frame(root)
            frame.pack()

            entry = Entry(frame)
            entry.pack(side= RIGHT)
            label = Label(frame , text = "Nombre Empleado")
            label.pack(side = LEFT)

            #Apellido
            frame1 = Frame(root)
            frame1.pack()
            entry1 = Entry(frame1)
            entry1.pack(side= RIGHT)
            label1 = Label(frame1 , text = "Apellido Empleado")
            label1.pack(side = LEFT)

            #CARGO
            frame3 = Frame(root)
            frame3.pack()
            entry2= Entry(frame3)
            entry2.pack(side= RIGHT)
            label2 = Label(frame3 , text = "Nombre Empleado")
            label2.pack(side = LEFT)


            root.mainloop()

        def inputText2(self):
            root = Tk()
            label = Label(root, text ="Nombre")
            label.grid(row=0,column=0)

            entry= Entry(root)
            entry.grid(row=0,column =1)

            label2 = Label(root, text ="Apellido")
            label2.grid(row=0,column=1)

            entry2= Entry(root)
            entry2.grid(row=0,column =2)

            label3 = Label(root, text ="Cargo")
            label3.grid(row=0,column=2)

            entry3= Entry(root)
            entry3.grid(row=0,column =3)

            root.mainloop()

        def textArea(self):
            root = Tk()
            texto = Text(root)
            texto.pack()
            texto.mainloop()

class calculadora:
        
    r = None
    n1 = None
    n2 = None 

    def sumar(self):
        resulatado = float(self.n1.get())+float(self.n2.get())
        self.r.set(resulatado)
        self.limpiar()

    def limpiar(self):
        self.n1.set("")
        self.n2.set("")

    def inicio(self):
        root =Tk()
        self.r = StringVar()
        self.n1 = StringVar()
        self.n2 = StringVar()
        root.config(bd=15)

        Label(root,text='Numero 1').pack()
        Entry(root,justify=CENTER,textvariable=self.n1).pack()

            
        Label(root,text='\nNumero 2').pack()
        Entry(root,justify=CENTER,textvariable=self.n2).pack()

            
        Label(root,text='\nResultado').pack()
        Entry(root,justify=CENTER,state =DISABLED,textvariable=self.r).pack()

        Label(root).pack() # separador
        Button(root, text="SUMAR",command=self.sumar).pack()

        root.mainloop()

class InterfazNomina:
    
    
    def __init__(self):
        self.root = Tk()
        self.root.config(bd =15)
        self.nombres = StringVar()
        self.apellido = StringVar()
        self.cargo = StringVar()
        self.salario = StringVar()
        self.diasLiquidados = StringVar()
        self.nomina =Nomina()
        self.texto = Text(self.root)

        

    def agregarEmpleado(self):
        empleado = Empleado()
        empleado.setNombre(self.nombres.get())
        empleado.setApellido(self.apellido.get())
        empleado.setCargo(self.cargo.get())
        empleado.setSueldo(self.salario.get())
        
        self.nomina.setSalarioBasico(float(self.salario.get()))
        self.nomina.setDiasLiquidados(30)
        self.limpiar()
        self.texto.insert('insert',empleado)
        self.texto.insert('insert','\n********\n')
        self.texto.insert('insert',self.nomina)
        self.texto.insert('insert','\n********\n')

       # print("\n++++++++++++++++++++")
        #print(empleado)
       # print("++++++++++++++++++++")
       # print("\n+++++++ DATOS EMPLEADO+++++++++++++")
       # print(self.nomina)
       # print("\n")

    def limpiar(self):
        self.nombres.set("")
        self.apellido.set("")
        self.apellido.set("")
        self.cargo.set("")
        self.salario.set("")


    def interfaz(self):
        pass
    def interfaz(self):
        frame = Frame(self.root,width=480, height=320)

        #Nombre
        labelEmpleado = Label(frame,text ="nombre del empleado")
        labelEmpleado.grid(row=0,column =0)
        inputEmpleado= Entry(frame,textvariable = self.nombres)
        inputEmpleado.grid(row=0 ,column=1)
         #Apellidos
        labelApellidos = Label(frame,text ="Apellido del empleado")
        labelApellidos.grid(row=1,column =0)
        inputApellidos= Entry(frame,textvariable = self.apellido)
        inputApellidos.grid(row=1,column=1)
         #Cargo
        labelCargo = Label(frame,text ="Cargo del empleado")
        labelCargo.grid(row=2,column =0)
        inputCargo= Entry(frame,textvariable = self.cargo)
        inputCargo.grid(row=2 ,column=1)
         #Salario
        labelSueldo = Label(frame,text ="Salario del empleado")
        labelSueldo.grid(row=3,column =0)
        inputSueldo= Entry(frame,textvariable = self.salario)
        inputSueldo.grid(row=3 ,column=1)

        agregar = Button(frame,text ="Agregar",command=self.agregarEmpleado)
        agregar.grid(row=4,column=1)

        frame.pack(fill = 'both',expand=1)
        self.texto.pack(fill ='both',expand=1)

       
        self.root,mainloop()