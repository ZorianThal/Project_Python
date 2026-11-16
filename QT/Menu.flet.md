```python
import flet as ft

ACCENT = ft.Colors.INDIGO_400


def main(page: ft.Page):
    page.title = "Мои задачи"
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
    page.padding = 0
    page.window.width = 460
    page.window.height = 760

    tasks = []          # список словарей: {"text": str, "done": bool}
    state = {"filter": "all"}

    # ---------- элементы интерфейса ----------
    progress = ft.ProgressBar(value=0, height=8, color=ft.Colors.WHITE,
                              bgcolor=ft.Colors.with_opacity(0.25, ft.Colors.WHITE))
    stats = ft.Text("Задач пока нет", color=ft.Colors.WHITE70, size=14)
    task_list = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)
    new_task = ft.TextField(
        hint_text="Что нужно сделать?",
        expand=True,
        border_radius=14,
        filled=True,
        border_color=ft.Colors.TRANSPARENT,
        on_submit=lambda e: add_task(e),
    )

    # ---------- логика ----------
    def refresh():
        task_list.controls.clear()
        for t in tasks:
            if state["filter"] == "active" and t["done"]:
                continue
            if state["filter"] == "done" and not t["done"]:
                continue
            task_list.controls.append(build_card(t))

        if not task_list.controls:
            task_list.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE, size=56,
                                    color=ft.Colors.with_opacity(0.4, ACCENT)),
                            ft.Text("Здесь пусто", size=16,
                                    color=ft.Colors.with_opacity(0.6, ft.Colors.ON_SURFACE)),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=40,
                )
            )

        total = len(tasks)
        done = sum(1 for t in tasks if t["done"])
        progress.value = done / total if total else 0
        stats.value = f"Выполнено {done} из {total}" if total else "Задач пока нет"
        update_filter_buttons()
        page.update()

    def add_task(e):
        text = new_task.value.strip()
        if not text:
            return
        tasks.insert(0, {"text": text, "done": False})
        new_task.value = ""
        refresh()
        new_task.focus()

    def toggle(t, value):
        t["done"] = value
        refresh()

    def delete(t):
        tasks.remove(t)
        refresh()

    def set_filter(name):
        state["filter"] = name
        refresh()

    def toggle_theme(e):
        dark = page.theme_mode == ft.ThemeMode.DARK
        page.theme_mode = ft.ThemeMode.LIGHT if dark else ft.ThemeMode.DARK
        theme_btn.icon = ft.Icons.DARK_MODE if dark else ft.Icons.LIGHT_MODE
        page.update()

    def build_card(t):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Checkbox(value=t["done"],
                                on_change=lambda e, t=t: toggle(t, e.control.value)),
                    ft.Text(
                        t["text"],
                        expand=True,
                        size=16,
                        style=ft.TextStyle(
                            decoration=ft.TextDecoration.LINE_THROUGH if t["done"]
                            else ft.TextDecoration.NONE
                        ),
                        opacity=0.5 if t["done"] else 1,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        icon_color=ft.Colors.RED_300,
                        tooltip="Удалить",
                        on_click=lambda e, t=t: delete(t),
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.Padding(left=12, right=4, top=2, bottom=2),
            border_radius=16,
            bgcolor=ft.Colors.with_opacity(0.08, ACCENT),
            animate_opacity=300,
        )

    # ---------- фильтры ----------
    filter_names = {"all": "Все", "active": "Активные", "done": "Готовые"}
    filter_buttons = {}

    def update_filter_buttons():
        for key, btn in filter_buttons.items():
            selected = key == state["filter"]
            btn.bgcolor = ACCENT if selected else ft.Colors.with_opacity(0.1, ACCENT)
            btn.content.color = ft.Colors.WHITE if selected else None

    for key, label in filter_names.items():
        filter_buttons[key] = ft.Container(
            content=ft.Text(label, size=14, weight=ft.FontWeight.W_500),
            padding=ft.Padding(left=16, right=16, top=8, bottom=8),
            border_radius=20,
            ink=True,
            on_click=lambda e, k=key: set_filter(k),
        )

    # ---------- шапка ----------
    theme_btn = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        icon_color=ft.Colors.WHITE,
        tooltip="Сменить тему",
        on_click=toggle_theme,
    )

    header = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Мои задачи", size=30,
                                        weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                stats,
                            ],
                            spacing=2,
                        ),
                        theme_btn,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                progress,
            ],
            spacing=16,
        ),
        padding=ft.Padding(left=24, right=16, top=36, bottom=24),
        bgcolor=ft.Colors.INDIGO_500,
        border_radius=ft.BorderRadius(top_left=0, top_right=0,
                                      bottom_left=32, bottom_right=32),
        shadow=ft.BoxShadow(blur_radius=24,
                            color=ft.Colors.with_opacity(0.35, ft.Colors.INDIGO_500)),
    )

    add_row = ft.Row(
        [
            new_task,
            ft.IconButton(
                icon=ft.Icons.ADD,
                icon_color=ft.Colors.WHITE,
                bgcolor=ACCENT,
                icon_size=26,
                on_click=add_task,
                tooltip="Добавить",
            ),
        ],
        spacing=10,
    )

    body = ft.Container(
        content=ft.Column(
            [
                add_row,
                ft.Row(list(filter_buttons.values()), spacing=8),
                task_list,
            ],
            spacing=18,
            expand=True,
        ),
        padding=ft.Padding(left=20, right=20, top=20, bottom=20),
        expand=True,
    )

    page.add(ft.Column([header, body], spacing=0, expand=True))

    # стартовые задачи для примера
    tasks.extend([
        {"text": "Попробовать Flet", "done": True},
        {"text": "Сделать своё приложение", "done": False},
        {"text": "Выпить кофе", "done": False},
    ])
    refresh()


if __name__ == "__main__":
    # ft.run в новых версиях, ft.app в старых
    (ft.run if hasattr(ft, "run") else ft.app)(main)
```

