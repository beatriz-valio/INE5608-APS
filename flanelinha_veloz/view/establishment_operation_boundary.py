import PySimpleGUI as sg
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class EstablishmentOperationBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    UPDATE = 2
    WEEKDAYS_OPTIONS = ['Domingo', 'Segunda-feira', 'Terça-feira',
                        'Quarta-feira', 'Quinta-feira', 'Sexta-feira',
                        'Sábado']
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def list_establishment_screen(self, dias_de_funcionamento, horarios_de_funcionamento):
        layout = [
            [sg.Text('Estas são as configurações atuais de Funcionamento.', font='Arial 12', pad=5)],
            [sg.Text('Para editar, altere os valores e confirme as alterações.', font='Arial 14', pad=15)],
            [sg.Text("Dias de Funcionamento:", font='Arial 11',size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Listbox(values=dias_de_funcionamento,
                        select_mode='extended',
                        key="dias_de_funcionamento",
                        disabled=True,
                        size=(32, 7), pad=5)],
            [sg.Text("Abertura:", font='Arial 11', size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Spin([i for i in range(0, 24)], size=3, disabled=True,
                     initial_value=horarios_de_funcionamento[0],
                     key="abertura_estabelecimento_hora"),
             sg.Text("h"),
             sg.Spin([i for i in range(0, 60, 30)], size=3, disabled=True,
                     initial_value=horarios_de_funcionamento[1],
                     key="abertura_estabelecimento_minuto"),
             sg.Text("min", size=15)],
            [sg.Text("Fechamento:", font='Arial 11', size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Spin([i for i in range(0, 24)], size=3, disabled=True,
                     initial_value=horarios_de_funcionamento[2],
                     key="fechamento_estabelecimento_hora"),
             sg.Text("h"),
             sg.Spin([i for i in range(0, 60, 30)], size=3, disabled=True,
                     initial_value=horarios_de_funcionamento[3],
                     key="fechamento_estabelecimento_minuto"),
             sg.Text("min", size=15)],
            [sg.Cancel('Voltar', key=EstablishmentOperationBoundary.CANCEL, size=EstablishmentOperationBoundary.TEXT_SIZE, pad=20),
             sg.Cancel('Alterar', key=EstablishmentOperationBoundary.UPDATE, size=EstablishmentOperationBoundary.TEXT_SIZE, pad=20)]
        ]

        window = sg.Window('Flanelinha Veloz - Funcionamento do Estabelecimento',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(100, 100)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def menu_update_establishment_screen(self, dias_de_funcionamento, horarios_de_funcionamento):
        layout = [
            [sg.Text('Estas são as configurações atuais de Funcionamento.', font='Arial 12', pad=5)],
            [sg.Text('Para editar, altere os valores e confirme as alterações.', font='Arial 14', pad=15)],
            [sg.Text("Dias de Funcionamento:", font='Arial 11',size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Listbox(values=EstablishmentOperationBoundary.WEEKDAYS_OPTIONS,
                        select_mode='extended',
                        default_values=dias_de_funcionamento,
                        key="dias_de_funcionamento",
                        size=(32, 7), pad=5)],
            [sg.Text("Abertura:", font='Arial 11', size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Spin([i for i in range(0, 24)], size=3,
                     initial_value=horarios_de_funcionamento[0],
                     key="abertura_estabelecimento_hora"),
             sg.Text("h"),
             sg.Spin([i for i in range(0, 60, 30)], size=3,
                     initial_value=horarios_de_funcionamento[1],
                     key="abertura_estabelecimento_minuto"),
             sg.Text("min", size=15)],
            [sg.Text("Fechamento:", font='Arial 11', size=EstablishmentOperationBoundary.TEXT_SIZE),
             sg.Spin([i for i in range(0, 24)], size=3,
                     initial_value=horarios_de_funcionamento[2],
                     key="fechamento_estabelecimento_hora"),
             sg.Text("h"),
             sg.Spin([i for i in range(0, 60, 30)], size=3,
                     initial_value=horarios_de_funcionamento[3],
                     key="fechamento_estabelecimento_minuto"),
             sg.Text("min", size=15)],
            [sg.Cancel('Voltar', key=EstablishmentOperationBoundary.CANCEL, size=EstablishmentOperationBoundary.TEXT_SIZE, pad=20),
             sg.Submit('Confirmar', key=EstablishmentOperationBoundary.SUBMIT, size=EstablishmentOperationBoundary.TEXT_SIZE, pad=20)]
        ]

        window = sg.Window('Flanelinha Veloz - Funcionamento do Estabelecimento',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(100, 100)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button
