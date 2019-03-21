from tkinter import *
from tkinter import ttk

class Application():
	def __init__(self):
		window=Tk()
		window.geometry('400x400')
		window.configure(wh='white')
		window.title('Retirement Simulator')
		ttk.Button(window,text='Salir',command=window.destroy).pack(side=BOTTOM)
		window.mainloop()

mi_app=Application()

