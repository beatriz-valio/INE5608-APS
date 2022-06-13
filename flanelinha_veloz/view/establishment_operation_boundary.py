import PySimpleGUI as sg
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class EstablishmentOperationBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    UPDATE = 3
    WEEKDAYS_OPTIONS = ['Domingo', 'Segunda-feira', 'Terça-feira',
                        'Quarta-feira', 'Quinta-feira', 'Sexta-feira',
                        'Sábado']
    SCHEDULES = ['Domingo', 'Segunda-feira', 'Terça-feira',
                        'Quarta-feira', 'Quinta-feira', 'Sexta-feira',
                        'Sábado']
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def open_over_view(self, dias_de_funcionamento, horarios_de_funcionamento):
        layout = [
            [sg.Text('Estas são as configurações atuais de Funcionamento.', font='Arial 12', pad=5)],
            [sg.Text('Para editar, altere os valores e confirme as alterações.', font='Arial 14', pad=15)],
            [sg.Text("Dias de Funcionamento:", size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Listbox(values=EstablishmentOperationBoundary.WEEKDAYS_OPTIONS,
                        select_mode='extended',
                        default_values=dias_de_funcionamento,
                        key="dias_de_funcionamento",
                        size=(32, 7), pad=5)],
            [sg.Text("Abertura:", size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Spin([i for i in range(0, 24)], size=3,
                     initial_value=horarios_de_funcionamento[0],
                     key="abertura_estabelecimento_hora"),
             sg.Text("h"),
             sg.Spin([i for i in range(0, 60, 15)], size=3,
                     initial_value=horarios_de_funcionamento[1],
                     key="abertura_estabelecimento_minuto"),
             sg.Text("min", size=15)],
            [sg.Text("Fechamento:", size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Spin([i for i in range(0, 24)], size=3,
                     initial_value=horarios_de_funcionamento[2],
                     key="fechamento_estabelecimento_hora"),
             sg.Text("h"),
             sg.Spin([i for i in range(0, 60, 15)], size=3,
                     initial_value=horarios_de_funcionamento[3],
                     key="fechamento_estabelecimento_minuto"),
             sg.Text("min", size=15)],
            [sg.Cancel('Voltar', key=EstablishmentOperationBoundary.CANCEL, size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Submit('Confirmar Alterações', key=EstablishmentOperationBoundary.SUBMIT, size=EstablishmentOperationBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Funcionamento do Estabelecimento',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(80, 80)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button
