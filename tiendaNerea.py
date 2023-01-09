import flet as ft


def main(page: ft.Page):
    page.title= "· COMESTIBLES ·"
    tnombre = ft.Text(value="Tienda López ", color= "green", size=30)
    tbienvenida=ft.Text(value="Bienvenido a nuestra tienda. Por favor, dinos tu nombre:", color= "black", size=20, italic=True)
    page.add(tnombre)
    page.add(tbienvenida)

    textField_Nombre= ft.TextField(label="Nombre", hint_text="¿Cuál es tu nombre?", width=400)
    page.add(textField_Nombre)

    def click_boton_hortalizas(e):
        dropdown_hortalizas= ft.Dropdown(width=200, options= [ft.dropdown.Option("Cebolla"),ft.dropdown.Option ("Ajo"), ft.dropdown.Option("Espinaca"),ft.dropdown.Option ("Alcachofa"),ft.dropdown.Option("Zanahoria")])
        page.add(dropdown_hortalizas)
        tcebolla=ft.Text(value="Cebolla - 1,50 €/kg", color= "black", size=15, italic=True)
        tajo=ft.Text(value="Ajo - 8,45 €/kg", color= "black", size=15, italic=True)
        tespinacas=ft.Text(value="Espinaca - 1 €/bolsa", color= "black", size=15, italic=True)
        talcachofa=ft.Text(value="Alcachofa - 2,50 €/kg", color= "black", size=15, italic=True)
        tzanahoria=ft.Text(value="Zanahoria - 1 €/bolsa", color= "black", size=15, italic=True)
        page.add(tcebolla, tajo, tespinacas, talcachofa, tzanahoria)

    def click_boton_carnes(e):
        dropdown_carne = ft.Dropdown(width=200, options=[ft.dropdown.Option("Carne de ave"),ft.dropdown.Option("Carne de vacuno"),ft.dropdown.Option("Carne de cerdo"),ft.dropdown.Option("Carne roja")])
        page.add(dropdown_carne)
        tcarnedeave=ft.Text(value="Carne de ave - 1,50 €/kg", color= "black", size=15, italic=True)
        tcarnevacuno=ft.Text(value="Carne de vacuno - 2,00 €/kg", color= "black", size=15, italic=True)
        tcarnecerdo=ft.Text(value="Carne de cerdo - 1,50 €/kg", color= "black", size=15, italic=True)
        tcarneroja=ft.Text(value="Carne roja - 3,50 €/kg", color= "black", size=15, italic=True)
        page.add( tcarnecerdo, tcarnevacuno, tcarnecerdo, tcarneroja,)


    def click_boton(e):
        usuario= ft.Text(value= "Por favor, seleccione una opción")
        page.add(usuario)
        boton_hortalizas= ft.ElevatedButton(text="Hotalizas", on_click= click_boton_hortalizas)
        boton_carnes= ft.ElevatedButton(text="Carnes", on_click= click_boton_carnes)
        row = ft.Row(spacing=50, controls=[boton_hortalizas, boton_carnes])
        page.add(row)
        page.remove(boton_correcto) 
    
    boton_correcto= ft.ElevatedButton(text="Es mi nombre", on_click= click_boton)
    page.add(boton_correcto)



    

ft.app(target=main)