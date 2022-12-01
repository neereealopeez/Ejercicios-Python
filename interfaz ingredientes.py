from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana=Tk()

ventana.title("Lista de ingredientes")
ventana.geometry("500x500")
ventana.resizable(width="False",height="False")
ventana.config(background="light grey")          

combo_carne = ttk.Combobox(ventana,
    state="readonly",
    values=["Mujer", "Hombre", "Prefiero no decirlo" ]
)
combo_carne.place(x=200, y=230)
combo_carne.set("Selecciona sexo")

ventana.mainloop()