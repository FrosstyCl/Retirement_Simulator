from tkinter import *
from tkinter import messagebox

class Application():
	def __init__(self):
		self.window=Tk()
		self.window.geometry('500x500')
		#window.resizable(0,0)
		self.window.title('Retirement Simulator')
		self.window.config(bg="white")
		self.inicio=False
		self.Start()

	def Start(self):
		if self.inicio:
			self.afp.destroy()

		self.frame=Frame(self.window,bg="beige")
		self.frame.pack()
		
		#Cargar Logo AFP
		imagen=PhotoImage(file="AFP.png")
		Logo=Label(self.frame,image=imagen).grid(row=5,columnspan=3)

		#Texto de Bienvenida y primeras instrucciones.
		Label(self.frame,text="Bienvenido al simulador\n Por favor selecciona la AFP en la cual cotizas.",font=("Arial",18)).grid(row=0,column=0,sticky="n",rowspan=2,columnspan=3)
		

		#Botones para elegir AFP.
		afp_cuprum=Button(self.frame,text="Cuprum",font=("Arial",12),command=self.cuprum).grid(row=2,column=0,padx=20,pady=20)
		afp_modelo=Button(self.frame,text="Modelo",font=("Arial",12),command=self.modelo()).grid(row=2,column=1,padx=20,pady=20)
		afp_habitat=Button(self.frame,text="Habitat",font=("Arial",12),command=self.habitat()).grid(row=2,column=2,padx=20,pady=20)
		afp_plan=Button(self.frame,text="PlanVital",font=("Arial",12),command=self.plan()).grid(row=3,column=0,padx=20,pady=20)
		afp_capital=Button(self.frame,text="Capital",font=("Arial",12),command=self.capital()).grid(row=3,column=1,padx=20,pady=20)
		afp_provida=Button(self.frame,text="Provida",font=("Arial",12),command=self.provida()).grid(row=3,column=2,padx=20,pady=20)
		salir=Button(self.frame,text="Salir",font=("Arial",12),command=self.salir).grid(row=4,column=1,padx=20,pady=20)
		#Mantener la ventana principal abierta hasta el fin del ciclo.
		self.window,mainloop()

	def cuprum(self):
		self.frame.destroy()
		self.inicio=True
		self.afp=Frame(self.window,bg="beige")
		self.afp.pack()
		self.Sueldo=IntVar()
		self.Edad=IntVar()
		#imagen_cuprum=PhotoImage(file="AFP.png")
		Label(self.afp,text="Cotizando en Cuprum",font=("Arial",16)).grid(row=0,column=0,columnspan=3)
		Button(self.afp,text="volver",command=self.Start).grid(row=5,column=1,columnspan=3,padx=20,pady=20)
		Entry(self.afp,textvariable=self.Edad).grid(row=2,column=2)
		Label(self.afp,text="Edad :").grid(row=2,column=1)
		Entry(self.afp,textvariable=self.Sueldo).grid(row=3,column=2)
		Label(self.afp,text="Sueldo :").grid(row=3,column=1)

		
	def modelo(self):
		pass
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

	
def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()