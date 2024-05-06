# from config import Config, Functions

import flet as ft

class Login:
    def __init__(self, page: ft.Page):
        self.page = page
        self.pagenow = None
        self.container = None
        self.loading_indicator = ft.ProgressRing(visible=False)
        self.incorrect_account = None
        self.username = None
        self.suffix = ".com"
        self.password = None
        self.login_button = None
        self.validation = False
        # self.config = Config()
        self.setup_ui()


    def update_login_button_state(self, e):
        self.login_button.disabled = not (self.username.value and self.password.value.strip())
        self.page.update()
        if self.username.value:
            self.username.border_color = ft.colors.ORANGE
            self.page.update()
        if self.password.value.strip():
            self.password.border_color = ft.colors.ORANGE
            self.page.update()

    def on_login_click(self, e):
        self.pagenow = self.container
        self.page.clean()
        self.overlay = ft.Container(
            content=self.loading_indicator,
            expand=True,
            width=self.page.window_width,
            height=self.page.window_height,
            alignment=ft.alignment.center
        )
        self.loading_indicator.visible = True
        self.page.add(self.overlay)
        self.page.update()

        import threading
        threading.Timer(2, self.end_loading).start()

    def end_loading(self):
        self.loading_indicator.visible = False

        self.validation = self.username.value == "admin" and self.password.value == "admin"
        self.page.remove(self.overlay)
        
        if self.validation:
            self.page.clean()
            pass
            # mainscreen = MainScreen(self.page)
            # mainscreen.setup_ui()
        else:
            self.username.border_color = ft.colors.RED
            self.password.border_color = ft.colors.RED
            self.open_banner_incorrect_account()
            self.page.add(self.pagenow)
            self.password.value = ""
            self.page.update()
                
    def open_banner_incorrect_account(self):
        self.page = self.incorrect_account
        self.incorrect_account.open = True

    def setup_ui(self):
        self.page.title = "Automate | Entrar"
        self.page.window_height = 680
        self.page.window_width = 850
        self.page.window_min_height = self.page.window_height
        self.page.window_min_width = self.page.window_width
        
        self.incorrect_account = ft.AlertDialog(
            title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        
        self.title = ft.Text(
            "Entrar",
            size=20,
            weight="bold"
        )
        self.divider = ft.Divider(height=120, color=ft.colors.TRANSPARENT)
        
        self.username =  ft.TextField(
                        suffix_text=self.suffix,
                        label="Usuário",
                        tooltip="Digite o seu usuário",
                        label_style=ft.TextStyle(size=13),
                        height=50,
                        width=240,
                        text_size=13,
                        border_radius=5,
                        border_color=ft.colors.ORANGE,
                        on_submit=self.on_login_click
                    )
        
        self.password = ft.TextField(
                        password=True,
                        can_reveal_password=True,
                        label="Senha",
                        tooltip="Digite a sua senha",
                        label_style=ft.TextStyle(size=13),
                        height=50,
                        width=240,
                        text_size=13,
                        border_radius=5,
                        border_color=ft.colors.ORANGE,
                        on_submit=self.on_login_click
                    )
        
        self.save_password = ft.Checkbox(
                            "Lembrar-me",
                            check_color=ft.colors.WHITE,
                            active_color=ft.colors.ORANGE,
                        )
        
        self.login_button =  ft.ElevatedButton(
                                "Entrar",
                                style=ft.ButtonStyle(
                                    animation_duration=500,
                                    side={
                                        ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.ORANGE),
                                        ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                                    },                                    
                                    shape={
                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                                    },
                                ),
                                height=50,
                                width=240,
                                bgcolor="#2F4F4F",
                                color=ft.colors.ORANGE,
                                tooltip="Clique para entrar",
                                disabled=True,
                                on_click=self.on_login_click
                    )
        
        self.singup =  ft.ElevatedButton(
                                "Inscrever-se",
                                style=ft.ButtonStyle(
                                    animation_duration=500,
                                    side={
                                        ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.ORANGE),
                                        ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                                    },                                    
                                    shape={
                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                                    },
                                ),
                                height=50,
                                width=240,
                                bgcolor="#2F4F4F",
                                color=ft.colors.ORANGE,
                                tooltip="Clique para se inscrever",
                                disabled=False,
                                on_click=None
                    )
        
        espace_left = ft.Container(
            expand=1,
        )
        
        
        left_container = ft.Container(
            content=
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "Automate",
                                    size=30,
                                    color="#2F4F4F",
                                    weight="bold"
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=ft.padding.only(left=90, bottom=-20, top=20),
                    ),
                    ft.Row(
                        controls=[
                            ft.Image(
                                src="icons/IntelliM/default_transparent_1000x1000.png",
                                height=150,
                                width=150,
                                color="#2F4F4F",
                            ),
                            ft.Container(
                                bgcolor="#2F4F4F",
                                height=80,
                                width=5,
                                border_radius=50,
                            ),
                            ft.Image(
                                src="icons/logoatenas.png",
                                height=150,
                                width=150,
                                color="#2F4F4F",
                            ),                    
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(left=90),
            bgcolor=ft.colors.ORANGE,
            height=600,
            width=500,
            margin=ft.margin.only(left=0, right=-20),
            border_radius=10,
        )

        right_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.title,
                    self.divider,
                    self.username,
                    self.password,
                    self.save_password,
                    self.login_button,
                    self.singup,
                    self.divider
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(left=30),
            bgcolor="#2F4F4F",
            height=600,
            width=300,
            margin=ft.margin.only(left=-5, right=0),
            border_radius=10,
        )

        espace_right = ft.Container(
            expand=1,
        )

        self.container = ft.Container(
            content=ft.Row(
                controls=[
                    espace_left,
                    left_container,
                    right_container,
                    espace_right
                ],
            ),
            expand=1,
        )

        self.username.on_change = self.update_login_button_state
        self.password.on_change = self.update_login_button_state

        self.page.add(self.container)
        
page = ft.app(target=Login)        
