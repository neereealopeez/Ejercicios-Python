from tkinter import *
from tkinter import ttk

#Generar la ventana
ventana = Tk()
ventana.title("·Primer Ejercicio·")
ventana.geometry("250x300")
ventana.resizable(width="False",height="False")
ventana.config(background="light blue")


#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=10).pack()

#Componentes Label y Button
labelTexto=ttk.Label(frm, text="¡Hola Tkinter!")
labelTexto.config(background="light pink", border=8, font=("Times New Roman",12))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()