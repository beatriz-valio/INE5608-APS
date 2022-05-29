import PySimpleGUI as sg
import os
import flanelinha_veloz.view.abstract_boundary as AbstractBoundary

class MenuBoundary:
    VER_PERFIL = 0

    def open_menu_client(self):

        layout = [
            [sg.Button('Ver Perfil', size=(10,1), key=MenuBoundary.VER_PERFIL)],
        ]

        window = sg.Window('Flanelinha Veloz - Menu Cliente', layout=layout, size=(900, 500), element_justification="c")
        
        button, value = window.Read()
        window.close()
        return button