from tkinter import *
from tkinter import messagebox

class Application:
	def __init__(self):
		self.window=Tk()
		self.window.geometry('600x450')
		#self.window.resizable(0,0)
		self.window.title('Retirement Simulator')
		self.window.config(bg="#617EDE")

		#Variables para los calculos
		self.inicio=False
		self.Sexo=IntVar()
		self.Total=0
		self.Sueldo=IntVar()
		self.SaldoInicial=IntVar()
		self.Edad=IntVar()
		self.AFP=IntVar()
		self.APV=IntVar()
		self.Fondo=IntVar()
		self.Rentas={ 0:[0.01,0.01,0.01,0.01,0.01] ,1:[0.054,0.048,0.048,0.042,0.042], 2:[0.026,0.027,0.031,0.034,0.034], 3:[0.053,0.046,0.046,0.038,0.036], 4:[0.053,0.044,0.044,0.038,0.038], 5:[0.055,0.049,0.051,0.044,0.044], 6:[0.052,0.046,0.045,0.039,0.041]}
		self.Start()
		
		#1 Cuprum
		#2 Modelo
		#3 Plan
		#4 Provida
		#5 Habitat
		#6 Capital

	def Start(self):
		if self.inicio:
			self.afp.destroy()
			self.frame.destroy()

		self.frame=Frame(self.window,bg="#617EDE",width=500,height=400)
		self.frame.pack()
		
		#Cargar Logo AFP
		imagen=PhotoImage(file="AFP.png")
		Logo=Label(self.frame,image=imagen).grid(row=5,columnspan=3)

		#Texto de Bienvenida y primeras instrucciones.
		Label(self.frame,text="Bienvenido al simulador\n Selecciona que valor deseas calcular.",font=("Arial",18)).grid(row=0,column=0,sticky="n",rowspan=2,columnspan=3)
		Button(self.frame,text="Calcular esperado",command=self.Esperado).grid(row=2,column=0)
		Button(self.frame,text="Calcular deseado",command=self.Deseado).grid(row=2,column=2)
		Button(self.frame,text="Salir",font=("Arial",12),command=self.salir).grid(row=3,column=1)
		
		#Mantener la ventana principal abierta hasta el fin del ciclo.
		self.window.mainloop()


	def Esperado(self):
		self.frame.destroy()
		self.afp=Frame(self.window,bg="#617EDE")
		self.afp.pack()
		self.inicio=True
		Label(self.afp,text="A continuacion ingresa tus datos",font=("Arial",16)).grid(row=0,column=0,columnspan=3)
		Label(self.afp,text="Edad :").grid(row=2,column=0)
		Entry(self.afp,textvariable=self.Edad).grid(row=2,column=1,columnspan=2)

		Label(self.afp,text="Sueldo :").grid(row=3,column=0)
		Entry(self.afp,textvariable=self.Sueldo).grid(row=3,column=1,columnspan=2)		
		
		Label(self.afp,text="Sexo: ").grid(row=4,column=0)
		Radiobutton(self.afp,text="Hombre",value=1,variable=self.Sexo).grid(row=4,column=1)
		Radiobutton(self.afp,text="Mujer",value=2,variable=self.Sexo).grid(row=4,column=2)
		
		Label(self.afp,text="Saldo Inicial: ").grid(row=5,column=0)
		Entry(self.afp,textvariable=self.SaldoInicial).grid(row=5,column=1,columnspan=2)

		Label(self.afp,text="AFP: ").grid(row=6,column=0,rowspan=2)
		#RECORDATORIO CAMBIAR LAS RENTABILIDADES
		Radiobutton(self.afp,text="Cuprum",value=1,variable=self.AFP).grid(row=6,column=1)
		Radiobutton(self.afp,text="Modelo",value=2,variable=self.AFP).grid(row=6,column=2)
		Radiobutton(self.afp,text="PlanVital",value=3,variable=self.AFP).grid(row=6,column=3)
		Radiobutton(self.afp,text="Provida",value=4,variable=self.AFP).grid(row=7,column=1)
		Radiobutton(self.afp,text="Habitat",value=5,variable=self.AFP).grid(row=7,column=2)
		Radiobutton(self.afp,text="Capital",value=6,variable=self.AFP).grid(row=7,column=3)

		Label(self.afp,text="Fondo: ").grid(row=8,column=0,rowspan=2)
		Radiobutton(self.afp,text="A",value=1,variable=self.Fondo).grid(row=8,column=1)
		Radiobutton(self.afp,text="B",value=2,variable=self.Fondo).grid(row=8,column=2)
		Radiobutton(self.afp,text="C",value=3,variable=self.Fondo).grid(row=8,column=3)
		Radiobutton(self.afp,text="D",value=4,variable=self.Fondo).grid(row=9,column=1)
		Radiobutton(self.afp,text="E",value=5,variable=self.Fondo).grid(row=9,column=2)		

		Button(self.afp,text="Calcular",command=self.Calculo_Esperado).grid(row=10,column=2)
		Button(self.afp,text="Volver",command=self.Start).grid(row=10,column=0,columnspan=2,padx=20,pady=20)

	def Deseado(self):
		self.frame.destroy()
		self.afp=Frame(self.window,bg="#617EDE")
		self.afp.pack()
		self.inicio=True

		Label(self.afp,text="A continuacion ingresa tus datos",font=("Arial",16)).grid(row=0,column=0,columnspan=3)
		Label(self.afp,text="Edad :").grid(row=2,column=0)
		Entry(self.afp,textvariable=self.Edad).grid(row=2,column=1,columnspan=2)

		Label(self.afp,text="Sueldo :").grid(row=3,column=0)
		Entry(self.afp,textvariable=self.Sueldo).grid(row=3,column=1,columnspan=2)		
		
		Label(self.afp,text="Sexo: ").grid(row=4,column=0)
		Radiobutton(self.afp,text="Hombre",value=1,variable=self.Sexo).grid(row=4,column=1)
		Radiobutton(self.afp,text="Mujer",value=2,variable=self.Sexo).grid(row=4,column=2)
		
		Label(self.afp,text="Saldo Inicial: ").grid(row=5,column=0)
		Entry(self.afp,textvariable=self.SaldoInicial).grid(row=5,column=1,columnspan=2)

		Label(self.afp,text="AFP: ").grid(row=6,column=0,rowspan=2)
		#RECORDATORIO CAMBIAR LAS RENTABILIDADES
		Radiobutton(self.afp,text="Cuprum",value=1,variable=self.AFP).grid(row=6,column=1)
		Radiobutton(self.afp,text="Modelo",value=2,variable=self.AFP).grid(row=6,column=2)
		Radiobutton(self.afp,text="PlanVital",value=3,variable=self.AFP).grid(row=6,column=3)
		Radiobutton(self.afp,text="Provida",value=4,variable=self.AFP).grid(row=7,column=1)
		Radiobutton(self.afp,text="Habitat",value=5,variable=self.AFP).grid(row=7,column=2)
		Radiobutton(self.afp,text="Capital",value=6,variable=self.AFP).grid(row=7,column=3)

		Label(self.afp,text="Fondo: ").grid(row=8,column=0,rowspan=2)
		Radiobutton(self.afp,text="A",value=1,variable=self.Fondo).grid(row=8,column=1)
		Radiobutton(self.afp,text="B",value=2,variable=self.Fondo).grid(row=8,column=2)
		Radiobutton(self.afp,text="C",value=3,variable=self.Fondo).grid(row=8,column=3)
		Radiobutton(self.afp,text="D",value=4,variable=self.Fondo).grid(row=9,column=1)
		Radiobutton(self.afp,text="E",value=5,variable=self.Fondo).grid(row=9,column=2)

		Label(self.afp,text="Monto deseado: ").grid(row=10,column=0)
		Entry(self.afp,textvariable=self.APV).grid(row=10,column=1,columnspan=2)

		Button(self.afp,text="Calcular",command=self.Calculo_Esperado).grid(row=11,column=2)
		Button(self.afp,text="Volver",command=self.Start).grid(row=11,column=0,columnspan=2,padx=20,pady=20)

	def salir(self):
		answer=messagebox.askquestion("Salir","¿Deseas cerrar la aplicacion?")
		if answer=="yes":
			self.window.destroy()
	def Calculo_Esperado(self):
		self.frame.destroy()
		self.afp.destroy()
		self.inicio=True
		self.afp=Frame(self.window,bg="#617EDE")
		self.afp.pack()

		Label(self.afp,text="Resultados").grid(row=0,column=0,columnspan=2)
		
		if self.Sexo==1:#Hombre
			Tiempo=65-self.Edad.get()
		else:#Mujer
			Tiempo=60-self.Edad.get()
		Deposito=(self.Sueldo.get()*0.1)*12
		#print(self.Rentas[self.AFP.get()][self.Fondo.get()-1])
		if (self.AFP.get() is 1 or 2 or 3 or 4 or 5) and (self.Fondo.get() is 1 or 2 or 3 or 4 or 5): 
			self.Total=(self.SaldoInicial.get()*((1+self.Rentas[self.AFP.get()][self.Fondo.get()-1])**Tiempo)+Deposito*((((self.Rentas[self.AFP.get()][self.Fondo.get()-1]+1)**Tiempo)-1)/self.Rentas[self.AFP.get()][self.Fondo.get()-1]))
		else:
			self.Total=0

		Label(self.afp,text="Tu total es: "+ str(self.Total)).grid(row=1,column=0,columnspan=3)
		if self.Sexo==1:#Hombre
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/180))+" pesos aprox").grid(row=2,column=0,columnspan=3)
		else:
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/300))+" pesos aprox").grid(row=2,column=0,columnspan=3)
				
		Button(self.afp,text="Volver",command=self.Start).grid(row=3,column=1)
		Button(self.afp,text="Salir",command=self.salir).grid(row=3,column=2)
		
	def Calculo_Deseado(self):
		self.frame.destroy()
		self.afp.destroy()
		self.inicio=True
		self.afp=Frame(self.window,bg='blue',fill="both")
		self.afp.pack()

		Label(self.afp,text="Resultados").grid(row=0,column=0,columnspan=2)
		
		if self.Sexo==1:#Hombre
			Tiempo=65-self.Edad.get()
		else:#Mujer
			Tiempo=60-self.Edad.get()
		Deposito=self.Sueldo.get()*12
		self.Total=self.SaldoInicial.get()*((1+self.Rentas[self.AFP.get()][self.Fondo.get()-1])**Tiempo)+(Deposito*((1+self.Rentas[self.AFP.get()][self.Fondo.get()-1])**(Tiempo-1))/self.Rentas[self.AFP.get()][self.Fondo.get()-1])
		
		self.Total_Deseado=self.APV.get()*12

		Deposito=(self.Rentas[self.AFP.get()][self.Fondo.get()-1]*(self.Total_Deseado-self.self.Total*((1+self.Rentas[self.AFP.get()][self.Fondo.get()-1])**Tiempo)))/(((1+self.Rentas[self.AFP.get()][self.Fondo.get()-1])**Tiempo)-1)
       	

		Label(self.afp,text="Tu total actual es: "+ str(self.Total)).grid(row=1,column=0,columnspan=3)
		Label(self.afp,text="Para tener tu jubilacion esperada, debes aportar: " + str(int(Deposito/12) + " entre lo obligarorio y tu ahorro.\n Por esto tu deposito de APV debe ser: "+ str(self.Sueldo-int(Deposito/12))+" mensualmente").grid(row=2,rowspan=3,column=0,columnspan=3))





def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()