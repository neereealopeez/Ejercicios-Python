import flet as ft

def main(page: ft.Page):
    page.title = "Basic elevated buttons"
    page.add(
        ft.ElevatedButton(text="Elevated button", disabled=True),
    )

ft.app(target=main)