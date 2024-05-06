from backend.users import Users
import re
import flet as ft

class SignUp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.pagenow = None
        self.container = None
        self.loading_indicator = ft.ProgressRing(visible=False)
        self.full_name = ""
        self.company = ""
        self.phone_number = ""
        self.email = ""
        self.email_confirm = ""
        self.password = ""
        self.password_confirm = ""
        self.suffix = ".com"
        self.username_validation = None
        self.password_validation = None
        self.login_button = None
        self.validation = False
        # self.config = Config()
        self.setup_ui()

    def format_phone_number(self, e):
        raw_number = e.control.value.replace("-", "").replace("(", "").replace(")", "").replace(" ", "").replace("+", "")
        if raw_number.startswith("1"):
            raw_number = raw_number[1:]

        print(raw_number)
        formatted_number = ""

        # Start constructing the formatted number
        if len(raw_number) > 0:
            formatted_number = "+" + raw_number[:2]  # Country code

        if len(raw_number) > 2:
            formatted_number += " (" + raw_number[2:4]  # Area code

        if len(raw_number) > 4:
            if len(raw_number) >= 13:
                formatted_number += ") " + raw_number[4:5] + " " + raw_number[5:9] + "-" + raw_number[9:13]
            else:
                formatted_number += ") " + raw_number[4:8]

        if len(raw_number) > 8 and len(raw_number) <= 12:
            formatted_number += "-" + raw_number[8:]
            
        formatted_number = formatted_number[:20]

        e.control.value = formatted_number
        self.phone_number.on_change = self.update_default_phone_number
        self.page.update()
        
    def update_default_full_name (self, e):
        self.page.update()
        if self.full_name.value:
            self.full_name.border_color = ft.colors.ORANGE
            self.full_name.label = "Nome Completo"
            self.full_name.label_style = ft.TextStyle(size=13, color=ft.colors.WHITE70)
            self.page.update()
            
    def update_default_phone_number (self, e):
        self.page.update()
        if self.phone_number.value:
            self.phone_number.border_color = ft.colors.ORANGE
            self.phone_number.label = "Telefone"
            self.phone_number.label_style = ft.TextStyle(size=13, color=ft.colors.WHITE70)
            self.page.update()
            self.phone_number.on_change = self.format_phone_number
            
    def update_default_email (self, e):
        self.page.update()
        if self.email.value:
            self.email.border_color = ft.colors.ORANGE
            self.email.label = "E-mail"
            self.email.label_style = ft.TextStyle(size=13, color=ft.colors.WHITE70)
            self.page.update()
            
    def update_default_email_confirm (self, e):
        self.page.update()
        if self.email_confirm.value:
            self.email_confirm.border_color = ft.colors.ORANGE
            self.email_confirm.label = "Confirmar E-mail"
            self.email_confirm.label_style = ft.TextStyle(size=13, color=ft.colors.WHITE70)
            self.page.update()         
            
    def update_default_password (self, e):
        self.page.update()
        if self.password.value:
            self.password.border_color = ft.colors.ORANGE
            self.password.label = "Confirmar E-mail"
            self.password.label_style = ft.TextStyle(size=13, color=ft.colors.WHITE70)
            self.page.update()      
            
    def update_default_password_confirm (self, e):
        self.page.update()
        if self.password_confirm.value:
            self.password_confirm.border_color = ft.colors.ORANGE
            self.password_confirm.label = "Confirmar E-mail"
            self.password_confirm.label_style = ft.TextStyle(size=13, color=ft.colors.WHITE70)
            self.page.update()                                 
        
    def on_click(self):
        self.validation_login = False
        errors = []  # Lista para armazenar mensagens de erro

        # Validação do nome completo
        if len(self.full_name.value.split()) < 2:
            errors.append("Full name must include at least two names.")
            self.full_name.border_color = ft.colors.RED
            self.full_name.label = "Digite o nome completo, nome e sobrenome!"
            self.full_name.label_style = ft.TextStyle(size=12, color=ft.colors.RED)
            self.page.update()

        # Validação do telefone
        phone_number_adjust = re.sub(r"[+\s()-]", "", self.phone_number.value)
        if not (len(phone_number_adjust) in [12, 13] and phone_number_adjust.isdigit()):
            errors.append("Phone number must contain 12 or 13 digits.")
            self.phone_number.border_color = ft.colors.RED
            self.phone_number.label = "Digite o Telefone correto +XX (XX) X XXXX-XXXX"
            self.phone_number.label_style = ft.TextStyle(size=12, color=ft.colors.RED)
            self.page.update()

        # Validação do e-mail
        if "@" not in self.email.value:
            errors.append("Email must contain '@'.")
            self.email.border_color = ft.colors.RED
            self.email.label = "E-mail incorreto"
            self.email.label_style = ft.TextStyle(size=12, color=ft.colors.RED)
            self.page.update()
            
            
        # Validação do e-mail
        if self.email.value != self.email_confirm.value or self.email_confirm.value == '':
            errors.append("Email not match the email confirmation.")
            self.email_confirm.border_color = ft.colors.RED
            self.email_confirm.label = "Os endereços de e-mail devem ser compativeis"
            self.email_confirm.label_style = ft.TextStyle(size=12, color=ft.colors.RED)
            self.page.update()            

        # Validação da senha
        password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{7,}$")
        if not password_pattern.match(self.password.value):
            errors.append("Password must be at least 7 characters long, include one uppercase letter, one lowercase letter, and one special character.")
            self.password.border_color = ft.colors.RED
            self.password.label = "A senha deve ter 7 caracteres, maiusculo, minisculo, número e caracter especial"
            self.password.label_style = ft.TextStyle(size=12, color=ft.colors.RED)
            self.page.update()     
            
        if not self.password.value != self.password_confirm.value or self.password_confirm == '':
            errors.append("Password not matched the password confirmation.")
            self.password_confirm.border_color = ft.colors.RED
            self.password_confirm.label = "As senhas devem ser compativeis"
            self.password_confirm.label_style = ft.TextStyle(size=12, color=ft.colors.RED)
            self.page.update()            

        if errors:
            for error in errors:
                print(error)
            return False

        return print('validado')
    
    def validation_login(self):
        users = Users()
        users.create_user(self.full_name.value, self.company.value, self.phone_number.value, self.email.value, self.password.value)
  

    def setup_ui(self):
        self.page.title = "Automate | Inscrever-se"
        self.page.window_height = 680
        self.page.window_width = 850
        self.page.window_min_height = self.page.window_height
        self.page.window_min_width = self.page.window_width
        
        self.title = ft.Text(
            "Inscreva-se no Automate",
            size=20,
            weight="bold"
        )
        
        self.full_name =  ft.TextField(
            label="Nome Completo",
            tooltip="Digite o nome completo",
            label_style=ft.TextStyle(size=13),
            height=50,
            width=240,
            text_size=13,
            border_radius=5,
            border_color=ft.colors.ORANGE,
        )
        
        self.company =  ft.TextField(
            label="Empresa",
            tooltip="Nome da Empresa",
            label_style=ft.TextStyle(size=13),
            height=50,
            width=240,
            text_size=13,
            border_radius=5,
            border_color=ft.colors.ORANGE,
        )
        
        self.phone_number =  ft.TextField(
            label="Telefone",
            tooltip="Digite o telefone",
            label_style=ft.TextStyle(size=13),
            height=50,
            width=240,
            text_size=13,
            border_radius=5,
            border_color=ft.colors.ORANGE,
            on_change=self.format_phone_number,
        )
        
        
        self.email =  ft.TextField(
            label="E-mail",
            tooltip="Digite o e-mail",
            label_style=ft.TextStyle(size=13),
            height=50,
            width=240,
            text_size=13,
            border_radius=5,
            border_color=ft.colors.ORANGE,
            suffix_text=".com"
        )
        
        self.email_confirm =  ft.TextField(
            label="Confirmar E-mail",
            tooltip="Confirme o e-mail",
            label_style=ft.TextStyle(size=13),
            height=50,
            width=240,
            text_size=13,
            border_radius=5,
            border_color=ft.colors.ORANGE,
            suffix_text=".com"
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
        )
        
        self.password_confirm = ft.TextField(
            password=True,
            can_reveal_password=True,
            label="Confirmar Senha",
            tooltip="Confirme a sua senha",
            label_style=ft.TextStyle(size=13),
            height=50,
            width=240,
            text_size=13,
            border_radius=5,
            border_color=ft.colors.ORANGE,
        )        
        
        self.signup =  ft.ElevatedButton(
            "Cadastrar",
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
            on_click=lambda e: self.on_click()
        )
        
        self.signin = ft.Row(
            controls=[
                ft.VerticalDivider(width=15),
                ft.Text("Já possui conta?"),
                ft.TextButton(
                    text="Clique Aqui",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.TRANSPARENT,
                        color=ft.colors.ORANGE,
                        padding=0,
                    ),
                ),
            ],
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
                    ft.Divider(color="#2F4F4F"),
                    self.full_name,
                    self.company,
                    self.phone_number,
                    self.email,
                    self.email_confirm,
                    self.password,
                    self.password_confirm,
                    self.signup,
                    self.signin
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
        
        self.full_name.on_change = self.update_default_full_name
        self.phone_number.on_change = self.update_default_phone_number
        self.email.on_change = self.update_default_email
        self.email_confirm.on_change = self.update_default_email_confirm
        self.password.on_change = self.update_default_password
        self.password_confirm.on_change = self.update_default_password_confirm

        self.page.add(self.container)
        
