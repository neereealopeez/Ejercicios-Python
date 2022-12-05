import flet as ft

def main(page: ft.Page):
    page.title="ola"

    def mostrarNombre(e):
        t.value=textField_Nombre.value
        page.update()

    #componente de texto
    t=ft.Text(value="Introducción a Flet", color="pink", size=20, italic=True)
    page.add(t) #Añade y actualiza

    #Componente botón
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=mostrarNombre)
    page.add(bt)

    textField_Nombre= ft.TextField(label="Nombre", hint_text="¿Cuál es tu nombre?")
    textField_Nombre.focus()
    page.add(textField_Nombre)

ft.app(target=main)