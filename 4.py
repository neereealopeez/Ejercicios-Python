dropdown_carne = ft.Dropdown(width=200, options=[ft.dropdown.Option("Pechuga"),ft.dropdown.Option("Solomillo"),ft.dropdown.Option("Cordero")])

    row = ft.Row(spacing=50, controls=[dropdown_carne,textField_Nombre])
    page.add(row)