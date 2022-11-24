from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("·Almacenamiento de datos·")
ventana.geometry("300x300")
ventana.resizable(width="False",height="False")
ventana.config(background="mistyrose")          

label_titulo=ttk.Label(ventana, text="Introduce tus datos")


label_usuario=ttk.Label(ventana, text="Nombre de usuario")

datos_usuario=ttk.Entry(ventana)

label_contraseña1= ttk.Label(ventana, text="Contraseña")


datos_contraseña1=ttk.Entry(ventana)

label_contraseña2=ttk.Label(ventana, text="Contraseña")

datos_contraseña1=ttk.Entry(ventana)
datos_contraseña2=ttk.Entry(ventana)

boton_guardar=ttk.Button(ventana, text="Guadar")
boton_salir= ttk.Button(ventana,text="Salir")

label_titulo.grid(row=0, column=0)
datos_usuario.grid(row=0, column=1)
label_usuario.grid(row=1, column=0)
label_contraseña1.grid(row=2, column=0)
label_contraseña2.grid(row=3, column=0)

ventana.mainloop()
