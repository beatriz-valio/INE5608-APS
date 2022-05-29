import PySimpleGUI as sg
import os
import flanelinha_veloz.view.abstract_boundary as AbstractBoundary

class MenuBoundary:
    SAIR = 0
    VER_PERFIL = 1
    MUDAR_PERFIL = 2
    AGENDAR_LAVAGEM = 3
    CADASTRAR_TIPO_SERV = 4



    def open_menu_client(self):

        layout = [
            [sg.Button('RF07 - Agendar Lavagem', size=(35,1), key=MenuBoundary.AGENDAR_LAVAGEM)],
            [sg.Button('Ver Perfil', size=(35,1), key=MenuBoundary.VER_PERFIL)],
            [sg.Button('Mudar Perfil', size=(35,1), key=MenuBoundary.MUDAR_PERFIL)],
            [sg.Button('Sair', size=(10,1), key=MenuBoundary.SAIR)],
        ]

        window = sg.Window('Flanelinha Veloz - Menu Cliente', layout=layout, size=(900, 500), element_justification="c")
        
        button, value = window.Read()
        window.close()
        return button



    def open_menu_manager(self):
        
        layout = [
            [sg.Button('RF04 - Cadastrar Tipo de Serviço', size=(35,1), key=MenuBoundary.CADASTRAR_TIPO_SERV)],
            [sg.Button('Ver Perfil', size=(35,1), key=MenuBoundary.VER_PERFIL)],
            [sg.Button('Mudar Perfil', size=(35,1), key=MenuBoundary.MUDAR_PERFIL)],
            [sg.Button('Sair', size=(10,1), key=MenuBoundary.SAIR)],
        ]

        window = sg.Window('Flanelinha Veloz - Menu Gestor', layout=layout, size=(900, 500), element_justification="c")
        
        button, value = window.Read()
        window.close()
        return button



    def open_menu_employer(self):
    
        layout = [
            [sg.Button('Ver Perfil', size=(35,1), key=MenuBoundary.VER_PERFIL)],
            [sg.Button('Mudar Perfil', size=(35,1), key=MenuBoundary.MUDAR_PERFIL)],
            [sg.Button('Sair', size=(10,1), key=MenuBoundary.SAIR)],
        ]

        window = sg.Window('Flanelinha Veloz - Menu Funcionário', layout=layout, size=(900, 500), element_justification="c")
        
        button, value = window.Read()
        window.close()
        return button
