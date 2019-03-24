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
		self.Rentabilidad=IntVar()
		self.APV=IntVar()
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
		Radiobutton(self.afp,text="Cuprum",value=1,variable=self.Rentabilidad).grid(row=6,column=1)
		Radiobutton(self.afp,text="Modelo",value=2,variable=self.Rentabilidad).grid(row=6,column=2)
		Radiobutton(self.afp,text="PlanVital",value=3,variable=self.Rentabilidad).grid(row=6,column=3)
		Radiobutton(self.afp,text="Provida",value=4,variable=self.Rentabilidad).grid(row=7,column=1)
		Radiobutton(self.afp,text="Habitat",value=5,variable=self.Rentabilidad).grid(row=7,column=2)
		Radiobutton(self.afp,text="Capital",value=6,variable=self.Rentabilidad).grid(row=7,column=3)

		Button(self.afp,text="Calcular",command=self.Calculo_Esperado).grid(row=8,column=2)
		Button(self.afp,text="volver",command=self.Start).grid(row=8,column=0,columnspan=2,padx=20,pady=20)

	def Deseado(self):
		self.frame.destroy()
		self.afp=Frame(self.window)
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
		Radiobutton(self.afp,text="Cuprum",value=1,variable=self.Rentabilidad).grid(row=6,column=1)
		Radiobutton(self.afp,text="Modelo",value=2,variable=self.Rentabilidad).grid(row=6,column=2)
		Radiobutton(self.afp,text="PlanVital",value=3,variable=self.Rentabilidad).grid(row=6,column=3)
		Radiobutton(self.afp,text="Provida",value=4,variable=self.Rentabilidad).grid(row=7,column=1)
		Radiobutton(self.afp,text="Habitat",value=5,variable=self.Rentabilidad).grid(row=7,column=2)
		Radiobutton(self.afp,text="Capital",value=6,variable=self.Rentabilidad).grid(row=7,column=3)

		Label(self.afp,text="Monto deseado: ").grid(row=8,column=0)
		Entry(self.afp,textvariable=self.APV).grid(row=8,column=1,columnspan=2)

		Button(self.afp,text="Calcular",command=self.Calculo_Deseado).grid(row=9,column=2)
		Button(self.afp,text="volver",command=self.Start).grid(row=9,column=0,columnspan=2,padx=20,pady=20)
		

	def salir(self):
		answer=messagebox.askquestion("Salir","¿Deseas cerrar la aplicacion?")
		if answer=="yes":
			self.window.destroy()
	def Calculo_Esperado(self):
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
		self.Total=self.SaldoInicial.get()*((1+self.Rentabilidad.get())**Tiempo)+(Deposito*((1+self.Rentabilidad.get())**(Tiempo-1))/self.Rentabilidad.get())
		
		Label(self.afp,text="Tu total es: "+ str(self.Total)).grid(row=1,column=0,columnspan=3)
		if self.Sexo==1:#Hombre
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/180))+" mil pesos aprox").grid(row=2,column=0,columnspan=3)
		else:
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/300))+" mil pesos aprox").grid(row=2,column=0,columnspan=3)
				
		#Label(self.afp,text="Total-1: "+str(self.Total-1)).grid(row=3,column=1)
		
	def Calculo_Deseado(self):
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
		self.Total=self.SaldoInicial.get()*((1+self.Rentabilidad.get())**Tiempo)+(Deposito*((1+self.Rentabilidad.get())**(Tiempo-1))/self.Rentabilidad.get())
		
		Label(self.afp,text="Tu total actual es: "+ str(self.Total)).grid(row=1,column=0,columnspan=3)



		
		if self.Sexo==1:#Hombre,180
			faltante=self.APV.get()*180-self.Total

		else:#mujeres,300
			Label(self.afp,text="Tu pension llegaria a : "+str(int(self.Total/300))+" mil pesos aprox").grid(row=2,column=0,columnspan=3)
		






def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()