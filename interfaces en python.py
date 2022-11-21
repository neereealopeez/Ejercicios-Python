from tkinter import *
from tkinter import ttk

def saludar():
    texto= campoTexto.get()
    textoLabel.set(texto)
    print(texto)

#Generar la ventana
ventana = Tk()
ventana.title("·Primer Ejercicio·")
ventana.geometry("300x300")
ventana.resizable(width="False",height="False")
ventana.config(background="light blue")


#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=10).pack()

#Componentes Label y Button
textoLabel=StringVar()
textoLabel.set("Hola Tkinter")                                         
labelTexto=ttk.Label(frm, textvariable=textoLabel)
labelTexto.config(background="light pink", border=8, font=("Times New Roman",12))
labelTexto.pack()

#Componente cuadro de texto
campoTexto= ttk.Entry(frm)
campoTexto.pack()
ttk.Button(frm, text="Saludo", command=saludar).pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()