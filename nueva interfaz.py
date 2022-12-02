import flet as ft

def main(page: ft.Page):

    def cambiarColor(e):
        t.color="cyan"
        for i in range (10):
            text=ft.Text(value=f"Número {i}", size="10")
            page.add(text)


    #componente de texto
    t=ft.Text(value="Introducción a Flet", color="pink", size=20, italic=True)
    page.add(t) #Añade y actualiza
    #Componente botón
    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiarColor)
    page.add(bt)
ft.app(target=main)