```python
import flet as ft

BG = "#0F1020"
CARD = "#1A1B33"
ACCENT = "#7C5CFF"
ACCENT_2 = "#4ADEDE"
TEXT_DIM = "#9A9CC0"


def stat_card(icon, title, value, color):
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Icon(icon, color=color, size=22),
                    padding=10,
                    border_radius=12,
                    bgcolor=ft.Colors.with_opacity(0.15, color),
                ),
                ft.Text(value, size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(title, size=13, color=TEXT_DIM),
            ],
            spacing=8,
        ),
        expand=True,
        padding=18,
        border_radius=20,
        bgcolor=CARD,
    )


def activity_row(icon, title, subtitle, time, color):
    return ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Icon(icon, color=color, size=20),
                    width=44,
                    height=44,
                    border_radius=14,
                    bgcolor=ft.Colors.with_opacity(0.15, color),
                    alignment=ft.Alignment(0, 0),
                ),
                ft.Column(
                    [
                        ft.Text(title, size=15, weight=ft.FontWeight.W_600, color=ft.Colors.WHITE),
                        ft.Text(subtitle, size=12, color=TEXT_DIM),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Text(time, size=12, color=TEXT_DIM),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=14,
        border_radius=18,
        bgcolor=CARD,
    )


def main(page: ft.Page):
    page.title = "Dashboard"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG
    page.padding = 0
    page.window.width = 440
    page.window.height = 800

    header = ft.Row(
        [
            ft.Row(
                [
                    ft.CircleAvatar(
                        content=ft.Text("А", weight=ft.FontWeight.BOLD),
                        bgcolor=ACCENT,
                        radius=24,
                    ),
                    ft.Column(
                        [
                            ft.Text("Добрый день,", size=13, color=TEXT_DIM),
                            ft.Text("Алексей", size=20, weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE),
                        ],
                        spacing=0,
                    ),
                ],
                spacing=12,
            ),
            ft.Container(
                content=ft.Icon(ft.Icons.NOTIFICATIONS_NONE, color=ft.Colors.WHITE),
                padding=10,
                border_radius=14,
                bgcolor=CARD,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    balance = ft.Container(
        content=ft.Column(
            [
                ft.Text("Общий баланс", size=14, color=ft.Colors.with_opacity(0.8, ft.Colors.WHITE)),
                ft.Text("128 450 ₽", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Row(
                    [
                        ft.Icon(ft.Icons.TRENDING_UP, color=ft.Colors.WHITE, size=18),
                        ft.Text("+12,5% за месяц", size=13, color=ft.Colors.WHITE),
                    ],
                    spacing=6,
                ),
            ],
            spacing=6,
        ),
        padding=24,
        border_radius=28,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[ACCENT, "#4A6BFF", ACCENT_2],
        ),
        shadow=ft.BoxShadow(
            blur_radius=30,
            offset=ft.Offset(0, 10),
            color=ft.Colors.with_opacity(0.4, ACCENT),
        ),
    )

    stats = ft.Row(
        [
            stat_card(ft.Icons.ARROW_DOWNWARD, "Доходы", "84 200", "#4ADE80"),
            stat_card(ft.Icons.ARROW_UPWARD, "Расходы", "32 650", "#FB7185"),
        ],
        spacing=14,
    )

    activity = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Последние операции", size=18, weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE),
                    ft.Text("Все", size=14, color=ACCENT),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            activity_row(ft.Icons.SHOPPING_BAG_OUTLINED, "Покупки", "Магазин одежды", "−4 200 ₽", "#FBBF24"),
            activity_row(ft.Icons.COFFEE_OUTLINED, "Кофейня", "Утренний кофе", "−350 ₽", "#FB7185"),
            activity_row(ft.Icons.WORK_OUTLINE, "Зарплата", "Основной доход", "+84 200 ₽", "#4ADE80"),
        ],
        spacing=12,
    )

    nav = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.HOME_ROUNDED, color=ACCENT, size=28),
                ft.Icon(ft.Icons.PIE_CHART_OUTLINE, color=TEXT_DIM, size=28),
                ft.Icon(ft.Icons.CREDIT_CARD, color=TEXT_DIM, size=28),
                ft.Icon(ft.Icons.PERSON_OUTLINE, color=TEXT_DIM, size=28),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ),
        padding=16,
        margin=ft.Margin(left=20, right=20, top=0, bottom=16),
        border_radius=24,
        bgcolor=CARD,
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Column([header, balance, stats, activity], spacing=22,
                                      scroll=ft.ScrollMode.AUTO),
                    padding=ft.Padding(left=20, right=20, top=36, bottom=10),
                    expand=True,
                ),
                nav,
            ],
            spacing=0,
            expand=True,
        )
    )


if __name__ == "__main__":
    (ft.run if hasattr(ft, "run") else ft.app)(main)
```
