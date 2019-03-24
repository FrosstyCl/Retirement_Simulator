from tkinter import *
from tkinter import messagebox

class Application:
	def __init__(self):
		self.window=Tk()
		self.window.geometry('500x500')
		#window.resizable(0,0)
		self.window.title('Retirement Simulator')
		self.window.config(bg="white")

		#Variables para los calculos
		self.inicio=False
		self.Sexo=IntVar()
		self.Total=0
		self.Sueldo=IntVar()
		self.SaldoInicial=IntVar()
		self.Edad=IntVar()
		self.Start()

	def Start(self):
		if self.inicio:
			self.afp.destroy()
			self.frame.destroy()

		self.frame=Frame(self.window,bg="beige")
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
		self.afp=Frame(self.window)
		self.afp.pack()
		self.inicio=True
		Label(self.afp,text="Selecciona la AFP donde cotices.").grid(row=0,column=0,rowspan=2,columnspan=3)
		Button(self.afp,text="Cuprum",font=("Arial",12),command=self.cuprum).grid(row=2,column=0,padx=20,pady=20)
		Button(self.afp,text="Modelo",font=("Arial",12),command=self.modelo).grid(row=2,column=1,padx=20,pady=20)
		Button(self.afp,text="Habitat",font=("Arial",12),command=self.habitat).grid(row=2,column=2,padx=20,pady=20)
		Button(self.afp,text="PlanVital",font=("Arial",12),command=self.plan).grid(row=3,column=0,padx=20,pady=20)
		Button(self.afp,text="Capital",font=("Arial",12),command=self.capital).grid(row=3,column=1,padx=20,pady=20)
		Button(self.afp,text="Provida",font=("Arial",12),command=self.provida).grid(row=3,column=2,padx=20,pady=20)
		Button(self.afp,text="volver",command=self.Start).grid(row=5,column=0,padx=20,pady=20)
		Button(self.afp,text="Salir",font=("Arial",12),command=self.salir).grid(row=5,column=2)

	def Deseado(self):
		self.frame.destroy()
		self.afp=Frame(self.window)
		self.afp.pack()
		self.inicio=True
		Label(self.afp,text="Selecciona la AFP donde cotices.").grid(row=0,column=0,rowspan=2,columnspan=3)
		Button(self.afp,text="Cuprum",font=("Arial",12),command=self.cuprum).grid(row=2,column=0,padx=20,pady=20)
		Button(self.afp,text="Modelo",font=("Arial",12),command=self.modelo).grid(row=2,column=1,padx=20,pady=20)
		Button(self.afp,text="Habitat",font=("Arial",12),command=self.habitat).grid(row=2,column=2,padx=20,pady=20)
		Button(self.afp,text="PlanVital",font=("Arial",12),command=self.plan).grid(row=3,column=0,padx=20,pady=20)
		Button(self.afp,text="Capital",font=("Arial",12),command=self.capital).grid(row=3,column=1,padx=20,pady=20)
		Button(self.afp,text="Provida",font=("Arial",12),command=self.provida).grid(row=3,column=2,padx=20,pady=20)
		Button(self.afp,text="volver",command=self.Start).grid(row=5,column=0,padx=20,pady=20)
		Button(self.afp,text="Salir",font=("Arial",12),command=self.salir).grid(row=5,column=2)

	def cuprum(self):
		self.frame.destroy()
		self.afp.destroy()
		self.inicio=True
		self.afp=Frame(self.window,bg="beige")
		self.afp.pack()
		
		#imagen_cuprum=PhotoImage(file="AFP.png")
		Label(self.afp,text="Cotizando en Cuprum",font=("Arial",16)).grid(row=0,column=0,columnspan=3)
		Label(self.afp,text="Edad :").grid(row=2,column=0)
		Entry(self.afp,textvariable=self.Edad).grid(row=2,column=1,columnspan=2)

		Label(self.afp,text="Sueldo :").grid(row=3,column=0)
		Entry(self.afp,textvariable=self.Sueldo).grid(row=3,column=1,columnspan=2)		
		
		Label(self.afp,text="Sexo: ").grid(row=4,column=0)
		Radiobutton(self.afp,text="Hombre",value=1,variable=self.Sexo).grid(row=4,column=1)
		Radiobutton(self.afp,text="Mujer",value=2,variable=self.Sexo).grid(row=4,column=2)
		
		Label(self.afp,text="Saldo Inicial: ").grid(row=5,column=0)
		Entry(self.afp,textvariable=self.SaldoInicial).grid(row=5,column=1,columnspan=2)

		Button(self.afp,text="Calcular",command=self.Calculo).grid(row=8,column=2)
		Button(self.afp,text="volver",command=self.Start).grid(row=8,column=0,columnspan=2,padx=20,pady=20)
		
	def modelo(self):
		self.afp.destroy()
		self.frame.destroy()
		self.inicio=True
		self.afp=Frame(self.window,bg="beige")
		self.afp.pack()
		Label(self.afp,text="Cotizando en",font=("Arial",16)).grid(row=0,column=0,columnspan=3)
		Button(self.afp,text="volver",command=self.Start).grid(row=5,column=1,columnspan=3,padx=20,pady=20)
		Entry(self.afp,textvariable=self.Edad).grid(row=2,column=2)
		Label(self.afp,text="Edad :").grid(row=2,column=1)
		Entry(self.afp,textvariable=self.Sueldo).grid(row=3,column=2)
		Label(self.afp,text="Sueldo :").grid(row=3,column=1)


	def habitat(self):
		pass
	def plan(self):
		pass
	def capital(self):
		pass
	def provida(self):
		pass
	def salir(self):
		answer=messagebox.askquestion("Salir","¿Deseas cerrar la aplicacion?")
		if answer=="yes":
			self.window.destroy()
	def Calculo(self,rentabilidad=0.07):
		self.frame.destroy()
		self.afp.destroy()
		self.inicio=True
		self.afp=Frame(self.window,bg="beige")
		self.afp.pack()

		Label(self.afp,text="Resultados").grid(row=0,column=0,columnspan=2)
		
		if self.Sexo==1:#Hombre
			Tiempo=65-self.Edad.get()
		else:#Mujer
			Tiempo=60-self.Edad.get()
		Deposito=self.Sueldo.get()*1200
		print(Tiempo,Deposito)
		self.Total=self.SaldoInicial.get()*((1+rentabilidad)**Tiempo)+(Deposito*((1+rentabilidad)**(Tiempo-1))/rentabilidad)
		
		Label(self.afp,text="Tu total es: "+ str(self.Total)).grid(row=1,column=0,columnspan=3)
		if self.Sexo==1:#Hombre
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/180))+" mil pesos aprox").grid(row=2,column=0,columnspan=3)
		else:
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/300))+" mil pesos aprox").grid(row=2,column=0,columnspan=3)
				
		Label(self.afp,text="Total-1: "+str(self.Total-1)).grid(row=3,column=1)
		


		






def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()