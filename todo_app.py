from custom_checkbox import CustomCheckbox
import flet as ft

def main(page: ft.Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    circle = ft.Stack(
        controls=[
            ft.Container(width=100, height=100, border_radius=50, bgcolor='white12'),
            ft.Container(
                gradient=ft.SweepGradient(
                    center=ft.alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=["#000000000", PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.Container(
                            padding=ft.padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=ft.Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=ft.CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_src="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
                                ),
                            ),
                        )
                    ],
                ),
            ),
        ]
    )
    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = ft.transform.Scale(
            0.8, alignment=ft.alignment.center_right
        )
        page_2.controls[0].border_radius = ft.border_radius.only(
            top_left=35, top_right=0, bottom_left=35, bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = ft.transform.Scale(1, alignment=ft.alignment.center_right)
        page_2.update()

    
    create_task_view = ft.Container(
        content=ft.Container(
            on_click=lambda _: page.go('/'), height=40, width=40, content=ft.Text("x")
        )
    )


    tasks = ft.Column(
        height=400,
        scroll="auto",
    )
    
    for i in range(10):
        tasks.controls.append(
            ft.Container(
                height=70,
                width=400,
                bgcolor=BG,
                border_radius=25,
                padding=ft.padding.only(
                    left=20,
                    top=20,
                ),
                content=CustomCheckbox(
                    color=PINK, 
                    label='Create interesting content!', 
                    
                ),
            ),
        )

    categories_card = ft.Row(
        scroll='auto'
    )

    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            ft.Container(
                border_radius=20,
                bgcolor=BG, 
                height=110, 
                width=170,
                padding=15,
                content=ft.Column(
                    controls=[
                        ft.Text('40 Tasks'),
                        ft.Text(category),
                        ft.Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=ft.padding.only(right=i*30),
                            content=ft.Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )
            )
        )

    first_page_contents = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment='spaceBetween',
                    controls=[
                        ft.Container(
                            content=ft.Icon(
                                ft.icons.MENU
                            ),
                            on_click=lambda e: shrink(e),
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SEARCH),
                                ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED),
                            ],
                        ),
                    ],
                ),

                ft.Container(height=20),

                ft.Text(
                    value='What\'s up, Olivia!'
                ),
                ft.Text(
                    value='CATEGORIES'
                ),
                ft.Container(
                    padding=ft.padding.only(top=10, bottom=20,),
                    content=categories_card,
                ),
                ft.Container(height=20),
                ft.Text("TODAY'S TASKS"),
                ft.Stack(
                    controls=[
                        tasks,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, 
                            on_click=lambda _: page.go('/create_task'),
                            bottom=90,
                            right=10,
                            bgcolor=PINK,
                        ),
                    ]
                ),
            ],
        ),
    )

    page_1 = ft.Container(
        bgcolor=BG,
        border_radius=35,
        padding=ft.padding.only(left=50, top=60, right=200),
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment='end',
                    controls=[
                        ft.Container(
                            border_radius=25,
                            padding=ft.padding.only(
                                top=13,
                                left=13,
                            ),
                            border=ft.border.all(color='white', width=1),
                            on_click=lambda e: restore(e),
                            content=ft.Text("<"),
                        )
                    ],
                ),
                ft.Container(height=20),
                circle,
                ft.Text("Olivia\nMitchel", size=32, weight='bold'),
                ft.Container(height=25),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.FAVORITE_BORDER_SHARP, color="white60"),
                        ft.Text(
                            "Templates",
                            size=15,
                            weight=ft.FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                ft.Container(height=5),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CARD_TRAVEL, color="white60"),
                        ft.Text(
                            "Templates",
                            size=15,
                            weight=ft.FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                ft.Container(height=5),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CALCULATE_OUTLINED, color="white60"),
                        ft.Text(
                            "Templates",
                            size=15,
                            weight=ft.FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                ft.Image(
                    src="https://raw.githubusercontent.com/1Mr-Newton/Flet-todo-app-Tutorials/refs/heads/master/assets/images/1.png",
                    width=300,
                    height=200,
                ),
                ft.Text(
                    "Good",
                    color=FG,
                    font_family="poppins",
                ),
                ft.Text(
                    "Consistency",
                    size=22,
                ),
            ]
        ),
    )

    page_2 = ft.Row(
        alignment="end",
        controls=[
            ft.Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                animate_scale=ft.animation.Animation(400, curve="decelerate"),
                padding=ft.padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=ft.Column(
                    controls=[
                        first_page_contents
                    ]
                ),
            )
        ],
    )

    container = ft.Container(
        width=400, 
        height=710, 
        bgcolor=BG,
        border_radius=35, 
        content=ft.Stack(
            controls=[
                page_1,
                page_2,
            ]
        ),
    )

    pages = {
        "/": ft.View(
            "/",
            [
                container,
            ],
        ),
        "/create_task": ft.View(
            "/create_task",
            [create_task_view],
        ),
    }

    def route_change(route):
        page.views.clear()
        new_view = pages[route.route]
        page.views.append(new_view)
        page.update()

    page.on_route_change = route_change
    page.go(page.route)



ft.app(target=main)
