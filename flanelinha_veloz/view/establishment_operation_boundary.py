import PySimpleGUI as sg

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class EstablishmentOperationBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    UPDATE = 3
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def open_over_view(self):
        layout = [
            [sg.Text('Escolha uma opção abaixo caso deseje modificá-la', font='Arial 13', pad=10)],
            [sg.Button('Vagas', key=1, size=EstablishmentOperationBoundary.TEXT_SIZE),
            sg.Button('Dias de Funcionamento', key=2, size=EstablishmentOperationBoundary.TEXT_SIZE),
            sg.Button('Horários de Funcionamento', key=3, size=EstablishmentOperationBoundary.TEXT_SIZE)],
            [sg.Cancel('Voltar', key=EstablishmentOperationBoundary.CANCEL, size=EstablishmentOperationBoundary.TEXT_SIZE, pad=(1, 20))]
        ]

        window = sg.Window('Flanelinha Veloz - Funcionamento do Estabelecimento',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(50, 50)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button
