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
            [sg.Image(LoginBoundary.IMAGE_PATH, subsample=2, pad=(5,5))],
            [sg.Text('Email', font='Arial 11')],
            [sg.Input(key='email', size=(40,1))],
            [sg.Text('Senha', font='Arial 11')],
            [sg.Input(key='senha', size=(40,1))],
            [sg.Button('Entrar', size=(10,1), key=LoginBoundary.ENTRAR)],
            [sg.Text('Não possui cadastro?', pad=(1,20))],
            [sg.Button('Cadastro de Cliente', key=LoginBoundary.REGISTER_CLIENT), sg.Button('Cadastro de Funcionário', key=LoginBoundary.REGISTER_EMPLOYER)],
        ]

        window = sg.Window('Flanelinha Veloz - Realize seu login', layout=layout, size=(900, 500), element_justification="c")
        
        button, value = window.Read()
        window.close()
        return button