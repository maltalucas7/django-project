import flet as ft

class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.selection_state = {}
        self.setup_ui()
        
    def on_select_changed(self, row_id, event):
        # Atualiza o estado de seleção com base no estado atual armazenado
        current_state = self.selection_state.get(row_id, False)
        self.selection_state[row_id] = not current_state
        print(f"Row {row_id} selection changed to {self.selection_state[row_id]}")
        self.update_table()
            
    def create_text_button_cell(self, text, icon, icon_color, button_color, width, cell_bgcolor, cell_border_radius):
        return ft.DataCell(
            ft.Container(
                ft.TextButton(
                    text=text,
                    icon=icon,
                    icon_color=icon_color,
                    style=ft.ButtonStyle(color=button_color),
                    width=width
                ),
                bgcolor=cell_bgcolor,
                border_radius=cell_border_radius
            )
        )

    def create_dropdown_cell(self, options, text_size, border_color, border_width, width, height):
        return ft.DataCell(
            ft.Container(
                content=ft.Dropdown(
                    options=[ft.dropdown.Option(opt) for opt in options],
                    text_size=text_size,
                    border_color=border_color,
                    border_width=border_width,
                ),
                width=width,
                height=height
            )
        )

    def create_text_cell(self, text):
        return ft.DataCell(ft.Text(text))

    def create_data_row(self, row_id, selected, on_select_changed, cells):
        selected = self.selection_state.get(row_id, False)
        return ft.DataRow(
            selected=selected,
            on_select_changed=on_select_changed,
            cells=cells,
        )    
    
    def open_about(self):
        self.about.open = True
        self.page.update()

    def close_about(self):
        self.about.open = False
        self.page.update()        

    def setup_ui(self):
        self.page.title = "Automate | Início"
        self.page.window_maximized = True

        send_button = ft.ElevatedButton(
            text="Enviar            ",
            color="white",
            bgcolor=ft.colors.ORANGE,
            icon=ft.icons.SEND_ROUNDED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },                                    
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )
        
        copy = ft.ElevatedButton(
            text="Copiar        ",
            color="white",
            icon=ft.icons.CONTENT_COPY_OUTLINED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },                                    
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )
        
        clean = ft.ElevatedButton(
            text="Limpar        ",
            color="white",
            icon=ft.icons.CLEANING_SERVICES_ROUNDED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },                                    
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )      
        
        upload = ft.ElevatedButton(
            text="Importar          ",
            color="white",
            icon=ft.icons.FILE_UPLOAD_OUTLINED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },                                    
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )
        
        
        messages = ft.ElevatedButton(
            text="Mensagens         ",
            color="white",
            icon=ft.icons.MESSAGE_OUTLINED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )
        
        parameters_button = ft.ElevatedButton(
            text="Parâmetros        ",
            color="white",
            icon=ft.icons.SETTINGS_SUGGEST_OUTLINED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )        
        
        settings_button = ft.ElevatedButton(
            text="Opções         ",
            color="white",
            icon=ft.icons.SETTINGS_OUTLINED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )
        
        self.about = ft.AlertDialog(
            title=ft.Text("Sobre", weight="bold"),
            content=ft.Column([ft.Text("Desenvolvido por Lucas Malta"), ft.Text("02/05/2024")], alignment=ft.MainAxisAlignment.START, height=100),
            actions=[
                ft.TextButton(text="Fechar", on_click=lambda e: self.close_about())
            ],
            on_dismiss=None
        )

        # Botão que abre o AlertDialog
        about_button = ft.ElevatedButton(
            text="Sobre                 ",
            color="white",
            icon=ft.icons.INFO_OUTLINE_ROUNDED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                }
            ),
            height=50,
            width=145,
            on_click=lambda e: self.open_about()
        )
        
        logout = ft.ElevatedButton(
            text="Sair              ",
            color="white",
            bgcolor=ft.colors.RED_400,
            icon=ft.icons.LOGOUT_ROUNDED,
            icon_color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                animation_duration=500,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.TRANSPARENT),
                    ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                },                                    
                shape={
                    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
            ),
            height=50,
            width=145,
            on_click=lambda e: print("Enviar clicked!"),
        )        
        
        menu_lateral = ft.Column(
            [
                send_button,
                copy,
                clean,
                upload,
                messages,
                ft.Container(expand=True),
                parameters_button,
                settings_button,
                about_button,
                logout,
            ],
        )
        
        divider = ft.VerticalDivider(
            thickness=0.1,
            color=ft.colors.WHITE
        )
        
        table = ft.Row(
            controls=[
                ft.DataTable(
                    # show_checkbox_column=True,
                    heading_text_style=ft.TextStyle(weight="bold", size=12),
                    data_text_style=ft.TextStyle(size=12),
                    expand=1,
                    columns=[
                        ft.DataColumn(
                            label=ft.Text("Status", text_align="center"),
                        ),
                        ft.DataColumn(
                            label=ft.Text("Mensagem"),
                        ),                                
                        ft.DataColumn(
                            label=ft.Text("Nome Cliente"),
                            tooltip="Nome completo do cliente",
                        ),
                        ft.DataColumn(
                            label=ft.Text("Contato Cliente"),
                            tooltip="Número de contato do cliente",
                        ),
                        ft.DataColumn(
                            label=ft.Text("Empresa"),
                            tooltip="Empresa do cliente",
                        ),
                        ft.DataColumn(
                            label=ft.Text("Negociador"),
                            tooltip="Responsável por negociações",
                        ),
                        ft.DataColumn(
                            label=ft.Text("Contato Negociador"),
                            tooltip="Contato do responsável por negociações",
                        ),
                        ft.DataColumn(
                            label=ft.Text("Mensagem", text_align="center"),
                            tooltip="Mensagens relevantes",
                            visible=False
                        ),
                    ],
                    rows=[
                        self.create_data_row(
                            row_id=1,
                            selected=True,
                            on_select_changed=lambda e, row_id=1: self.on_select_changed(row_id, e),
                            cells=[
                                self.create_text_button_cell("Falha", ft.icons.CIRCLE, ft.colors.RED_700, ft.colors.RED_700, 100, ft.colors.RED_100, 5),
                                self.create_dropdown_cell(["Modelo 1","Modelo 2","Modelo 3"], 12, "#2F4F4F", 0, 200, 100),
                                self.create_text_cell("João Silva"),
                                self.create_text_cell("1234"),
                                self.create_text_cell("Acme Corp"),
                                self.create_text_cell("Ana Souza"),
                                self.create_text_cell("987654321"),
                                self.create_text_cell("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."),
                            ]
                        ),                       
                    ],
                ),
            ],
        )
        
        body = ft.Column(
            [
                ft.Column(
                    [
                        ft.Dropdown(
                            label="Mensagem",
                            hint_text="Selecione a mensagem para enviar",
                            options=[
                                ft.dropdown.Option("Modelo Mensagem 1"),
                                ft.dropdown.Option("Modelo Mensagem 2"),
                                ft.dropdown.Option("Modelo Mensagem 3"),
                            ],
                            border_color="#ffffff",
                            border_width=0.5,
                        ),
                        ft.Row(
                            [
                                ft.TextField(
                                    label="Campo desejado",
                                    width=200,
                                    border_color="#ffffff",
                                    border_width=0.5,
                                ),
                                ft.ElevatedButton(
                                    "Adicionar",
                                    color="white",
                                    icon=ft.icons.ADD_ROUNDED,
                                    icon_color=ft.colors.WHITE,
                                    style=ft.ButtonStyle(
                                        animation_duration=500,
                                        side={
                                            ft.MaterialState.DEFAULT: ft.BorderSide(0.5, ft.colors.WHITE),
                                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE24),
                                        },
                                        shape={
                                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
                                            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                        },
                                    ),
                                    height=55,
                                    width=145,
                                    on_click=lambda e: print("Enviar clicked!"),
                                ),
                                ft.Dropdown(
                                    label="Campos desejados",
                                    hint_text="Selecione os campos",
                                    options=[
                                        ft.dropdown.Option("Status"),
                                        ft.dropdown.Option("Nome Cliente"),
                                        ft.dropdown.Option("Contato Cliente"),
                                        ft.dropdown.Option("Empresa"),
                                        ft.dropdown.Option("Negociador"),
                                        ft.dropdown.Option("Contato Negociador"),
                                        ft.dropdown.Option("Mensagem"),

                                    ],
                                    border_color="#ffffff",
                                    border_width=0.5,
                                    expand=7
                                ),
                            ],
                        ),             
                        ft.Divider(),
                        table,
                    ],
                ),
            ],
            expand=90
        )
        
        main_content = ft.Row(
            controls=[
                menu_lateral,
                divider,
                body
            ],
            expand=True
        )

        self.page.add(main_content)
        self.page.add(self.about)
        self.page.update()
        
page = ft.app(target=Main)                 