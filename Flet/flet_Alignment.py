import flet as ft

def box(n, color=ft.Colors.RED, w = 50, h = 50):
    return ft.Container(
        content = ft.Text(str(n), color = ft.Colors.WHITE, weight = ft.FontWeight.BOLD),
        width = w, height = h,
        bgcolor = color,
        alignment = ft.Alignment.CENTER,
        border_radius = 6,
    )
def frame(content, w = 420, h = 200):
    return ft.Container(
        content = content,
        width = w, height = h,
        border = ft.Border.all(1, ft.Colors.GREY),
        margin = ft.Margin.only(bottom=10),
    )
def title(text):
    return ft.Text(text, size = 20, weight = ft.FontWeight.BOLD)

def main(page: ft.Page):
    page.title = "Подсказка для студентов"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    page.window.width = 600
    page.window.height = 800

    # 1. В столбик
    page.add(title("1. Column (Вертикаль)"))
    for mode in (ft.MainAxisAlignment.START,
        ft.MainAxisAlignment.CENTER,
        ft.MainAxisAlignment.END,
        ft.MainAxisAlignment.SPACE_EVENLY,):

        page.add(ft.Text(f"Alignment: {mode.name}"))
        page.add(frame(ft.Column([box(1), box(2), box(3)], alignment = mode, expand = True,)))

    page.add(title("1.2 - Column (Горизонталь)"))
    for mode in (
        ft.CrossAxisAlignment.START,
        ft.CrossAxisAlignment.CENTER,
        ft.CrossAxisAlignment.END,
    ):
        page.add(ft.Text(f"Horizontal-Alignment: {mode.name}"))
        page.add(frame(
            ft.Column([box(1), box(2), box(3)],
                      horizontal_alignment = mode, width = 500,)
        ))
    #2 - Строка (Row)
    page.add(title("2 - ROW (Горизонталь)"))
    for mode in (
        ft.MainAxisAlignment.START,
        ft.MainAxisAlignment.CENTER,
        ft.MainAxisAlignment.END,
        ft.MainAxisAlignment.SPACE_EVENLY,
        ft.MainAxisAlignment.SPACE_AROUND,
        ft.MainAxisAlignment.SPACE_BETWEEN,
    ):
        page.add(ft.Text(f"Alignment: {mode.name}"))
        page.add(frame(ft.Row([box(1), box(2), box(3)], alignment = mode, expand = True,)))

    page.add(ft.Text("2.1 - Row (vertical)"))
    for mode in (
        ft.CrossAxisAlignment.START,
        ft.CrossAxisAlignment.CENTER,
        ft.CrossAxisAlignment.END,
    ):
        page.add(ft.Text(f"Alignment - vertical: {mode.name}"))
        page.add(frame(ft.Row([box(1, h = 30), box(2, h = 70), box(3, w = 90)], vertical_alignment = mode,)))
        h = 100,

ft.run(main)
