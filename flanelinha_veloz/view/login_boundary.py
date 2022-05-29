import PySimpleGUI as sg
import os
import flanelinha_veloz.view.abstract_boundary as AbstractBoundary

class LoginBoundary:
    ENTRAR = 0
    REGISTER_CLIENT = 1
    REGISTER_EMPLOYER = 2
    IMAGE_PATH = os.path.abspath('flanelinha_veloz/assets/logo.png')

    def open_screen(self):

        layout = [
            [sg.Image(LoginBoundary.IMAGE_PATH, subsample=2, pad=(35,35))],
            [sg.Text('Email')],
            [sg.Input(key='email')],
            [sg.Text('Senha')],
            [sg.Input(key='senha')],
            [sg.Button('Entrar', key=LoginBoundary.ENTRAR)],
            [sg.Text('Não possui cadastro?', pad=(5,25))],
            [sg.Button('Cadastro de Cliente', key=LoginBoundary.REGISTER_CLIENT)],
            [sg.Button('Cadastro de Funcionário', key=LoginBoundary.REGISTER_EMPLOYER)],
        ]

        window = sg.Window('Flanelinha Veloz', layout=layout)
        
        button, values = window.read()
        window.close()
        return button
