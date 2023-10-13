import flet as ft

def main(page: ft.Page):
    # Judul Halaman
    page.title = "Penghitung dengan Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    # "Minus" Button
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()
    
    # "Plus" Button
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ]
        )
    )
ft.app(target=main)