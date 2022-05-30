from ctypes import alignment
import PySimpleGUI as sg
import os
import flanelinha_veloz.view.abstract_boundary as AbstractBoundary

class MenuBoundary:
    SHUTDOWN = 0
    # VER_PERFIL = 1
    # MUDAR_PERFIL = 2
    # AGENDAR_LAVAGEM = 3
    # CADASTRAR_TIPO_SERV = 4



    def open_menu_client(self):

        layout = [
            [sg.Text('CLIENTE LOGADO COM SUCESSO!', font='Arial 16')],
            ]

        window = sg.Window('Flanelinha Veloz - Menu Cliente', layout=layout, size=(900, 500), element_justification="c")
        
        button, values = window.Read()
        window.close()
        return button



    def open_menu_manager(self):
        
        layout = [
            [sg.Text('GESTOR LOGADO COM SUCESSO!', font='Arial 16')],
            ]

        window = sg.Window('Flanelinha Veloz - Menu Gestor', layout=layout, size=(900, 500), element_justification="c")
        
        button, values = window.Read()
        window.close()
        return button



    def open_menu_employer(self):
    
        layout = [
            [sg.Text('FUNCIONÁRIO LOGADO COM SUCESSO!', font='Arial 16')],
            ]

        window = sg.Window('Flanelinha Veloz - Menu Funcionário', layout=layout, size=(900, 500), element_justification="c")
        
        button, values = window.Read()
        window.close()
        return button
