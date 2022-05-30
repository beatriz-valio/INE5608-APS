import PySimpleGUI as sg


class MenuBoundary:
    SHUTDOWN = 0
    OPEN_PROFILE = 1

    def open_menu_client(self):
        layout = [
            [sg.Text('CLIENTE LOGADO COM SUCESSO!', font='Arial 16')],
            [sg.Button('Ver perfil', key=MenuBoundary.OPEN_PROFILE)],
            [sg.Cancel('Sair', key=MenuBoundary.SHUTDOWN)]
        ]

        window = sg.Window('Flanelinha Veloz - Menu Cliente', layout=layout,
                           size=(900, 500), element_justification="c")

        button, values = window.Read()
        window.close()
        return button

    def open_menu_manager(self):
        layout = [
            [sg.Text('GESTOR LOGADO COM SUCESSO!', font='Arial 16')],
            [sg.Button('Ver perfil', key=MenuBoundary.OPEN_PROFILE)],
            [sg.Cancel('Sair', key=MenuBoundary.SHUTDOWN)]

        ]

        window = sg.Window('Flanelinha Veloz - Menu Gestor', layout=layout,
                           size=(900, 500), element_justification="c")

        button, values = window.Read()
        window.close()
        return button

    def open_menu_employer(self):
        layout = [
            [sg.Text('FUNCIONÁRIO LOGADO COM SUCESSO!', font='Arial 16')],
            [sg.Button('Ver perfil', key=MenuBoundary.OPEN_PROFILE)],
            [sg.Cancel('Sair', key=MenuBoundary.SHUTDOWN)]
        ]

        window = sg.Window('Flanelinha Veloz - Menu Funcionário',
                           layout=layout, size=(900, 500),
                           element_justification="c")

        button, values = window.Read()
        window.close()
        return button
