from flanelinha_veloz.view.abstract_boundary import AbstractBoundary
import PySimpleGUI as sg


class ClientBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1

    def open_screen(self):
        layout = [
            [sg.Button("Abrir gerência de Cursos", key=1)],
            [sg.Button("Abrir gerência de Disciplinas", key=2)],
            [sg.Button('Abrir gerência de Alunos', key=3)],
            [sg.Cancel('Voltar', key=ClientBoundary.CANCEL)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastramento',
                           size=(290, 290), element_justification='c') \
            .Layout(layout)
        button, value = window.Read()
        window.close()
        return button

    def open_update_screen(self):
        layout = [
            [sg.Button("Abrir gerência de Cursos", key=1)],
            [sg.Button("Abrir gerência de Disciplinas", key=2)],
            [sg.Button('Abrir gerência de Alunos', key=3)],
            [sg.Cancel('Voltar', key=ClientBoundary.CANCEL)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastramento',
                           size=(290, 290), element_justification='c') \
            .Layout(layout)
        button, value = window.Read()
        window.close()
        return button
