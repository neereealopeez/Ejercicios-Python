from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usuario=""
contraseña=""
vUsuarios=[]
contraseña_repetida=""

def guardarDatos():
    usuario= datos_usuario.get()
    contraseña= datos_contraseña1.get()
    contraseña_repetida= datos_contraseña2
    print(usuario + " - " + contraseña)
    if datos_contraseña1==datos_contraseña2:
        vUsuarios.append(usuario)
        vUsuarios.append(contraseña)
        vUsuarios.append(contraseña_repetida)
        datos_usuario.delete(0, (usuario))
        datos_contraseña1.delete(0,(contraseña))
        datos_contraseña2.delete(0, (contraseña_repetida))
        messagebox.showinfo("Usuario guardado", f"Usuario {usuario} guardado correctamente")

ventana = Tk()
ventana.title("·Almacenamiento de datos·")
ventana.geometry("550x300")
ventana.resizable(width="False",height="False")
ventana.config(background="light grey")          

label_titulo=ttk.Label(ventana, text="Introduce tus datos")


label_usuario=ttk.Label(ventana, text="Nombre de usuario")

datos_usuario=ttk.Entry(ventana)

label_contraseña1= ttk.Label(ventana, text="Contraseña")


datos_contraseña1=ttk.Entry(ventana)

label_contraseña2=ttk.Label(ventana, text="Repite contraseña")

datos_contraseña1=ttk.Entry(ventana)
datos_contraseña1= ttk.Entry(ventana, show="*")
datos_contraseña2=ttk.Entry(ventana)
datos_contraseña2= ttk.Entry(ventana, show="*")

boton_guardar=ttk.Button(ventana, text="Guadar", command=guardarDatos)
boton_salir= ttk.Button(ventana,text="Salir")

label_titulo.grid(row=0, column=0, pady=10, padx=10)
datos_usuario.grid(row=1, column=2, pady=12)
label_usuario.grid(row=1, column=1, pady=12)
datos_contraseña1.grid(row=2, column=2, pady=12)
label_contraseña1.grid(row=2, column=1, pady=12)
datos_contraseña2.grid(row=3, column=2, pady=12,)
label_contraseña2.grid(row=3, column=1, pady=12)
boton_guardar.grid(row=4, column=1, pady=12)
boton_salir.grid(row=4, column=2, pady=12)

combo_sexo = ttk.Combobox(ventana,
    state="readonly",
    values=["Mujer", "Hombre", "Prefiero no decirlo" ]
)
combo_sexo.place(x=200, y=230)
combo_sexo.set("Selecciona sexo")
ventana.mainloop()
