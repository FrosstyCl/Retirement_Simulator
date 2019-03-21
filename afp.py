from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.geometry('400x400') #ancho x alto
ventana.title('Retirement Simulator')
ttk.Button(ventana,text='Salir',command=quit).pack(side=BOTTOM)




ventana.mainloop()

