import flet as ft

# Utilizar flet como ft

def main(page: ft.Page):
    page.title= "· COMESTIBLES ·"
    tnombre = ft.Text(value="Tienda López ", color= "green", size=30)
    tbienvenida=ft.Text(value="Bienvenido a nuestra tienda. Por favor, dinos tu nombre:", color= "black", size=20, italic=True)
    page.add(tnombre)
    page.add(tbienvenida)

    textField_Nombre= ft.TextField(label="Nombre", hint_text="¿Cuál es tu nombre?", width=400)
    page.add(textField_Nombre)

    def click_boton(e):
        usuario= ft.Text(value= "Por favor, seleccione una opción")
        page.add(usuario)
        dropdown_carne = ft.Dropdown(width=200, options=[ft.dropdown.Option("Pechuga"),ft.dropdown.Option("Solomillo"),ft.dropdown.Option("Cordero")])
        dropdown_hortalizas= ft.Dropdown(width=200, options= [ft.dropdown.Option("Cebolla"),ft.dropdown.Option ("Ajo"), ft.dropdown.Option("Espinaca"),ft.dropdown.Option ("Alcachofa"),ft.dropdown.Option("Zanahoria")])
        row = ft.Row(spacing=50, controls=[dropdown_carne,dropdown_hortalizas])
        page.add(row)
        boton_correcto.disabled 

    boton_correcto= ft.ElevatedButton(text="Es mi nombre", on_click= click_boton)
    page.add(boton_correcto)

    

ft.app(target=main)