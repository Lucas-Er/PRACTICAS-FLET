import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hola todooooos")))
    page.bgcolor = "#33a8ff"


ft.app(main)
