import PySimpleGUI as sg

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class MenuBoundary(AbstractBoundary):
    SHUTDOWN = 0
    OPEN_PROFILE = 1
    TEXT_SIZE = 20

    def open_menu_client(self):
        layout = [
            [sg.Text('Olá, cliente.', font='Arial 16', pad=10)],
            [sg.Text('O que gostaria de fazer hoje?', font='Arial 14', pad=10)],
            [sg.Button('Ver perfil', key=MenuBoundary.OPEN_PROFILE, size=MenuBoundary.TEXT_SIZE)],
            [sg.Cancel('Sair', key=MenuBoundary.SHUTDOWN, size=MenuBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Menu Cliente',
                           layout=layout,
                           size=(900, 500),
                           element_justification="c",
                           margins=(100,100))

        button, values = window.Read()
        window.close()
        return button

    def open_menu_manager(self):
        layout = [
            [sg.Text('Olá, gestor.', font='Arial 16', pad=10)],
            [sg.Text('O que gostaria de fazer hoje?', font='Arial 14', pad=10)],
            [sg.Button('Ver perfil', key=MenuBoundary.OPEN_PROFILE, size=MenuBoundary.TEXT_SIZE)],
            [sg.Button('Tipos de Veículos', key=2, size=MenuBoundary.TEXT_SIZE)],
            [sg.Button('Tipos de Serviços', key=3, size=MenuBoundary.TEXT_SIZE)],
            [sg.Cancel('Sair', key=MenuBoundary.SHUTDOWN, size=MenuBoundary.TEXT_SIZE)]

        ]

        window = sg.Window('Flanelinha Veloz - Menu Gestor',
                           layout=layout,
                           size=(900, 500),
                           element_justification="c",
                           margins=(100,100))

        button, values = window.Read()
        window.close()
        return button

    def open_menu_employer(self):
        layout = [
            [sg.Text('Olá, funcionário.', font='Arial 16')],
            [sg.Text('O que gostaria de fazer hoje?', font='Arial 14', pad=10)],
            [sg.Button('Ver perfil', key=MenuBoundary.OPEN_PROFILE, size=MenuBoundary.TEXT_SIZE)],
            [sg.Cancel('Sair', key=MenuBoundary.SHUTDOWN, size=MenuBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Menu Funcionário',
                           layout=layout,
                           size=(900, 500),
                           element_justification="c",
                           margins=(100,100))

        button, values = window.Read()
        window.close()
        return button
